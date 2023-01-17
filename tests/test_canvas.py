import functools
from pyray import Canvas
from pyray import Color


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


def test_writing_pixels_to_a_canvas():
    """Writing pixels to a canvas (Chapter 2 page 19)"""
    c = Canvas(10, 20)
    red = Color(1, 0, 0)
    c.canvas[2][3] = red
    assert c.canvas[2][3] == red


def test_constructing_the_PPM_header():
    """Constructing the PPM header (Chapter 2 page 20 & 21)"""
    c = Canvas(5, 3)
    ppm = c.convert_to_ppm()
    lines = ppm.split('\n')
    assert lines[0] == "P3"
    assert lines[1] == "5 3"
    assert lines[2] == "255"


def test_constructing_the_PPM_pixel_data():
    """Constructing the PPM header (Chapter 2 page 20 & 21)"""
    c = Canvas(5, 3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)
    c.canvas[0][0] = c1
    c.canvas[2][1] = c2
    c.canvas[4][2] = c3
    ppm = c.convert_to_ppm()
    lines = ppm.split('\n')
    assert lines[3] == "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    assert lines[4] == "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0"
    assert lines[5] == "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"


def test_splitting_long_lines_in_PPM_files():
    """Splitting long lines in PPM files (Chapter 2 page 22)"""
    c = Canvas(10, 2)
    for row in range(2):
        for column in range(10):
            c.canvas[column][row] = Color(1, 0.8, 0.6)
    ppm = c.convert_to_ppm()
    lines = ppm.split('\n')
    assert lines[3] == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204"
    assert lines[4] == "153 255 204 153 255 204 153 255 204 153 255 204 153"
    assert lines[5] == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204"
    assert lines[6] == "153 255 204 153 255 204 153 255 204 153 255 204 153"


def test_PPM_files_are_terminated_by_a_newline_character():
    """PPM files are terminated by a newline character (Chapter 2 page 22)"""
    c = Canvas(10, 2)
    ppm = c.convert_to_ppm()
    lines = ppm.split('\n')
    lines[len(lines) - 1] = ""
