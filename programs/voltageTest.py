import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D8)
led.direction = Direction.OUTPUT

led.value = True