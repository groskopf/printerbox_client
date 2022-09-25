import subprocess


class Led:

    debugBlink: bool = True

    def __log(self, message : str):
        if(self.debugBlink):
            print(message)

    def off(self):
        self.__log("blinkOff")
        blinkCmd = ['blink1-tool', '--off', '/dev/null']
        subprocess.run(blinkCmd, capture_output=True)

    def constant_green(self, n = 1):
        self.__log("constant_green")
        blinkCmd = ['blink1-tool', '--green', '/dev/null']
        subprocess.run(blinkCmd, capture_output=True)

    def blink_red(self, n = 1):
        self.__log("blink_red")
        blinkCmd = ['blink1-tool', '--red', '--blink=' + str(n), '/dev/null']
        subprocess.run(blinkCmd, capture_output=True)
        self.constant_green()

    def blink_green(self, n = 1):
        self.__log("blink_green")
        blinkCmd = ['blink1-tool', '--green', '--blink=' + str(n), '/dev/null']
        subprocess.run(blinkCmd, capture_output=True)
        self.constant_green()

    def blink_blue(self, n = 1):
        self.__log("blink_blue")
        blinkCmd = ['blink1-tool', '--blue', '--blink=' + str(n), '/dev/null']
        subprocess.run(blinkCmd, capture_output=True)
        self.constant_green()

    def blink_magenta(self, n = 1):
        self.__log("blink_magenta")
        blinkCmd = ['blink1-tool', '--magenta', '--blink=' + str(n), '/dev/null']
        subprocess.run(blinkCmd, capture_output=True)
        self.constant_green()

class LedMock(Led):
    def off(self):
        pass

    def constant_green(self, n = 1):
        pass

    def blink_red(self, n = 1):
        pass

    def blink_green(self, n = 1):
        pass

    def blink_blue(self, n = 1):
        pass

    def blink_magenta(self, n = 1):
        pass


    