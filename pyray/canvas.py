from pyray.color import Color


class Canvas:
    """Rectangular grid of pixels"""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.canvas = [[Color(0, 0, 0)]*width]*height
