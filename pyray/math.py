EPSILON: float = 0.00001


def fequal(a: float, b: float):
    """Comparing floating point numbers"""
    return abs(a - b) < EPSILON
