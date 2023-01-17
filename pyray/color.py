from dataclasses import dataclass
from typing import Self
from pyray.raymath import float_equal


@dataclass(frozen=True, slots=True)
class Color:
    """A composite of three colors: red, green, and blue. Each be a value
    between 0 and 1"""
    red: float
    green: float
    blue: float

    def __add__(self, other: Self) -> Self:
        return Color(self.red + other.red, self.green + other.green,
                     self.blue + other.blue)

    def __sub__(self, other: Self) -> Self:
        return Color(self.red - other.red, self.green - other.green,
                     self.blue - other.blue)

    def __mul__(self, other: object) -> Self:
        if isinstance(other, Color):
            return Color(self.red * other.red, self.green * other.green,
                         self.blue * other.blue)
        if isinstance(other, float):
            return Color(self.red * other, self.green * other,
                         self.blue * other)
        if isinstance(other, int):
            return Color(self.red * other, self.green * other,
                         self.blue * other)

        raise ValueError(object)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Color):
            return float_equal(self.red, other.red) & float_equal(
                self.green, other.green) & float_equal(self.blue, other.blue)

        return False
