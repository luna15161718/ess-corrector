from evdev import InputDevice, list_devices, UInput
from ess_inversion import gc_to_n64
import asyncio

def get_controllers():
    devices = [InputDevice(path) for path in list_devices()]
    global gcontroller
    for device in devices:
        print(device.path, device.name, device.phys)
        if device.phys == "usb-0000:13:00.4-2/input0":
            gcontroller = device
    print(device)
    create_controller()


async def read_input():
    async for ev in gcontroller.async_read_loop():
        vcontroller.write_event(ev)
        x = gcontroller.absinfo(0).value
        y = gcontroller.absinfo(1).value
        print("X - " + x)
        print("Y - " + y)


def create_controller():
    global vcontroller
    vcontroller = UInput.from_device(gcontroller, name="virtual-controller")
    print(gcontroller)
    print(vcontroller)
    