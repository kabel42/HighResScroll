A high res scroll wheel inspired by the [ploopy knob](https://github.com/ploopyco/knob)

Running micropython on a raspberry pi rp2040.
Connect a AS5600 or MT6701 to Pin 15 and 16.

USB lib from [micropython](https://docs.micropython.org/en/latest/library/machine.USBDevice.html) and [micropython-lib](https://github.com/micropython/micropython-lib/tree/master/micropython/usb) \
Descriptors based on [QMK](https://github.com/qmk/qmk_firmware/pull/24423/files#diff-9b81bdb526b5a64af607df29089326f9467bc3f12068661b20bc44bb6709d2f7R168) [QMK](https://github.com/eynsai/qmk_firmware/blob/b3a44e8e99787942e5d2f921ef449040ce3c9c4b/tmk_core/protocol/vusb/vusb.c#L527) and [HID-remapper](https://github.com/jfedor2/hid-remapper/blob/master/firmware/src/our_descriptor.cc#L82)

copy files with:
``` bash
mpremote connect /dev/ttyACM0 cp boot.py :/
mpremote connect /dev/ttyACM0 cp -r lib :/
```
for AS5600
``` bash
mpremote connect /dev/ttyACM0 cp AS5600_main.py :/main.py
```

for MT6701
``` bash
mpremote connect /dev/ttyACM0 cp MT6701_main.py :/main.py
```

TODO:
- receive and evaluate feature report, currently report length is 0 bytes
- measured values are sometimes twichy
