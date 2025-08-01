A high res scroll wheel inspired by the [ploopy knob](https://github.com/ploopyco/knob)

Running micropython on a raspberry pi rp2040.
Connect a AS5600 to Pin 15 and 16.

USB lib from [micropython-lib](https://github.com/micropython/micropython-lib/tree/master/micropython/usb)

copy files with:
``` bash
mpremote connect /dev/ttyACM0 cp main.py :/
mpremote connect /dev/ttyACM0 cp -r lib :/
```

TODO:
- reveive and evaluate feature report, currently reports 0 bytes
- measured values are sometimes twichy
