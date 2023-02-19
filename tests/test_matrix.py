import functools
from pyray import Matrix


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
# Therefore 2x2 matrix and 3x3 matrix are skipped
# these matrices are used but only internal to the library

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

    assert A.equals(B)


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

    assert A.equals(B) is False
