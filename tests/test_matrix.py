from pyray import Matrix
from pyray.matrix import IDENTITY_MATRIX
from pyray.raymath import float_equal
from pyray.tuples import Point


def test_constructing_and_inspecting_a_4x4_matrix():
    """Constructing and inspecting a 4x4 matrix (Chapter 3 page 26)"""

    M = Matrix(1, 2, 3, 4,
               5.5, 6.5, 7.5, 8.5,
               9, 10, 11, 12,
               13.5, 14.5, 15.5, 16.5)
    assert M[0][0] == 1
    assert M[0][3] == 4
    assert M[1][0] == 5.5
    assert M[1][2] == 7.5
    assert M[2][2] == 11
    assert M[3][0] == 13.5
    assert M[3][2] == 15.5


# Only building a 4x4 matrix
# Therefore 2x2 matrix and 3x3 matrix are subsets of the 4x4 grid
# the unused rows and columns will be filled with 0

def test_matrix_equality_with_identical_matrices():
    """Matrix equality with identical matrices (Chapter 3 page 27)"""

    A = Matrix(1, 2, 3, 4,
               5, 6, 7, 8,
               9, 10, 11, 12,
               13, 14, 15, 16)
    B = Matrix(1, 2, 3, 4,
               5, 6, 7, 8,
               9, 10, 11, 12,
               13, 14, 15, 16)

    assert A == B


def test_matrix_equality_with_different_matrices():
    """Matrix equality with different matrices (Chapter 3 page 27 & 28)"""

    A = Matrix(1, 2, 3, 4,
               5, 6, 7, 8,
               9, 8, 7, 6,
               5, 4, 3, 2)

    B = Matrix(2, 3, 4, 5,
               6, 7, 8, 9,
               8, 7, 6, 5,
               4, 3, 2, 1)

    assert A != B


def test_multiple_two_matrices():
    """Matrix equality with different matrices (Chapter 3 page 27 & 28)"""

    A = Matrix(1, 2, 3, 4,
               5, 6, 7, 8,
               9, 8, 7, 6,
               5, 4, 3, 2)

    B = Matrix(-2, 1, 2, 3,
               3, 2, 1, -1,
               4, 3, 6, 5,
               1, 2, 7, 8)

    expected = Matrix(20, 22, 50, 48,
                      44, 54, 114, 108,
                      40, 58, 110, 102,
                      16, 26, 46, 42)

    actual = A * B

    assert expected == actual

# This library does not have tuples but the two specific types
# of tuples, vector and point. Therefore the following tests
# are for those type and not generic tuples.
# As a reminder w = 0 is a vector and w = 1 is a point


def test_a_matrix_multiplied_by_a_point():
    """A matrix multiplied by a point (Chapter 3 page 30)"""

    A = Matrix(1, 2, 3, 4,
               2, 4, 4, 2,
               8, 6, 4, 1,
               0, 0, 0, 1)

    b = Point(1, 2, 3)

    expected = Point(18, 24, 33)

    actual = A.mul_point(b)

    assert actual == expected


def test_multiplying_a_matrix_by_the_identity_matrix():
    """Multiplying a matrix by the identity matrix (Chapter 3 page 32)"""

    M = Matrix(0, 1, 2, 4,
               1, 2, 4, 8,
               2, 4, 8, 16,
               4, 8, 16, 32)

    assert (M * IDENTITY_MATRIX) == M


def test_multiplying_the_identity_matrix_by_a_point():
    """Multiplying the identity matrix by a
    tuple (point) (Chapter 3 page 32)"""

    a = Point(1, 2, 3)

    assert IDENTITY_MATRIX.mul_point(a) == a


def test_transposing_a_matrix():
    """Transposing a matrix"""

    A = Matrix(0, 9, 3, 0,
               9, 8, 0, 8,
               1, 8, 5, 3,
               0, 0, 5, 8)

    expected = Matrix(0, 9, 1, 0,
                      9, 8, 8, 0,
                      3, 0, 5, 5,
                      0, 8, 3, 8)

    actual = A.transpose()

    assert expected == actual


def test_transposing_the_identity_matrix():
    """Transposing the identity matrix"""

    A = IDENTITY_MATRIX.transpose()

    assert A == IDENTITY_MATRIX


def test_calculating_the_determinant_of_a_2x2_matrix():
    """Calculating the determinant of a 2x2 matrix"""

    A = Matrix(1, 5, 0, 0,
               -3, 2, 0, 0,
               0, 0, 0, 0,
               0, 0, 0, 0)

    assert A.determinant(2) == 17


def test_a_sub_matrix_of_a_3x3_matrix_is_a_2x2_matrix():
    """A sub matrix of a 3x3 matrix is a 2x2 matrix"""

    A = Matrix(1, 5, 0, 0,
               -3, 2, 7, 0,
               0, 6, -3, 0,
               0, 0, 0, 0)

    expected = Matrix(-3, 2, 0, 0,
                      0, 6, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0)

    assert A.sub_matrix(0, 2) == expected


def test_a_sub_matrix_of_a_4x4_matrix_is_a_3x3_matrix():
    """A sub matrix of a 4x4 matrix is a 3x3 matrix"""

    A = Matrix(-6, 1, 1, 6,
               -8, 5, 8, 6,
               -1, 0, 8, 2,
               -7, 1, -1, 1,)

    expected = Matrix(-6, 1, 6, 0,
                      -8, 8, 6, 0,
                      -7, -1, 1, 0,
                      0, 0, 0, 0)

    assert A.sub_matrix(2, 1) == expected


def test_calculating_a_minor_of_a_3x3_matrix():
    """Calculating a minor of a 3x3 matrix"""

    A = Matrix(3, 5, 0, 0,
               2, -1, -7, 0,
               6, -1, 5, 0,
               0, 0, 0, 0)

    B = A.sub_matrix(1, 0)

    d = B.determinant(2)

    assert A.minor(1, 0, 2) == d


def test_calculating_a_cofactor_of_a_3x3_matrix():
    """Calculating a cofactor of a 3x3 matrix (Chapter 3 page 36)"""

    A = Matrix(3, 5, 0, 0,
               2, -1, -7, 0,
               6, -1, 5, 0,
               0, 0, 0, 0)

    assert A.minor(0, 0, 3) == -12
    assert A.cofactor(0, 0, 3) == -12


def test_calculating_the_determinant_of_3x3_matrix():
    """Calculating the determinant of a 3x3 matrix  (Chapter 3 page 37)"""

    A = Matrix(1, 2, 6, 0,
               -5, 8, -4, 0,
               2, 6, 4, 0,
               0, 0, 0, 0)
    assert A.cofactor(0, 0, 3) == 56
    assert A.cofactor(0, 1, 3) == 12
    assert A.cofactor(0, 2, 3) == -46
    assert A.determinant(3) == -196


def test_calculating_the_determinant_of_4x4_matrix():
    """Calculating the determinant of a 4x4 matrix (Chapter 3 page 37)"""

    A = Matrix(-2, -8, 3, 5,
               -3, 1, 7, 3,
               1, 2, -9, 6,
               - 6, 7, 7, -9)
    assert A.cofactor(0, 0) == 690
    assert A.cofactor(0, 1) == 447
    assert A.cofactor(0, 2) == 210
    assert A.determinant() == -4071


def test_testing_an_invertible_matrix_for_invertibility():
    """Testing an invertible matrix for invertibility (Chapter 3 page 39)"""

    A = Matrix(6, 4, 4, 4,
               5, 5, 7, 6,
               4, -9, 3, -7,
               9, 1, 7, -6)

    assert A.determinant() != 0


def test_testing_an_non_invertible_matrix_for_invertibility():
    """Testing an non-invertible matrix for invertibility (Chapter 3 page 39)"""

    A = Matrix(-4, 2, -2, -3,
               9, 6, 2, 6,
               0, -5, 1, -5,
               0, 0, 0, 0)

    assert A.determinant() == 0


def test_calculating_the_inverse_of_a_matrix():
    """Calculating the inverse of a matrix (Chapter 3 page 39)"""

    A = Matrix(-5, 2, 6, -8,
               1, -5, 1, 8,
               7, 7, -6, -7,
               1, -3, 7, 4)
    B = A.inverse()
    assert A.determinant() == 532
    assert float_equal(B[3][2], -160/532.0)
    assert A.cofactor(2, 3)
    assert float_equal(B[2][3], 105/532)
    expected = Matrix(0.21805,  0.45113,  0.24060, -0.04511,
                      -0.80827, -1.45677, -0.44361,  0.52068,
                      -0.07895, -0.22368, -0.05263,  0.19737,
                      -0.52256, -0.81391, -0.30075,  0.30639)
    assert expected == B


def test_calculating_the_inverse_of_another_matrix():
    """Calculating the inverse of another matrix (Chapter 3 page 41)"""

    A = Matrix(8.0, -5.0,  9.0,  2.0,
               7.0,  5.0,  6.0,  1.0,
               -6.0,  0.0,  9.0,  6.0,
               -3.0,  0.0, -9.0, -4.0)

    expected = Matrix(
        -0.15385, -0.15385, -0.28205, -0.53846,
        -0.07692,  0.12308,  0.02564,  0.03077,
        0.35897,  0.35897,  0.43590,  0.92308,
        -0.69231, -0.69231, -0.76923, -1.92308)

    assert A.inverse() == expected


def test_calculating_the_inverse_of_a_third_matrix():
    """Calculating the inverse of a third matrix (Chapter 3 page 41)"""

    A = Matrix(9.0,  3.0,  0.0,  9.0,
               -5.0, -2.0, -6.0, -3.0,
               -4.0,  9.0,  6.0,  4.0,
               -7.0,  6.0,  6.0,  2.0)

    expected = Matrix(-0.04074, -0.07778,  0.14444, -0.22222,
                      -0.07778,  0.03333,  0.36667, -0.33333,
                      -0.02901, -0.14630, -0.10926,  0.12963,
                      0.17778,  0.06667, -0.26667,  0.33333)

    assert A.inverse() == expected


def test_multiplying_a_product_by_its_inverse():
    """Multiplying a product by its inverse (Chapter 3 page 41)"""

    A = Matrix(3.0, -9.0,  7.0,  3.0,
               3.0, -8.0,  2.0, -9.0,
               -4.0,  4.0,  4.0,  1.0,
               -6.0,  5.0, -1.0,  1.0)
    B = Matrix(8.0,  2.0, 2.0, 2.0,
               3.0, -1.0, 7.0, 0.0,
               7.0,  0.0, 5.0, 4.0,
               6.0, -2.0, 0.0, 5.0)

    C = A * B

    assert C * B.inverse() == A
