import time
import usb.device
from usb.device.scroll import ScrollInterface
from machine import Pin, I2C
import struct
import neopixel

s = ScrollInterface()
usb.device.get().init(s, builtin_driver=True)

while not s.is_open():
    time.sleep_ms(100)
