"""
Find Sequence Task

You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits.
The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

Input: A matrix as a list of lists with integers.
Output: Whether or not a sequence exists as a boolean.

Precondition:
0 ≤ len(matrix) ≤ 10
all(all(0 < x < 10 for x in row) for row in matrix)
"""

from itertools import groupby, chain
import numpy as np

MIN_N = 4


def check(arr):
    return any([1 for _, g in groupby(arr) if len(list(g)) >= MIN_N])


def diagonals(matrix):
    d = matrix.shape[0] - MIN_N
    diags = [matrix.diagonal(i) for i in range(-d, d + 1)]
    return diags


def checkio(matrix):
    np_d = np.array(matrix)
    return any(
        map(check, chain(np_d, np_d.T, diagonals(np_d), diagonals(np.rot90(np_d))))
    )


if __name__ == "__main__":
    assert (
        checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6], [1, 7, 2, 5]]) is True
    ), "Vertical"
    assert (
        checkio([[7, 1, 4, 1], [1, 2, 5, 2], [3, 4, 1, 3], [1, 1, 8, 1]]) is False
    ), "Nothing here"
    assert (
        checkio(
            [
                [2, 1, 1, 6, 1],
                [1, 3, 2, 1, 1],
                [4, 1, 1, 3, 1],
                [5, 5, 5, 5, 5],
                [1, 1, 3, 1, 1],
            ]
        )
        is True
    ), "Long Horizontal"
    assert (
        checkio(
            [
                [7, 1, 1, 8, 1, 1],
                [1, 1, 7, 3, 1, 5],
                [2, 3, 1, 2, 5, 1],
                [1, 1, 1, 5, 1, 4],
                [4, 6, 5, 1, 3, 1],
                [1, 1, 9, 1, 2, 1],
            ]
        )
        is True
    ), "Diagonal"

