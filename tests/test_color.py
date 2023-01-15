from pyray import Color


def test_colors_are_red_green_blue_tuples():
    """Colors are (red, green, blue) tuples (Chapter 2 page 16)"""
    c = Color(-0.5, 0.4, 1.7)
    assert c.red == -0.5
    assert c.green == 0.4
    assert c.blue == 1.7
