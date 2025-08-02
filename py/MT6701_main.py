import time
import usb.device
from usb.device.scroll import ScrollInterface
from machine import Pin, I2C
import struct

s = ScrollInterface()
usb.device.get().init(s, builtin_driver=True)

while not s.is_open():
    time.sleep_ms(100)

time.sleep_ms(100)

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400_000)

def readAngle():
    return struct.unpack(">H", i2c.readfrom_mem(0x06, 0x03, 2))[0]>>2

last_angle = readAngle()
print("Go", last_angle)

while True:
    angle = readAngle()
    diff = angle-last_angle
    if diff > 8192:
        diff -= 16384
    elif diff < -8192:
        diff += 16384
    if diff:
        print(angle, last_angle, diff)
        if diff < 128 and diff > -128:
            s.send_report(diff)
    last_angle = angle
