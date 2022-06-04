import subprocess
import os
import json
import time
from datetime import date as date
from xmlrpc.client import Boolean

from blink import blinkBlue, blinkMagenta, blinkRed
from fast_api_client import Client
from fast_api_client.models.booking import Booking
from fast_api_client.models.printer_code import PrinterCode
from fast_api_client.api.name_tags import get_name_tag_name_tags_printer_code_filename_get, delete_name_tag_name_tags_printer_code_filename_delete
from fast_api_client.api.bookings import get_bookings_bookings_get


class PrinterBox:

    client: Client
    printerCode: PrinterCode
    debugPrinter = True
    booking: Booking
    disablePrinting: Boolean = False

    def __init__(self, apiUrl: str,  printerCode: PrinterCode, disablePrinting : Boolean):
        self.client = Client(base_url=f"https://{apiUrl}")
        self.printerCode = printerCode
        self.disablePrinting = disablePrinting

    def getBooking(self):
        today = date.today()  # FIXME today is not working correctly
        for booking in get_bookings_bookings_get.sync(client=self.client):
            if booking.printer_code == self.printerCode:
                if booking.start_date <= today and today <= booking.end_date:
                    print(f"Booking: {booking}")
                    self.booking = booking
                    return True
        return False

    def newMessage(self, message: str):
        filePath = json.loads(message)
        filename = os.path.basename(filePath['filename'])

        nameTagPdf = self.__downloadFile(filename)
        if not nameTagPdf:
            blinkRed(4)
            # continue
            return

        self.__saveFile(filename, nameTagPdf.content)

        if not self.__printFile(filename, self.booking.name_tag_type):
            self.blinkMagenta()

        blinkBlue()
        self.__deleteFile(filename)

        delete_name_tag_name_tags_printer_code_filename_delete.sync(client=self.client,
                                                                   printer_code=self.printerCode,
                                                                   filename=filename)

    def __downloadFile(self, filename: str):
        self.printPB("downloadFile({filename})")
        return get_name_tag_name_tags_printer_code_filename_get.sync_detailed(client=self.client,
                                                                             printer_code=self.printerCode,
                                                                             filename=filename)

    def __printFile(self, filename, labelname):
        print("Printing: " + filename)
        if self.disablePrinting:
            print("Printing disabled")
            return True

        media = 'media=' + labelname
        printCmd = ['lp', '-d', 'TD4550DNWB', '-h', 'printerbox_sortkaffe_cupsd_1',
                    '-o', media, '-o', 'BrTrimtape=OFF', filename]
        self.printPB(printCmd)
        output = subprocess.run(printCmd, capture_output=False)
        return output.returncode == 0

    def printPB(self, message: str):
        if self.debugPrinter:
            print(message)

    def __saveFile(self, filename, content):
        self.printPB(f"saveFile({filename})")
        file = open(filename, "wb")
        file.write(content)
        file.close()

    def __deleteFile(self, filename):
        self.printPB("deleteFile({filename})")
        os.remove(filename)
