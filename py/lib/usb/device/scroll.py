# MicroPython USB Mouse module
#
# MIT license; Copyright (c) 2023-2024 Angus Gratton
from micropython import const
import struct
import machine

from usb.device.hid import HIDInterface

_INTERFACE_PROTOCOL_MOUSE = const(0x02)


class ScrollInterface(HIDInterface):
    def __init__(self, interface_str="MicroPython Scroll"):
        super().__init__(
            _MOUSE_REPORT_DESC,
            set_report_buf=bytearray(1),
            protocol=_INTERFACE_PROTOCOL_MOUSE,
            interface_str=interface_str,
        )
        self._buf = bytearray(1)
        self.lastSet = []

    def on_set_report(self, report_data, report_id, report_type):
        self.lastSet.append((bytes(report_data), report_id, report_type))
        print(report_data, report_id, report_type)

    def send_report(self, pos):
        struct.pack_into("B", self._buf, 0, pos)
        return super().send_report(self._buf)

_MOUSE_REPORT_DESC = (
    b'\x05\x01' # Usage Page (Generic Desktop)
    b'\x09\x02' #   Usage (Mouse)
    b'\xA1\x01' # Collection (Application)
    b'\x05\x01' #   Usage Page (Generic Desktop)
    b'\x09\x38' #   USAGE (Wheel)
    b'\xa1\x02' # COLLECTION (Logical)
    b'\x09\x48' #   USAGE (Resolution Multiplier)
    b'\x15\x00' #   LOGICAL_MINIMUM (0)
    b'\x25\x01' #   LOGICAL_MAXIMUM (1)
    b'\x35\x01' #   PHYSICAL_MINIMUM (1)
    b'\x45\x10' #   PHYSICAL_MAXIMUM (16)
    b'\x95\x01' #   REPORT_COUNT (1)
    b'\x75\x02' #   REPORT_SIZE (2)
    b'\xb1\x02' #   FEATURE (Data,Var,Abs)
    #b'\x35\x00' #   PHYSICAL_MINIMUM (0)
    #b'\x45\x00' #   PHYSICAL_MAXIMUM (0)
    #b'\x95\x01' #   REPORT_COUNT (1)
    #b'\x75\x06' #   REPORT_SIZE (6)
    #b'\xb1\x03' #   FEATURE (Cnst,Var,Abs)
    b'\x09\x38' #   USAGE (Wheel)
    b'\x15\x81' #   LOGICAL_MINIMUM (-127)
    b'\x25\x7f' #   LOGICAL_MAXIMUM (127)
    b'\x95\x01' #   REPORT_COUNT (1)
    b'\x75\x08' #   REPORT_SIZE (8)
    b'\x81\x06' #   INPUT (Data,Var,Rel)
    b'\xc0'     # END_COLLECTION
    b'\xc0'     # END_COLLECTION
)
