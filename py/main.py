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

last_angle = struct.unpack(">H", i2c.readfrom_mem(0x36, 0x0c, 2))[0]

print("Go", last_angle)

while True:
    agc = struct.unpack("B", i2c.readfrom_mem(0x36, 0x1a, 1))[0]
    if agc > 100:
        print("no magnet")
        time.sleep_ms(100)
    else:
        angle = struct.unpack(">H", i2c.readfrom_mem(0x36, 0x0c, 2))[0]
        diff = angle-last_angle
        if diff > 2048:
            diff -= 4096
        elif diff < -2048:
            diff += 4096
        if diff:
            print(angle, last_angle, diff)
            if diff < 128 and diff > -128:
                s.send_report(diff)
        last_angle = angle
