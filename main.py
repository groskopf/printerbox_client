from datetime import date
import websocket
import rel
import json
from asyncio import sleep

from blink import blinkOff
from fast_api_client.models.booking import Booking
from fast_api_client.models.printer_code import PrinterCode
from printerbox import PrinterBox


def printWS(message: str):
    if debugWebSocket:
        print(message)


def loadPrinterConfig():
    with open('/config/printerbox_config.json') as config_file:
        config = json.load(config_file)
        return config['config']



def onWSMessage(ws, message):
    printWS(message)
    printerBox.newMessage(message)


def onWSError(ws, error):
    printWS("### error ###: " + repr(error))


def onWSClose(ws, close_status_code, close_msg):
    printWS("### closed connection ###")
    printWS("status code: " + close_status_code)
    printWS("message: " + close_msg)


def onWSOpen(ws):
    printWS("### opened connection ###")


traceWebSocket = True
debugWebSocket = True

apiUrl = 'api.printerboks.dk/api/v1'
# apiUrl = 'localhost:8000'


if __name__ == "__main__":


    config = loadPrinterConfig()



    # TODO Should we do some getting async? We might fail printing and then not delete files we have received on WS

    #    blinkOff()

    print("Started")

    printerCode = config['boxid'] + '_' + config['number']
    printerBox = PrinterBox(apiUrl, printerCode)

    booking : Booking = None
    while not printerBox.getBooking():
        sleep(10) 

    websocket.enableTrace(traceWebSocket)
    # ws = websocket.WebSocketApp(f"ws://{apiUrl}/printers/{booking.printer_code}/ws",
    wsApp = websocket.WebSocketApp(f"wss://{apiUrl}/printers/XDESP95271_p/ws",
                                on_open=onWSOpen,
                                on_message=onWSMessage,
                                on_error=onWSError,
                                on_close=onWSClose)

    wsApp.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()

    print("Stopped")
