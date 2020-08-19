"""Similar Triangles

    https://py.checkio.org/en/mission/similar-triangles/

    This is a mission to check the similarity of two triangles.

    You are given two lists as coordinates of vertices of each triangle.
    You have to return a bool. (The triangles are similar or not)

    Example:

    similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True
    similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False
    similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True

    Input:
    Two lists as coordinates of vertices of each triangle.
    Coordinates is three tuples of two integers.

    Output:
    True or False.

    Precondition:
    -10 ≤ x(, y) coordinate ≤ 10
"""

from __future__ import annotations
from math import dist
from typing import List, Tuple
from dataclasses import dataclass
from itertools import combinations

Coords = List[Tuple[int, int]]


@dataclass
class Triangle:
    a: float
    b: float
    c: float

    def __init__(self, coord: Coords):
        """Calculate degrees between a and b sides"""
        self.a, self.b, self.c = sorted(
            dist(c1, c2) for c1, c2 in combinations(coord, 2)
        )

    def is_similar(self, other: Triangle) -> bool:
        """Check if triangles are similar."""
        return (
            round(self.a / other.a, 2)
            == round(self.b / other.b, 2)
            == round(self.c / other.c, 2)
        )


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    return Triangle(coords_1).is_similar(Triangle(coords_2))


if __name__ == "__main__":
    assert (
        similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True
    ), "basic"
    assert (
        similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False
    ), "different #1"
    assert (
        similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True
    ), "scaling"
    assert (
        similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True
    ), "reflection"
    assert (
        similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True
    ), "scaling and reflection"
    assert (
        similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False
    ), "different #2"
    assert (
        similar_triangles([(2, -2), (1, 3), (-1, 4)], [(-10, 10), (-1, -8), (-4, 7)])
        is True
    )
    print("PASSED!!!")
