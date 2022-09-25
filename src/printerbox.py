import subprocess
import os
import json
import time
from datetime import date as date
from xmlrpc.client import Boolean

from pydantic import BaseModel

from led import Led
from fast_api_client import AuthenticatedClient
from fast_api_client.models.booking import Booking
from fast_api_client.models.printer_code import PrinterCode
from fast_api_client.api.name_tags import get_name_tag_name_tags_booking_code_filename_get, delete_name_tag_name_tags_booking_code_filename_delete
from fast_api_client.api.bookings import get_bookings_bookings_get, get_bookings_bookings_printer_printer_code_get


class PrinterboxConfig(BaseModel):
    box_id: str
    number: str
    printing_disabled: Boolean
    access_token: str
    printer_server: str
    host_development: bool
    localhost_api: bool
    trace_websocket: bool
    debug_websocket: bool


class PrinterBox:

    client: AuthenticatedClient
    printerCode: PrinterCode
    debugPrinter = True
    booking: Booking
    printingDisabled: Boolean = False
    printer_label_code: str
    led: Led

    def __init__(self, apiUrl: str,  config: PrinterboxConfig, led: Led):
        self.client = AuthenticatedClient(
            base_url=f"{apiUrl}",
            token=config.access_token,
            prefix=None,
            auth_header_name="access_token")
        self.printerCode = PrinterCode(config.box_id + '_' + config.number)
        self.printingDisabled = config.printing_disabled
        self.printerServer = config.printer_server
        self.led = led

    def getBooking(self):
        try:
            self.booking = get_bookings_bookings_printer_printer_code_get.sync(
                printer_code=self.printerCode,
                client=self.client)
            if self.booking:
                return True
        except: 
            pass

        return None

    def readLabelFile(self):
        try:
            with open('/labels/' + self.booking.name_tag_type + '.txt', 'rt') as labelFile:
                labelName = labelFile.readline()
                self.printer_label_code = labelName.strip()
        except:
            return None

    def newMessage(self, message: str):
        filePath = json.loads(message)
        filename = os.path.basename(filePath['filename'])
        print("received: " + filename)

        nameTagPdf = self.__downloadFile(filename)
        if not nameTagPdf:
            self.led.blink_red(4)
            return

        self.__saveFile(filename, nameTagPdf.content)

        if self.__printFile(filename):
            self.led.blink_blue()
        else:
            self.led.blink_magenta()

        self.__deleteFile(filename)

        delete_name_tag_name_tags_booking_code_filename_delete.sync(client=self.client,
                                                                    booking_code=self.booking.booking_code,
                                                                    filename=filename)

    def __downloadFile(self, filename: str):
        self.printPB("downloadFile({filename})")
        return get_name_tag_name_tags_booking_code_filename_get.sync_detailed(client=self.client,
                                                                              booking_code=self.booking.booking_code,
                                                                              filename=filename)

    def __printFile(self, filename):
        print("Printing: " + filename)
        if self.printingDisabled:
            print("Printing disabled")
            return True

        media = 'media=' + self.printer_label_code
        printCmd = ['lp', '-d', 'TD4550DNWB', '-h', self.printerServer,
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
