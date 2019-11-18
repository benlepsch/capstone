# needs to be named code.py

import board, time
from digitalio import DigitalInOut, Direction, Pull
from info import delayTime

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

while True:
    led.value = True
    time.sleep(delayTime)
    led.value = False
    time.sleep(delayTime)
