"""Skew-symmetric Matrix

    https://py.checkio.org/en/mission/skew-symmetric-matrix/

    In mathematics, particularly in linear algebra, a skew-symmetric matrix
    (also known as an antisymmetric or antimetric) is a square matrix A
    which is transposed and negative. This means that it satisfies the
    equation A = −AT. If the entry in the i-th row and j-th column is aij,
    i.e. A = (aij) then the symmetric condition becomes aij = −aji.

    You should determine whether the specified square matrix is skew-symmetric or not.

    Input: A square matrix as a list of lists with integers.
    Output: If the matrix is skew-symmetric or not as a boolean.

    Example:

    checkio([
        [ 0,  1,  2],
        [-1,  0,  1],
        [-2, -1,  0]]) == True
    checkio([
        [ 0,  1, 2],
        [-1,  1, 1],
        [-2, -1, 0]]) == False
    checkio([
        [ 0,  1, 2],
        [-1,  0, 1],
        [-3, -1, 0]]) == False

    Precondition: 0 < N < 5

    Output:
        checkio_product 0.0713
        checkio_product 0.0430
        checkio_product 0.0354
        checkio_zip 0.0296
        checkio_zip 0.0299
        checkio_zip 0.0291
        checkio_allclose 0.7690
        checkio_allclose 0.7574
        checkio_allclose 0.7623
"""
from timeit import timeit
from itertools import product
from numpy import allclose, array


def using_product(matrix):
    return not any(
        matrix[i][j] + matrix[j][i] for i, j in product(range(len(matrix)), repeat=2)
    )


def using_zip(matrix):
    return matrix == [[-x for x in row] for row in zip(*matrix)]


def using_allclose(matrix):
    return allclose(matrix, -array(matrix).T)


def using_classic(matrix):
    n = len(matrix)
    return not any(matrix[i][j] + matrix[j][i] for i in range(n) for j in range(i, n))


if __name__ == "__main__":
    tests = [
        ([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]], True),
        ([[0, 1, 2], [-1, 1, 1], [-2, -1, 0]], False),
        ([[0, 1, 2], [-1, 0, 1], [-3, -1, 0]], False),
    ]
    for func in [using_product, using_zip, using_allclose, using_classic]:
        for data, result in tests:
            assert func(data) is result
            t = timeit(stmt=f"func({data})", number=10_000, globals=globals())
            print(f"{func.__name__} {t:.4f}")
    print("PASSED!")
