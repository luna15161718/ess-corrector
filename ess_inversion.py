import math

def map(x, y):
    with open("oot-vc.bin", "rb") as file:
        table = file.read()
    index = 2 * (y * 128 + x)
    return(table[index], table[index + 1])

def get_quadrant(x, y):
    if x >= 128:
        if y >= 128:
            return 1
        else:
            return 4
    else:
        if y >= 128:
            return 2
        else:
            return 3

def normalise(x, y):
    quadrant = get_quadrant(x, y)
    if quadrant == 1 or quadrant == 4:
        x = x - 128
    else:
        x = min(128 - x, 127)
    if quadrant == 1 or quadrant == 2:
        y = y - 128
    else:
        y = min(128 - y, 127)
    return (quadrant, x, y)


def denormalise(quadrant, x, y):
    if quadrant == 1 or quadrant == 4:
        x = x + 128
    else:
        x = 128 - x
    if quadrant == 1 or quadrant == 2:
        y = y + 128
    else:
        y = 128 - y
    return (x, y)

def gc_to_n64(x, y):
    scale = math.fma((pow((math.fma(5, x, 2 * y)) / 525, 2) * (7 * y / 525)), 70 / 75 - 80 / 105, 80 / 105)
    return (min(math.ceil(x * scale), 127), min(math.ceil(y * scale), 127))
