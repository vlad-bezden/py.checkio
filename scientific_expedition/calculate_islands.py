"""Calculate Islands.


The Robots have found a chain of islands in the middle of the Ocean.
They would like to explore these islands and have asked for your help
calculating the areas of each island. They have given you a map of the territory.
The map is a 2D array, where 0 is water, 1 is land.
An island is a group of land cells surround by water.
Cells are connected by their edges and corners.
You should calculate the areas for each of the islands and return a
list of sizes (quantity of cells) in ascending order.
All of the cells outside the map are considered to be water.

Input: A map as a list of lists with 1 or 0.

Output: The sizes of island as a list of integers.

Precondition: 0 < len(land_map) < 10
all(len(land_map[0]) == len(row) for row in land_map)
any(any(row) for row in land_map)
"""

from collections import namedtuple
from itertools import chain, product
from typing import List, Set

LAND = 1

Point = namedtuple("Point", ["x", "y"])
Map = List[List[int]]


def count_land(land_map: Map, xy: Point) -> Set[Point]:
    visited: Set[Point] = set()
    to_visit: Set[Point] = set()
    result: Set[Point] = set()

    n = len(land_map)
    m = len(land_map[0])

    is_land = lambda x, y: 0 <= x < n and 0 <= y < m and land_map[x][y] == LAND
    get_land = lambda p: [
        Point(x, y)
        for x, y in product(range(p.x - 1, p.x + 2), range(p.y - 1, p.y + 2))
        if is_land(x, y)
    ]

    to_visit.add(xy)
    while to_visit:
        current = to_visit.pop()
        if current in visited:
            continue
        if land := get_land(current):
            to_visit.update(land)
            result.update(land)
        visited.add(current)

    return result


def checkio(land_map: Map) -> List[int]:
    result: List[Set[Point]] = []

    def coordinates():
        """Generate matrix coordinates (0, 0)...(n, m)."""
        return product(*map(range, [len(land_map), len(land_map[0])]))

    def is_land(p):
        """Check if point is a land and it's not processed yet."""
        return land_map[p.x][p.y] == LAND and p not in chain(*result)

    for i, j in coordinates():
        point = Point(i, j)
        if is_land(point):
            land = count_land(land_map, point)
            result.append(land)

    return sorted(map(len, result))


if __name__ == "__main__":
    assert checkio(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    ) == [1, 3], "1st example"
    assert checkio(
        [[0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [0, 1, 1, 0, 0]]
    ) == [5], "2nd example"
    assert checkio(
        [
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    ) == [2, 3, 3, 4], "3rd example"

    print("PASSED!!!")
