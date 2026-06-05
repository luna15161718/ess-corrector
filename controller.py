import evdev
import asyncio

def get_controllers():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
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
        print(repr(ev))


def create_controller():
    global vcontroller
    vcontroller = evdev.UInput.from_device(gcontroller, name="virtual-controller")
    print(gcontroller)
    print(vcontroller)
    