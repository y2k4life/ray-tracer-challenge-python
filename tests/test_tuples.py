from pyray import Vector, Point


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
    assert b + a == Point(1, 1, 6)


def test_adding_two_vectors():
    """Adding a two vectors (Chapter 1 page 6)"""
    a = Vector(3, -2, 5)
    b = Vector(-2, 3, 1)
    assert b + a == Vector(1, 1, 6)


def test_subtracting_two_points():
    """Subtracting two points (Chapter 1 page 6)"""
    p1 = Point(3, 2, 1)
    p2 = Point(5, 6, 7)
    assert p1 - p2 == Vector(-2, -4, -6)


def test_subtracting_a_vector_from_a_point():
    """Subtracting a vector from a point (Chapter 1 page 6)"""
    p1 = Point(3, 2, 1)
    p2 = Vector(5, 6, 7)
    assert p1 - p2 == Point(-2, -4, -6)


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
