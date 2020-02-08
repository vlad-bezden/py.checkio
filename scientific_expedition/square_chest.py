"""The Square Chest.

On the chest keypad is a grid of numbered dots.
The grid is comprised of a square shaped array of dots and contains lines
that connect some pairs of adjacent dots. The answer to the code is the
number of squares that are formed by these lines.

The dots are marked by the numbers 1 through 16.
The endpoints of the lines are represented by lists of two numbers.

Input: A list of lines as a list of list. Each list consists of the two integers.

Output: The quantity of squares formed as an integer.

Example:

checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3
checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2

How it is used: This is a simple puzzle that illustrates pattern searching.
For complex cases you can improve your program and use it to search
for more complex patterns, shapes and objects.

Precondition:
0 < len(lines) ≤ 32
"""

from collections import defaultdict
from typing import Tuple, List, Dict, Set


Point = Tuple[int, int]

SIDE_SIZE = 4


def get_points_between(candidate: Point) -> List[Point]:
    """Gets points between top left corner and bottom right point of the square."""
    # number of rows between two points
    rows_num = (candidate[1] - candidate[0]) // SIDE_SIZE
    points = []

    for i in range(rows_num):
        right_point = candidate[0] + i
        bellow_point = candidate[0] + i * SIDE_SIZE
        left_point = candidate[1] - i
        above_point = candidate[1] - i * SIDE_SIZE
        points.append((right_point, right_point + 1))
        points.append((bellow_point, bellow_point + SIDE_SIZE))
        points.append((left_point - 1, left_point))
        points.append((above_point - SIDE_SIZE, above_point))

    return points


def count_squares(points: Set[Point], candidates: List[Point]) -> int:
    counter = 0

    for candidate in candidates:
        square_points = get_points_between(candidate)
        if all(line in points for line in square_points):
            counter += 1

    return counter


def checkio(lines_list: List[List[int]]) -> int:
    graph1: Dict[int, List[int]] = defaultdict(list)
    graph2: Dict[int, List[int]] = defaultdict(list)
    candidates: List[Point] = []
    # sort points from min to max and convert them to tuple
    points = {tuple(sorted(i)) for i in lines_list}

    # create to dictionaries. First with top left, second with bottom right points
    for x, y in points:
        graph1[x].append(y)
        graph2[y].append(x)

    length = max(graph2)
    diagonal_size = SIDE_SIZE + 1

    # get top left points of the square/rectangle
    top_left_points = [k for k, v in graph1.items() if 1 < len(v)]
    # get bottom right points of the square/rectangle
    bottom_right_points = [k for k, v in graph2.items() if 1 < len(v)]

    # find matches between top left and bottom right points
    for tl_point in top_left_points:
        point_between = range(tl_point + diagonal_size, length + 1, diagonal_size)
        candidates.extend(
            (tl_point, p) for p in point_between if p in bottom_right_points
        )

    return count_squares(points, candidates)


if __name__ == "__main__":
    result = checkio(
        [
            [1, 2],
            [3, 4],
            [1, 5],
            [2, 6],
            [4, 8],
            [5, 6],
            [6, 7],
            [7, 8],
            [6, 10],
            [7, 11],
            [8, 12],
            [10, 11],
            [10, 14],
            [12, 16],
            [14, 15],
            [15, 16],
        ]
    )

    assert (
        checkio(
            [
                [1, 2],
                [3, 4],
                [1, 5],
                [2, 6],
                [4, 8],
                [5, 6],
                [6, 7],
                [7, 8],
                [6, 10],
                [7, 11],
                [8, 12],
                [10, 11],
                [10, 14],
                [12, 16],
                [14, 15],
                [15, 16],
            ]
        )
        == 3
    ), "First, from description"
    assert (
        checkio(
            [
                [1, 2],
                [2, 3],
                [3, 4],
                [1, 5],
                [4, 8],
                [6, 7],
                [5, 9],
                [6, 10],
                [7, 11],
                [8, 12],
                [9, 13],
                [10, 11],
                [12, 16],
                [13, 14],
                [14, 15],
                [15, 16],
            ]
        )
        == 2
    ), "Second, from description"
    assert checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1, "Third, one small square"

    assert (
        checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0
    ), "Fourth, it's not square"

    assert (
        checkio([[16, 15], [16, 12], [15, 11], [11, 10], [10, 14], [14, 13], [13, 9]])
        == 0
    ), "Fifth, snake"

    expected = 4
    result = checkio(
        [
            [1, 2],
            [3, 4],
            [1, 5],
            [2, 6],
            [3, 7],
            [4, 8],
            [5, 6],
            [6, 7],
            [7, 8],
            [6, 10],
            [7, 11],
            [8, 12],
            [10, 11],
            [10, 14],
            [12, 16],
            [14, 15],
            [15, 16],
        ]
    )
    assert result == expected, f"Sixth. Mine, first modified from description.{result=}"

    expected = 3
    result = checkio(
        [
            [16, 15],
            [16, 12],
            [15, 11],
            [11, 12],
            [11, 10],
            [10, 14],
            [9, 10],
            [14, 13],
            [13, 9],
            [15, 14],
        ]
    )
    assert result == expected, f"Seven. {expected=}, {result=}"

    print("PASSED!!!")
