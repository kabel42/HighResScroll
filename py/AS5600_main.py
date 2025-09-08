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

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400_000)

def readAngle():
    return struct.unpack(">H", i2c.readfrom_mem(0x36, 0x0c, 2))[0]
def getMagnetPresent():
    return struct.unpack("B", i2c.readfrom_mem(0x36, 0x1a, 1))[0] < 100

last_angle = readAngle()
print("Go", last_angle)

while True:
    if not getMagnetPresent():
        print("no magnet")
        time.sleep_ms(100)
    else:
        angle = readAngle()
        diff = angle-last_angle
        if diff > 2048:
            diff -= 4096
        elif diff < -2048:
            diff += 4096
        if abs(diff) > 2:
            print(angle, last_angle, diff)
            if diff < 128 and diff > -128:
                s.send_report(diff)
            last_angle = angle
