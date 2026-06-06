from evdev import InputDevice, list_devices, InputEvent, UInput, ecodes
from ess_inversion import normalise, gc_to_n64, ess_map, denormalise
import asyncio

def get_controllers():
    global table
    with open("oot-vc.bin", "rb") as file:
        table = file.read()
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
        x = gcontroller.absinfo(0).value
        y = gcontroller.absinfo(1).value
        x, y = process_input(x, y)
        new_x = InputEvent(0, 0, ecodes.EV_ABS, ecodes.ABS_X, x)
        new_y = InputEvent(0, 0, ecodes.EV_ABS, ecodes.ABS_Y, y)
        vcontroller.write_event(new_x)
        vcontroller.write_event(new_y)
        vcontroller.syn()
        print("5 - " + str(x))
        print("5 - " + str(y))


def process_input(x, y):
    print(1)
    print(x, y)
    should_swap = y > x
    quadrant, x, y = normalise(x, y)
    print(2)
    print(x, y)
    if should_swap:
        temp = x
        x = y
        y = temp
    x, y = gc_to_n64(x, y)
    print(3)
    print(x, y)
    if should_swap:
        temp = x
        x = y
        y = temp
    x, y = ess_map(table, x, y)
    print(4)
    print(x, y)
    x, y = denormalise(quadrant, x, y)
    return(x, y)


def create_controller():
    global vcontroller
    vcontroller = UInput.from_device(gcontroller, name="virtual-controller")
    print(gcontroller)
    print(vcontroller)
    