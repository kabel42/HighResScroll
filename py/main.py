import time
import usb.device
from usb.device.scroll import ScrollInterface
s = ScrollInterface()
usb.device.get().init(s, builtin_driver=True)

while not s.is_open():
    time.sleep_ms(100)

time.sleep_ms(100)

while True:
    if rp2.bootsel_button():
        print("scroll")
        s.send_report(1)
        while rp2.bootsel_button():
            time.sleep_ms(100)
