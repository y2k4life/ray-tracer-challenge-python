import math
from typing import Union
from pyray.raymath import fequal


class Point:
    """A particular position in space"""

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Vector") -> "Point":
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Point") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def subVector(self, other: "Vector") -> "Point":
        """Subtract a vector from a point"""
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float) -> "Point":
        return Point(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float) -> "Point":
        return Point(self.x / other, self.y / other, self.z / other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return fequal(self.x, other.x) & fequal(self.y, other.y) & fequal(
                self.z, other.z)

        return False


class Vector:
    """A quantity having direction as well as magnitude, especially as
    determining the position of one point in space relative to another"""

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self) -> float:
        """Calculate the distance/length represented by a vector"""
        return math.sqrt((self.x * self.x) + (self.y * self.y) +
                         (self.z * self.z))

    def normalized(self) -> "Vector":
        """Convert a vector into a unit vector"""
        m = self.magnitude()
        return Vector(self.x / m, self.y / m, self.z / m)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def addPoint(self, other: Point) -> Point:
        """Add point to vector"""
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float) -> "Vector":
        return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float) -> "Vector":
        return Vector(self.x / other, self.y / other, self.z / other)

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y, -self.z)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vector):
            return fequal(self.x, other.x) & fequal(
                self.y, other.y) & fequal(self.z, other.z)

        return False


def dot(a: Vector, b: Vector) -> float:
    """Calculate a scalar value of two vectors"""
    return a.x * b.x + a.y * b.y + a.z * b.z


def cross(a: Vector, b: Vector) -> Vector:
    """Calculate a right triangle to two vectors"""
    return Vector(a.y * b.z - a.z * b.y,
                  a.z * b.x - a.x * b.z,
                  a.x * b.y - a.y * b.x)
