"""Black Holes

https://py.checkio.org/en/mission/black-holes/

You need to help Stephen implement a software model (function) that predicts the state
of black holes under a controlled environment.
The A&A research team has identified some peculiarities in the behavior of black holes.

To create the software model one should take into account:

1. The cartesian coordinate system is used to map out the black holes.
2. Each black hole is represented as a circle with x, y (center coordinates)
and r (radius).
3. In contrast to the area, which may change during the absorption process,
the coordinates remain constant.
4. The area of a black hole greatly influences its mass, and consequently,
the gravitational field.
5. The absorption order of black holes depends on the distance between their centers,
starting with the black holes that are closest to each other. If the distance between
different black holes is equal, then the leftmost black hole in the list
should merge first.
6. The absorption process (merging) of black holes is possible
if and only if the following conditions are met:
   - The intersection area of the two black holes is greater than or equal
   to 55% (>= 55%) of one of the two black holes area.
   - The area of one of the two black holes is over 20% (>= 20%)
   more than the area of the other.
7. If one black hole absorbs another, their areas are summarized as (Stotal = S1 + S2).
8. The absorption process continues as long as all conditions are met (see p. 6).
Let's look at some simple examples:


Input: A list of tuples [(x, y, r), ..., ...],
where x, y - coordinates, r - radius of a black hole

Output: Predictable (final) state of black holes as a list/tuple of lists/tuples,
radius should be given with two digits precision as ±0.01.

Precondition: 1 ≤ len(data) ≤ 20
0.5 ≤ radius ≤ 10
x ∈ [-100; 100], y ∈ [-100; 100]
"""

import math
from itertools import combinations


MIN_INTERSECTION = 0.55
MIN_DOMINATION = 0.2

distance = lambda p1, p2: math.dist(p1, p2)
area = lambda c: math.pi * c[2] ** 2


def intersection(c1, c2):
    """Finds intersection area of two circles.

    Returns intersection area of two circles otherwise 0
    """

    c1_x, c1_y, c1_r = c1
    c2_x, c2_y, c2_r = c2
    d = distance(c1[:2], c2[:2])
    rad1sqr = c1_r ** 2
    rad2sqr = c2_r ** 2

    if d == 0:
        # the circle centers are the same
        return math.pi * min(c1_r, c2_r) ** 2

    angle1 = (rad1sqr + d ** 2 - rad2sqr) / (2 * c1_r * d)
    angle2 = (rad2sqr + d ** 2 - rad1sqr) / (2 * c2_r * d)

    # check if the circles are overlapping
    if (-1 <= angle1 < 1) or (-1 <= angle2 < 1):
        theta1 = math.acos(angle1) * 2
        theta2 = math.acos(angle2) * 2

        area1 = (0.5 * theta2 * rad2sqr) - (0.5 * rad2sqr * math.sin(theta2))
        area2 = (0.5 * theta1 * rad1sqr) - (0.5 * rad1sqr * math.sin(theta1))

        return area1 + area2
    elif angle1 < -1 or angle2 < -1:
        # Smaller circle is completely inside the largest circle.
        # Intersection area will be area of smaller circle
        # return area(c1_r), area(c2_r)
        return math.pi * min(c1_r, c2_r) ** 2
    return 0


def get_candidates(data, processed):
    """Finds two plannets that needs to be processed based on min distance"""
    candidates = sorted(
        (distance(*p), p) for p in combinations(data, 2) if p not in processed
    )
    return candidates[0][1] if candidates else None


def absorption_process(c1, c2):
    S1 = area(c1)
    S2 = area(c2)
    domination = abs(S1 - S2) / min(S1, S2)
    intersect = intersection(c1, c2)
    if (
        MIN_INTERSECTION <= max(intersect / S1, intersect / S2)
        and MIN_DOMINATION <= domination
    ):
        c = max(c1, c2, key=lambda c: c[2])
        r = round(math.sqrt((S1 + S2) / math.pi), 2)
        return (*c[:2], r)
    return None


def checkio(data):
    processed = []

    while candidates := get_candidates(data, processed):
        if absorption_result := absorption_process(*candidates):
            data[data.index(candidates[0])] = absorption_result
            data.remove(candidates[1])
            processed = []
        else:
            processed.append(candidates)

    return data


if __name__ == "__main__":
    assert checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)], "First"
    assert checkio([(0, 0, 2), (-1, 1, 2)]) == [(0, 0, 2), (-1, 1, 2)], "Second"
    assert checkio([(1, 3, 2), (1, 3, 2.19)]) == [(1, 3, 2), (1, 3, 2.19)], "Third"
    assert checkio([(0, 0, 2), (-1, 0, 2)]) == [(0, 0, 2), (-1, 0, 2)], "Forth"
    assert checkio([(4, 3, 2), (2.5, 3.5, 1.4)]) == [(4, 3, 2.44)], "Fifth"
    assert checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)], "Sixth"
    assert checkio([(3, 3, 3), (2, 2, 1), (6, 3, 2)]) == [
        (3, 3, 3.16),
        (6, 3, 2),
    ], "Seventh"

    print("DONE!!!")
