
from typing import Self, cast

from pyray.raymath import float_equal
from pyray.tuples import Point, Vector


class Matrix:
    """A data structure with 4 rows of 4 columns of floating point numbers.

    Regardless of a matrix size, for example a 3x3 matrix, the 4x4 matrix is
    used. This is for simplifications. Due to the computation expense the data
    form the inverse of the matrix is calculated when created. When an inverse
    is needed a Matrix is create with the inverse data."""

    def __init__(self, r1c1: float, r1c2: float, r1c3: float, r1c4: float,
                 r2c1: float, r2c2: float, r2c3: float, r2c4: float,
                 r3c1: float, r3c2: float, r3c3: float, r3c4: float,
                 r4c1: float, r4c2: float, r4c3: float, r4c4: float,
                 invert: bool = True):

        self.data = [[r1c1, r1c2, r1c3, r1c4],
                     [r2c1, r2c2, r2c3, r2c4],
                     [r3c1, r3c2, r3c3, r3c4],
                     [r4c1, r4c2, r4c3, r4c4]]

        self.__inverse = [[r1c1, r1c2, r1c3, r1c4],
                          [r2c1, r2c2, r2c3, r2c4],
                          [r3c1, r3c2, r3c3, r3c4],
                          [r4c1, r4c2, r4c3, r4c4]]

        if invert:
            self.__invert_matrix__()

    def __eq__(self, other: object) -> bool:
        """Check if this matrix equals another matrix."""

        other_matrix = cast(Matrix, other)
        for row in range(0, 4):
            for col in range(0, 4):
                if (float_equal(self[row][col],
                                other_matrix[row][col]) is not True):
                    return False

        return True

    def __getitem__(self, index: int) -> list[float]:
        """Get a row with in the matrix."""

        return self.data[index]

    def __str__(self) -> str:
        buffer = ''

        for row in range(0, 4):
            for col in range(0, 4):
                buffer = buffer + f' {self[row][col]:>12.5f}'
            buffer = buffer.rstrip() + '\n'
        return buffer

    def __mul__(self, other: object) -> Self:
        """Multiple matrix by another matrix."""

        other_matrix = cast(Matrix, other)
        m = Matrix(0, 0, 0, 0,
                   0, 0, 0, 0,
                   0, 0, 0, 0,
                   0, 0, 0, 0,
                   False)

        for row in range(0, 4):
            for col in range(0, 4):
                m[row][col] = self[row][0] * other_matrix[0][col] + \
                    self[row][1] * other_matrix[1][col] + \
                    self[row][2] * other_matrix[2][col] + \
                    self[row][3] * other_matrix[3][col]
                # This will remove signs zero values with a sign
                if float_equal(m[row][col], 0):
                    m[row][col] = 0

        m.__invert_matrix__()
        return m

    def mul_vector(self, vector: Vector) -> Vector:
        """Multiple matrix by vector."""

        x = (self[0][0] * vector.x) + (self[0][1] * vector.y) + \
            (self[0][2] * vector.z) + (self[0][3] * 0.0)
        y = (self[1][0] * vector.x) + (self[1][1] * vector.y) + \
            (self[1][2] * vector.z) + (self[1][3] * 0.0)
        z = (self[2][0] * vector.x) + (self[2][1] * vector.y) + \
            (self[2][2] * vector.z) + (self[2][3] * 0.0)

        return Vector(x, y, z)

    def mul_point(self, point: Point) -> Point:
        """Multiple matrix by point."""

        x = (self[0][0] * point.x) + (self[0][1] * point.y) + \
            (self[0][2] * point.z) + (self[0][3] * 1)
        y = (self[1][0] * point.x) + (self[1][1] * point.y) + \
            (self[1][2] * point.z) + (self[1][3] * 1)
        z = (self[2][0] * point.x) + (self[2][1] * point.y) + \
            (self[2][2] * point.z) + (self[2][3] * 1)

        return Point(x, y, z)

    def transpose(self) -> Self:
        """Transposes the matrix.

        Turn rows into columns and the columns into rows."""

        M = Matrix(0, 0, 0, 0,
                   0, 0, 0, 0,
                   0, 0, 0, 0,
                   0, 0, 0, 0,
                   False)
        for row in range(0, 4):
            for col in range(0, 4):
                M[row][col] = self[col][row]

        M.__invert_matrix__()
        return M

    def determinant(self, size: int = 4) -> float:
        """Calculate the determinant of a matrix.

        The determinant is used to determine if a system
        has a solution. if the calculated value is 0 then
        system has no solution.
        """

        det = 0

        if size <= 2:
            det = (self[0][0] * self[1][1]) - (self[0][1] * self[1][0])
        else:
            for col in range(0, size):
                det = det + self[0][col] * self.cofactor(0, col, size)

        return det

    def sub_matrix(self, row: int, col: int) -> Self:
        """Return a sub matrix of the matrix.

        Return a matrix of the matrix with the row and column of the
        matrix removed.
        """

        M = Matrix(0, 0, 0, 0,
                   0, 0, 0, 0,
                   0, 0, 0, 0,
                   0, 0, 0, 0,
                   False)

        row_counter = 0
        for i in range(0, 4):
            if i == row:
                continue
            col_counter = 0
            for j in range(0, 4):
                if j == col:
                    continue
                M[row_counter][col_counter] = self[i][j]
                col_counter = col_counter + 1
            row_counter = row_counter + 1

        return M

    def minor(self, row: int, col: int, size: int) -> float:
        """Calculate the minor of a matrix at row and column.

        The minor is the determinate of the sub matrix of the matrix
        with the row and column.
        """

        d = self.sub_matrix(row, col)
        return d.determinant(size - 1)

    def cofactor(self, row: int, col: int, size: int = 4) -> float:
        """Change the sign of a minor"""

        minor = self.minor(row, col, size)
        if (row + col) % 2 == 1:
            return minor * -1.0
        return minor

    def __invert_matrix__(self):
        """Calculate the data for the inverse of the matrix.

        The inverse matrix is only calculated if can be calculated.
        """

        d = self.determinant()
        if d != 0:
            for row in range(0, 4):
                for col in range(0, 4):
                    c = self.cofactor(row, col)

                    self.__inverse[col][row] = c / d

    def inverse(self) -> Self:
        """Create and return a inverse matrix.

        A matrix is create and return of the inverse data calculated
        when the matrix was created.
        """

        inverse = self.__inverse
        return Matrix(
            inverse[0][0], inverse[0][1], inverse[0][2], inverse[0][3],
            inverse[1][0], inverse[1][1], inverse[1][2], inverse[1][3],
            inverse[2][0], inverse[2][1], inverse[2][2], inverse[2][3],
            inverse[3][0], inverse[3][1], inverse[3][2], inverse[3][3])


IDENTITY_MATRIX = Matrix(1, 0, 0, 0,
                         0, 1, 0, 0,
                         0, 0, 1, 0,
                         0, 0, 0, 1,
                         False)

EMPTY_MATRIX = Matrix(0.0, 0.0, 0.0, 0.0,
                      0.0, 0.0, 0.0, 0.0,
                      0.0, 0.0, 0.0, 0.0,
                      0.0, 0.0, 0.0, 0.0,
                      False)
