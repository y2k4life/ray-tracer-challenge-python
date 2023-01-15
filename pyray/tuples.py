from .math import fequal


class Vector:
    """A quantity having direction as well as magnitude, especially as
    determining the position of one point in space relative to another"""

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: object) -> "Vector | Point":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)

        raise ValueError('Incorrect type')

    def __sub__(self, other: object) -> 'Vector':
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

        raise ValueError('Incorrect type')

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y, -self.z)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vector):
            return fequal(self.x, other.x) & fequal(
                self.y, other.y) & fequal(self.z, other.z)

        return False


class Point:
    """A particular position in space"""

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: Vector) -> "Point":
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Point | Vector") -> "Vector | Point":
        if isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return fequal(self.x, other.x) & fequal(self.y, other.y) & fequal(
                self.z, other.z)

        return False
