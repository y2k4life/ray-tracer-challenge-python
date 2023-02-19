
import functools


class Matrix:
    """A particular position in space"""

    def __init__(self, r1c1: float, r1c2: float, r1c3: float, r1c4: float,
                 r2c1: float, r2c2: float, r2c3: float, r2c4: float,
                 r3c1: float, r3c2: float, r3c3: float, r3c4: float,
                 r4c1: float, r4c2: float, r4c3: float, r4c4: float):

        self.data = [[r1c1, r1c2, r1c3, r1c4],
                     [r2c1, r2c2, r2c3, r2c4],
                     [r3c1, r3c2, r3c3, r3c4],
                     [r4c1, r4c2, r4c3, r4c4]]

    def equals(self, other: 'Matrix') -> bool:
        """Check if this matrix equals another matrix"""

        isEqual = functools.reduce(lambda x, y: x and y,
                                   map(lambda p, q: p == q, self[0], other[0]),
                                   True)
        isEqual = isEqual & functools.reduce(lambda x, y: x and y,
                                             map(lambda p, q: p == q, self[1],
                                                 other[1]), True)
        isEqual = isEqual & functools.reduce(lambda x, y: x and y,
                                             map(lambda p, q: p == q, self[2],
                                                 other[2]), True)
        isEqual = isEqual & functools.reduce(lambda x, y: x and y,
                                             map(lambda p, q: p == q, self[3],
                                                 other[3]), True)
        return isEqual

    def __getitem__(self, index: int) -> list[float]:
        return self.data[index]
