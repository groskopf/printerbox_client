import websocket
import socket
import rel
import json
from time import sleep

from blink import blinkOff
from blink import ledGreen
from fast_api_client.models.booking import Booking
from fast_api_client.models.printer_code import PrinterCode
from printerbox import PrinterBox, PrinterboxConfig


def printWS(message: str):
    if debugWebSocket:
        print(message)


def loadPrinterConfig():
    with open('config/printerbox_config.json') as config_file:
        configDict = json.load(config_file)['config']
        return PrinterboxConfig(**configDict)


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


host_development: bool = True
localhost_api: bool = False
traceWebSocket: bool = True
debugWebSocket: bool = True

if __name__ == "__main__":

    if not host_development:
        blinkOff()
    print("Started")

    config = loadPrinterConfig()

    # TODO Should we do some getting async? We might fail printing and then not delete files we have received on WS

    if localhost_api:
        apiUrl = '127.0.0.1:8000'
        printerBox = PrinterBox(f"http://{apiUrl}", config)
    else:
        apiUrl = 'api.printerboks.dk/api/v1'
        printerBox = PrinterBox(f"https://{apiUrl}", config)

    while not printerBox.getBooking():
        sleep(5)

    print("Got booking code: " + printerBox.booking.booking_code)

    if not host_development:
        ledGreen()

        printerBox.readLabelFile()

    websocket.enableTrace(traceWebSocket)
    if localhost_api:
        websocketUrl = f'ws://{apiUrl}/name_tags/{printerBox.booking.booking_code}/ws'
    else:
        websocketUrl = f'wss://{apiUrl}/name_tags/{printerBox.booking.booking_code}/ws'

    wsApp = websocket.WebSocketApp(websocketUrl,
                                   on_open=onWSOpen,
                                   on_message=onWSMessage,
                                   on_error=onWSError,
                                   on_close=onWSClose)

    socketOptions = [(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1),
                     (socket.IPPROTO_TCP, socket.TCP_QUICKACK, 1),
                     (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)]
    wsApp.run_forever(dispatcher=rel,
                      sockopt=socketOptions)
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()

    print("Stopped")
