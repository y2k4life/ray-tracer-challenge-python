import functools
from pyray import Canvas


def test_creating_a_canvas():
    """Create a canvas (Chapter 2 page 19)"""
    c = Canvas(10, 20)
    total = 0
    for row in c.canvas:
        total = total + \
            functools.reduce(lambda a, r: r.red + r.green +
                             r.blue, row, 0)

    assert c.width == 10
    assert c.height == 20
    assert total == 0
