import math

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


def gc_to_n64(x, y):
    scale = math.fma((pow((math.fma(5, x, 2 * y)) / 525, 2) * (7 * y / 525)), 70 / 75 - 80 / 105, 80 / 105)
    return (min(math.ceil(x * scale), 127), min(math.ceil(y * scale), 127))
