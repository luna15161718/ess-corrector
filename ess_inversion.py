import math

def gc_to_n64(x, y):
    scale = math.fma((pow((math.fma(5, x, 2 * y)) / 525, 2) * (7 * y / 525)), 70 / 75 - 80 / 105, 80 / 105)
    return (min(math.ceil(x * scale), 127), min(math.ceil(y * scale), 127))