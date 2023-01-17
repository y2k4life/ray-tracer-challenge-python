from pyray import Color


def test_colors_are_red_green_blue_tuples():
    """Colors are (red, green, blue) tuples (Chapter 2 page 16)"""
    c = Color(-0.5, 0.4, 1.7)
    assert c.red == -0.5
    assert c.green == 0.4
    assert c.blue == 1.7


def test_adding_colors():
    """Adding colors (Chapter 2 page 17)"""
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    assert c1 + c2 == Color(1.6, 0.7, 1.0)


def test_subtracting_colors():
    """Subtracting colors (Chapter 2 page 17)"""
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    assert c1 - c2 == Color(0.2, 0.5, 0.5)


def test_multiplying_a_color_by_a_scalar():
    """Multiplying a color by a scalar (Chapter 2 page 17)"""
    c1 = Color(0.2, 0.3, 0.4)
    assert c1 * 2 == Color(0.4, 0.6, 0.8)


def test_multiplying_colors():
    """Multiplying colors (Chapter 2 page 17)"""
    c1 = Color(1, 0.2, 0.4)
    c2 = Color(0.9, 1, 0.1)
    assert c1 * c2 == Color(0.9, 0.2, 0.04)
