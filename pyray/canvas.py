from io import StringIO
from pyray.color import Color
from pyray.raymath import clamp


class Canvas:
    """Rectangular grid of pixels"""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.canvas = [[Color(0, 0, 0) for _ in range(height)]
                       for _ in range(width)]
        self._buffer = StringIO()
        self._line_length = 0

    def convert_to_ppm(self) -> str:
        """Convert canvas to PPM"""
        self._buffer = StringIO()
        self._line_length: int = 0

        self.append_line("P3")
        self.append_line(f"{self.width} {self.height}")
        self.append_line("255")

        for row in range(self.height):
            for col in range(self.width):
                self.append_color(self.canvas[col][row])
            self.append_line("")
            self._line_length = 0
        self.append_line("")
        self._line_length = 0
        return self._buffer.getvalue()

    def append_color(self, color: Color) -> None:
        """Append color to PPM buffer"""
        self.append_str(str(self.__to_rgb(color.red)))
        self.append_str(str(self.__to_rgb(color.green)))
        self.append_str(str(self.__to_rgb(color.blue)))

    def append_str(self, string: str) -> None:
        """Append a string to PPM"""
        if self._line_length == 0:
            self._line_length += len(string)
            self._buffer.write(string)
            return

        padded_string = f" {string}"
        if self._line_length + len(padded_string) > 70:
            self._line_length = len(string)
            self._buffer.write("\n")
            self._buffer.write(string)
        else:
            self._buffer.write(padded_string)
            self._line_length += len(padded_string)

    def append_line(self, string: str) -> None:
        """Append string with a new line"""
        self._buffer.write(string)
        self._buffer.write("\n")

    def close(self) -> None:
        """Close PPM buffer"""
        self._buffer.close()

    def __to_rgb(self, color: float) -> int:
        """Convert color to int"""
        return round(clamp(color, 0, 1) * 255)
