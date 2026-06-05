import evdev

def read_input():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        print(device.path, device.name, device.phys)
    device = evdev.InputDevice("/dev/input/event262")
    print(device)
    for event in device.read_loop():
        print(event)