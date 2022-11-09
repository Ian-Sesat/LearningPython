from time import *
from threading import *

def myDoor():
    while True:
        print('........My door is open')
        sleep(5)
        print('........My door is closed')
        sleep(5)

def myLED():
    while True:
        print('My LED is ON')
        sleep(1)
        print('My LED is OFF')
        sleep(1)

doorThread=Thread(target=myDoor)
LEDThread=Thread(target=myLED)

doorThread.daemon=True
LEDThread.daemon=True

doorThread.start()
LEDThread.start()

while True:
    pass

