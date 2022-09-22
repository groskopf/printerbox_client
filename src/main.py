from datetime import date
from xmlrpc.client import boolean
import websocket
import rel
import json
from asyncio import sleep

from blink import blinkOff
from blink import ledGreen
from fast_api_client.models.booking import Booking
from fast_api_client.models.printer_code import PrinterCode
from printerbox import PrinterBox, PrinterboxConfig

host_development : boolean = False


def printWS(message: str):
    if debugWebSocket:
        print(message)


def loadPrinterConfig():
    with open('config/printerbox_config.json') as config_file:
        configDict = json.load(config_file)['config']
        return  PrinterboxConfig(**configDict)


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

if __name__ == "__main__":

    if not host_development:
        blinkOff()
    print("Started")

    config = loadPrinterConfig()

    # TODO Should we do some getting async? We might fail printing and then not delete files we have received on WS

    if host_development:
        apiUrl = '127.0.0.1:8000'
        printerBox = PrinterBox(f"http://{apiUrl}", config)
    else:
        apiUrl = 'api.printerboks.dk/api/v1'
        printerBox = PrinterBox(f"https://{apiUrl}", config)

    while not printerBox.getBooking():
        sleep(5) 

    if not host_development:
        ledGreen()

        printerBox.readLabelFile()



    websocket.enableTrace(traceWebSocket)
    if host_development:
        websockerUrl = f'ws://{apiUrl}/name_tags/{printerBox.booking.booking_code}/ws'
    else:
        websockerUrl = f'wss://{apiUrl}/name_tags/{printerBox.booking.booking_code}/ws'
    wsApp = websocket.WebSocketApp(websocketUrl,
                                on_open=onWSOpen,
                                on_message=onWSMessage,
                                on_error=onWSError,
                                on_close=onWSClose)

    wsApp.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()

    print("Stopped")
