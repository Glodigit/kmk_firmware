import usb_hid
from micropython import const

from kmk.keys import AX, Key, MouseKey, make_key
from kmk.modules import Module
from kmk.scheduler import cancel_task, create_task

_USAGE_MOUSE = const(0x02)

class HiResScrollKey(Key):
    def __init__(self, code):
        self.code = code


class HiResScroll(Module):
    def __init__(self):
        pass

    def during_bootup(self, keyboard):
        # Find Pointer device
        for device in usb_hid.devices:
            if (
                device.usage == _USAGE_MOUSE
                and device.out_report_lengths[0] == 1
            ):
                self.hid = device
        if self.hid is None:
            raise RuntimeError
        
    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def before_hid_send(self, keyboard):
        #if self.hid.
        report = self.hid.get_last_received_report()

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return
    