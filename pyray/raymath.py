EPSILON: float = 0.00001


def float_equal(a: float, b: float):
    """Comparing floating point numbers"""
    return abs(a - b) < EPSILON
