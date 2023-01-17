EPSILON: float = 0.00001


def fequal(a: float, b: float):
    """Comparing floating point numbers"""
    return abs(a - b) < EPSILON


def clamp(num: float, min_value: float, max_value: float):
    """Clamp number between min max value"""
    return max(min(num, max_value), min_value)
