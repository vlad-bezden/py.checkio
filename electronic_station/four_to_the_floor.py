"""Four to the Floor.
https://py.checkio.org/en/mission/four-to-the-floor/

Given a room's size and a list of PIR sensors mounted on the
room's ceiling and looking down on the floor, your task is to
determine whether the floor area is completely into the sensors
coverage area (return True) or not (return False).
The bottom left corner of the rectangle matches the origin point O,
the top right corner is defined by W and H. Each sensor is defined
by its mounting point (coordinates xi and yi) and its range (Ri).

Input: Two arguments:
the first is a list containing a room's top right corner coordinates,
all are integers [W, H]
the second is a list containing sensors info, all are integers
[[xi, yi, Ri], [xi+1, yi+1, Ri+1], ....., [xn, yn, Rn]]
Output: True or False.


Precondition:
All given values are integers.

if (int - 10e-6 < f < int + 10e-6) then (f == int)
H ∈ (0; 1000]
W ∈ [H; 4*H]
xi ∈ [0; W]
yi ∈ [0; H]
Ri ∈ (0; 1600]
n ∈ [1; 10]
"""

from itertools import product as product, starmap
from typing import List

Point = List[int]
Circle = List[int]


def is_covered(room: Point, sensors: List[Circle]) -> bool:
    def is_inside_circle(rx: int, ry: int) -> bool:
        """Check if point inside of the circle using revese Pythagorean theorem."""
        return any((rx - sx) ** 2 + (ry - sy) ** 2 <= r ** 2 for sx, sy, r in sensors)

    return all(starmap(is_inside_circle, product(*map(range, room))))


if __name__ == "__main__":
    assert is_covered([200, 150], [[100, 75, 130]]) is True
    assert is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]) is True
    assert (
        is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]) is False
    )
    assert (
        is_covered(
            [200, 150],
            [[100, 75, 100], [0, 40, 60], [0, 110, 60], [200, 40, 60], [200, 110, 60]],
        )
        is True
    )
    assert (
        is_covered(
            [200, 150],
            [[100, 75, 100], [0, 40, 50], [0, 110, 50], [200, 40, 50], [200, 110, 50]],
        )
        is False
    )
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 110]]) is False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 20]]) is False
    assert is_covered([3, 1], [[1, 0, 2], [2, 1, 2]]) is True
    assert (
        is_covered([30, 10], [[0, 10, 10], [10, 0, 10], [20, 10, 10], [30, 0, 10]])
        is True
    )
    assert (
        is_covered([30, 10], [[0, 10, 8], [10, 0, 7], [20, 10, 9], [30, 0, 10]])
        is False
    )
    assert (
        is_covered(
            [800, 800], [[0, 0, 500], [0, 800, 500], [800, 0, 500], [800, 800, 500]]
        )
        is False
    )

    print("PASSED!!!")
