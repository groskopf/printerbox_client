import websocket
import socket
import rel
import json
from time import sleep

from led import LedMock, Led
from fast_api_client.models.booking import Booking
from fast_api_client.models.printer_code import PrinterCode
from printerbox import PrinterBox, PrinterboxConfig


def printWS(message: str):
    if config.debug_websocket:
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
    if close_status_code:
        printWS("status code: " + str(close_status_code))
    if close_msg:
    printWS("message: " + close_msg)


def onWSOpen(ws):
    printWS("### opened connection ###")


if __name__ == "__main__":

    print("Started")
    config = loadPrinterConfig()

    if config.host_development:
       led = LedMock()
    else:
        led = Led()
       
    led.off()

    if config.localhost_api:
        api_host = '127.0.0.1:8000'
        api_url = f"http://{api_host}"
    else:
        api_host = 'api.printerboks.dk/api/v1'
        api_url = f"https://{api_host}"

    printerBox = PrinterBox(api_url, config, led=led)
    
    while not printerBox.getBooking():
        sleep(5)

    print("Got booking code: " + printerBox.booking.booking_code)
    led.constant_green()
    
    if not config.host_development:
        printerBox.readLabelFile()

    websocket.enableTrace(config.trace_websocket)

    if config.localhost_api:
        websocketUrl = f'ws://{api_host}/name_tags/{printerBox.booking.booking_code}/ws'
    else:
        websocketUrl = f'wss://{api_host}/name_tags/{printerBox.booking.booking_code}/ws'

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
