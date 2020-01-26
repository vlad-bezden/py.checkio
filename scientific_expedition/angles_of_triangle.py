"""The angles of triangle.

You are given the lengths for each side on a triangle.
You need to find all three angles for this triangle.
If the given side lengths cannot form a triangle (or form a degenerated triangle),
then you must return all angles as 0 (zero).
The angles should be represented as a list of integers in ascending order.
Each angle is measured in degrees and rounded to the nearest integer number
(Standard mathematical rounding).

Input: The lengths of the sides of a triangle as integers.
Output: Angles of a triangle in degrees as sorted list of integers.
Example:

checkio(4, 4, 4) == [60, 60, 60]
checkio(3, 4, 5) == [37, 53, 90]
checkio(2, 2, 5) == [0, 0, 0]

How it is used: This is a classical geometric task.
The ideas can be useful in topography and architecture.
With this concept you can measure an angle without the need for a protractor.

Precondition:
0 < a,b,c ≤ 1000
"""

from math import acos, degrees
from typing import List

calc = lambda a, b, c: round(degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))))
rotate = lambda l, n: l[n:] + l[:n]


def checkio(a: int, b: int, c: int) -> List[int]:
    if a + b <= c:
        return [0, 0, 0]

    return sorted(calc(*rotate([a, b, c], i)) for i in range(3))


if __name__ == "__main__":
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(5, 4, 3) == [37, 53, 90], "Check for sorted order"
    print("Passed tests!!!")
