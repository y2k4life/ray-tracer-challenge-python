import math
from pyray.tuples import Vector, Point, dot, cross


def test_create_a_point():
    """Create a Point (Chapter 1 page 4)"""
    a: Point = Point(4.3, -4.2, 3.1)
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1


def test_create_vector():
    """Subtracting a Vector (Chapter 1 page 4)"""
    a: Vector = Vector(4.3, -4.2, 3.1)
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1


def test_adding_a_vector_to_a_point():
    """Adding a vetor to a point (Chapter 1 page 6)"""
    a = Point(3, -2, 5)
    b = Vector(-2, 3, 1)
    assert a + b == Point(1, 1, 6)


def test_adding_a_point_to_a_vector():
    """Adding a point to a vector (Chapter 1 page 6)"""
    a = Point(3, -2, 5)
    b = Vector(-2, 3, 1)
    assert b.addPoint(a) == Point(1, 1, 6)


def test_adding_two_vectors():
    """Adding a two vectors (Chapter 1 page 6)"""
    a = Vector(3, -2, 5)
    b = Vector(-2, 3, 1)
    sut: Vector = b + a
    assert sut == Vector(1, 1, 6)


def test_subtracting_two_points():
    """Subtracting two points (Chapter 1 page 6)"""
    p1 = Point(3, 2, 1)
    p2 = Point(5, 6, 7)
    assert p1 - p2 == Vector(-2, -4, -6)


def test_subtracting_a_vector_from_a_point():
    """Subtracting a vector from a point (Chapter 1 page 6)"""
    p1 = Point(3, 2, 1)
    p2 = Vector(5, 6, 7)
    assert p1.subVector(p2) == Point(-2, -4, -6)


def test_subtracting_two_vectors():
    """Subtracting two vectors (Chapter 1 page 7)"""
    p1 = Vector(3, 2, 1)
    p2 = Vector(5, 6, 7)
    assert p1 - p2 == Vector(-2, -4, -6)


def test_subtracting_a_vector_from_the_zero_vector():
    """Subtracting a vector_from_the_zero_vector (Chapter 1 page 7)"""
    p1 = Vector(0, 0, 0)
    p2 = Vector(1, -2, 3)
    assert p1 - p2 == Vector(-1, 2, -3)


def test_negating_a_vector():
    """Negating a vector (Chapter 1 page 7)"""
    a = Vector(1, -2, 3)
    assert -a == Vector(-1, 2, -3)


def test_multiplying_a_point_by_a_scalar():
    """Multiplying a point by a scalar (Chapter 1 page 8)"""
    a = Point(1, -2, 3)
    assert a * 3.5 == Point(3.5, -7, 10.5)


def test_multiplying_a_point_by_a_fraction():
    """Multiplying a point by a scalar (Chapter 1 page 8)"""
    a = Point(1, -2, 3)
    assert a * 0.5 == Point(0.5, -1, 1.5)


def test_multiplying_a_vector_by_a_scalar():
    """Multiplying a vector by a scalar (Chapter 1 page 8)"""
    a = Vector(1, -2, 3)
    assert a * 3.5 == Vector(3.5, -7, 10.5)


def test_multiplying_a_vector_by_a_fraction():
    """Multiplying a vector by a scalar (Chapter 1 page 8)"""
    a = Vector(1, -2, 3)
    assert a * 0.5 == Vector(0.5, -1, 1.5)


def test_divide_a_point_by_a_scalar():
    """Multiplying a point by a scalar (Chapter 1 page 8)"""
    a = Point(1, -2, 3)
    assert a / 2.0 == Point(0.5, -1, 1.5)


def test_divide_a_vector_by_a_scalar():
    """Multiplying a point by a scalar (Chapter 1 page 8)"""
    a = Vector(1, -2, 3)
    assert a / 2.0 == Vector(0.5, -1, 1.5)


def test_computing_the_magnitude_of_vector_0_1_0():
    """Computer the magnitude of vector(0, 1, 0) (Chapter 1 page 9)"""
    v = Vector(0, 1, 0)
    assert v.magnitude() == 1


def test_computing_the_magnitude_of_vector_0_0_1():
    """Computer the magnitude of vector(0, 0, 1) (Chapter 1 page 9)"""
    v = Vector(0, 0, 1)
    assert v.magnitude() == 1


def test_computing_the_magnitude_of_vector_1_2_3():
    """Computer the magnitude of vector(1, 2, 3) (Chapter 1 page 9)"""
    v = Vector(1, 2, 3)
    assert v.magnitude() == math.sqrt(14)


def test_normalizing_vector_4_0_0_give_1_0_0():
    """Normalizing Vector(4, 0, 0) give Vector(1, 0, 0) (Chapter 1 page 10)"""
    v = Vector(4, 0, 0)
    assert v.normalized() == Vector(1, 0, 0)


def test_normalizing_vector_1_2_3():
    """Normalizing Vector(1, 2, 3) (Chapter 1 page 10)"""
    v = Vector(1, 2, 3)
    n = v.normalized()
    assert n == Vector(0.26726, 0.53452, 0.80178)


def test_dot_product_of_two_vectors():
    """The doct product of two tuples (Chapter 1 page 10)"""
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    assert dot(a, b) == 20


def test_cross_product_of_two_vectors():
    """The cross product of two vectors (Chapter 1 page 11)"""
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    assert cross(a, b) == Vector(-1, 2, -1)
    assert cross(b, a) == Vector(1, -2, 1)
