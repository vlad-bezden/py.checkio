"""Inside Block

    https://py.checkio.org/en/mission/inside-block/

    When it comes to city planning it's important to understand the borders of
    various city structures. Parks, lakes or living blocks can be represented as
    closed polygon and can be described using cartesian coordinates on a map.
    We need a functionality to determine if a point (a building or a tree)
    lies inside the structure.

    For the purpose of this mission, a city structure may be considered a polygon
    represented as a sequence of vertex coordinates on a plane or map.
    The vertices are connected sequentially with the last vertex in the
    list connecting to the first. We are given the coordinates of the point
    which we need to check. If the point of impact lies on the edge of the
    polygon then it should be considered inside of it. For this mission, you
    need to determine whether the given point lies inside the polygon.

    For example, on the left image you see a polygon which is described by
    ((2,1),(1,5),(5,7),(7,7),(7,2)) and the point at (2,7). The result is False.
    For the right image the point lies on the edge and gets counted as inside the
    polygon, making the result True.

    Input: Two arguments. Polygon coordinates as a tuple of tuples
    with two integers each. A checking point coordinates as a tuple of two integers.

    Output: Whatever the point inside the polygon or not as a boolean.

    Precondition:
    all(x ≥ 0 and y ≥ 0 for x, y in polygon)
    point[0] ≥ 0 and point[1] ≥ 0
"""


from typing import Tuple

Point = Tuple[int, int]


def is_inside(polygon: Tuple[Point, ...], point: Point) -> bool:
    x, y = point
    # check if point is a vertex
    if (x, y) in polygon:
        return True
    inside = False
    p1x, p1y = polygon[-1]
    x_intersect = 0.0
    for p2x, p2y in polygon:
        # check if point is on a boundary
        if p1x == p2x and p1x == x and y > min(p1y, p2y) and x < max(p1y, p2y):
            return True
        if p1y == p2y and p1y == y and x > min(p1x, p2x) and x < max(p1x, p2x):
            return True
        # check if point is inside of boundary
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        x_intersect = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= x_intersect:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


if __name__ == "__main__":
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (2, 2)) is True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)), (4, 2)) is False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)), (3, 2)) is True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)), (3, 3)) is False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)), (4, 3)) is True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)), (4, 3)) is False, "Sixth"
    assert (
        is_inside(
            ((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)), (3, 3)
        )
        is True
    ), "Seventh"
    assert (
        is_inside(
            ((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)), (4, 3)
        )
        is False
    ), "Eighth"
    assert is_inside(((0, 0), (0, 2), (2, 2), (2, 0)), (1, 0)) is True

    print("PASSED!!!")
