from dataclasses import dataclass
import math
from typing import Self
from pyray.raymath import fequal


@dataclass(frozen=True, slots=True)
class Point:
    """A particular position in space"""

    x: float
    y: float
    z: float

    def __add__(self, other: 'Vector') -> Self:
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Self) -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def subVector(self, other: 'Vector') -> Self:
        """Subtract a vector from a point"""
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float) -> Self:
        return Point(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float) -> Self:
        return Point(self.x / other, self.y / other, self.z / other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return fequal(self.x, other.x) & fequal(self.y, other.y) & fequal(
                self.z, other.z)

        return False


@dataclass(frozen=True, slots=True)
class Vector:
    """A quantity having direction as well as magnitude, especially as
    determining the position of one point in space relative to another"""

    x: float
    y: float
    z: float

    def magnitude(self) -> float:
        """Calculate the distance/length represented by a vector"""
        return math.sqrt((self.x * self.x) + (self.y * self.y) +
                         (self.z * self.z))

    def normalized(self) -> Self:
        """Convert a vector into a unit vector"""
        m = self.magnitude()
        return Vector(self.x / m, self.y / m, self.z / m)

    def __add__(self, other: Self) -> Self:
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def addPoint(self, other: Point) -> Point:
        """Add point to vector"""
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Self) -> Self:
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float) -> Self:
        return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float) -> Self:
        return Vector(self.x / other, self.y / other, self.z / other)

    def __neg__(self) -> Self:
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
