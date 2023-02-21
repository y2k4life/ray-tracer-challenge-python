from pyray.matrix import IDENTITY_MATRIX, Matrix
from pyray.tuples import Point


i = IDENTITY_MATRIX

print("What happens when you invert the identity matrix?")
print()
print("Identity Matrix:")
print(i)

print("Inverted Identity Matrix:")
print(i.inverse())

print("--------------------------------------------------------------")
print("What do you get when you multiply a matrix by its inverse?")
print()
print("--------------------------------------------------------------")
print("What do you get when you multiply a matrix by its inverse?")
print()
A = Matrix(3.0, -9.0,  7.0,  3.0,
           3.0, -8.0,  2.0, -9.0,
           -4.0,  4.0,  4.0,  1.0,
           -6.0,  5.0, -1.0,  1.0)

print("Matrix A:")
print(A)
print("Inverse of matrix A:")
print(A.inverse())
print("Matrix A multiplied by its inverse:")
print(A * A.inverse())

print("--------------------------------------------------------------")
print("Is there any difference between:")
print()
print("  inverse of the transpose of matrix A")
print("            vs")
print("  transpose of the inverse of matrix A ")
print()
print("Inverse of the transpose of a matrix A")
print(A.transpose().inverse())

print("Transpose of the inverse of a matrix A")
print(A.inverse().transpose())

print("--------------------------------------------------------------")
i2 = Matrix(
    1.0, 0.0, 0.0, 0.0,
    0.0, 2.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0,
    0.0, 0.0, 0.0, 1.0)

p = Point(1.0, 2.0, 3.0)

print("Multiplying the identity matrix by a point (tuple):")
print()
print("Point:")
print(p)
print()
print("Multiplied by identity matrix:")
print()
print(i.mul_point(p))
print()
print("Changed identity matrix:")
print()
print(i2)
print()
print("Multiplied by change identity matrix:")
print()
print(i2.mul_point(p))

i2[0][0] = 3.0
i2[3][3] = 3.0
print()
print("Changed identity matrix:")
print()
print(i2)
print()
print("Multiplied by change identity matrix:")
print()
print(i2.mul_point(p))
