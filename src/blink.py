import subprocess

debugBlink = True

def printBL(message : str):
    if(debugBlink):
        print(message)

def blinkOff():
    printBL("blinkOff")
    blinkCmd = ['blink1-tool', '--off', '/dev/null']
    output = subprocess.run(blinkCmd, capture_output=True)
    return output.returncode  

def blinkRed(n = 1):
    printBL("blinkRed")
    blinkCmd = ['blink1-tool', '--red', '--blink=' + str(n), '/dev/null']
    output = subprocess.run(blinkCmd, capture_output=True)
    return output.returncode  

def blinkGreen(n = 1):
    printBL("blinkGreen")
    blinkCmd = ['blink1-tool', '--green', '--blink=' + str(n), '/dev/null']
    output = subprocess.run(blinkCmd, capture_output=True)
    return output.returncode  

def blinkBlue(n = 1):
    printBL("blinkBlue")
    blinkCmd = ['blink1-tool', '--blue', '--blink=' + str(n), '/dev/null']
    output = subprocess.run(blinkCmd, capture_output=True)
    return output.returncode  

def blinkMagenta(n = 1):
    printBL("blinkMagenta")
    blinkCmd = ['blink1-tool', '--magenta', '--blink=' + str(n), '/dev/null']
    output = subprocess.run(blinkCmd, capture_output=True)
    return output.returncode  
