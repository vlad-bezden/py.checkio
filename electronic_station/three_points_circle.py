"""
Three Points Circle

Nicola discovered a calliper inside a set of drafting tools he received as a gift.
Seeing the caliper, he has decided to learn how to use it.

Through any three points that do not exist on the same line, there lies a unique circle.
The points of this circle are represented in a string with the coordinates like so:

    "(x1,y1),(x2,y2),(x3,y3)"

Where x1,y1,x2,y2,x3,y3 are digits.

You should find the circle for three given points,
such that the circle lies through these point and return the result
as a string with the equation of the circle. In a Cartesian coordinate system
(with an X and Y axis), the circle with central coordinates of (x0,y0)
and radius of r can be described with the following equation:

    "(x-x0)^2+(y-y0)^2=r^2"

where x0,y0,r are decimal numbers rounded to two decimal points.
Remove extraneous zeros and all decimal points, they are not necessary.
For rounding, use the standard mathematical rules.

Input: Coordinates as a string..
Output: The equation of the circle as a string.
Precondition: All three given points do not lie on one line.
0 < xi, yi, r < 10
"""

from collections import namedtuple

Points = namedtuple("Points", ["x1", "y1", "x2", "y2", "x3", "y3"])
Coefficients = namedtuple("Coefficients", ["A", "B", "C", "D"])

# def str_to_tuples(data: Text) -> List[Tuple[int, int]]:
#     """Converts string of pair tuples to list of pair tuples"""
#     it = iter("".join(c for c in data if c not in "() ").split(","))
#     return [(int(x), int(y)) for x, y in zip(it, it)]


def str_to_points(data: str) -> Points:
    """Converts string of pair tuples namedtuple"""
    it = "".join(c for c in data if c not in "() ").split(",")
    return Points(*(int(i) for i in it))


def A(p: Points) -> int:
    """A = x1(y2 - y3) - y1(x2 - x3) + x2y3 - x3y2"""
    return p.x1 * (p.y2 - p.y3) - p.y1 * (p.x2 - p.x3) + p.x2 * p.y3 - p.x3 * p.y2


def B(p: Points) -> int:
    """B = (x1^2 + y1^2)(y3 - y2) + (x2^2 + y2^2)(y1 - y3) + (x3^2 + y3^2)(y2 - y1)"""
    return (
        (p.x1 ** 2 + p.y1 ** 2) * (p.y3 - p.y2)
        + (p.x2 ** 2 + p.y2 ** 2) * (p.y1 - p.y3)
        + (p.x3 ** 2 + p.y3 ** 2) * (p.y2 - p.y1)
    )


def C(p: Points) -> int:
    """C = (x1^2 + y1^2)(x2 - x3) + (x2^2 + y2^2)(x3 - x1) + (x3^2 + y3^2)(x1 - x2)"""
    return (
        (p.x1 ** 2 + p.y1 ** 2) * (p.x2 - p.x3)
        + (p.x2 ** 2 + p.y2 ** 2) * (p.x3 - p.x1)
        + (p.x3 ** 2 + p.y3 ** 2) * (p.x1 - p.x2)
    )


def D(p: Points) -> int:
    """D = (x1^2 + y1^2)(x3y2 - x2y3) + (x2^2 + y2^2)(x1y3 - x3y1) + (x3^2 + y3^2)(x2y1 - x1y2)"""
    return (
        (p.x1 ** 2 + p.y1 ** 2) * (p.x3 * p.y2 - p.x2 * p.y3)
        + (p.x2 ** 2 + p.y2 ** 2) * (p.x1 * p.y3 - p.x3 * p.y1)
        + (p.x3 ** 2 + p.y3 ** 2) * (p.x2 * p.y1 - p.x1 * p.y2)
    )


def x(c: Coefficients) -> float:
    """x = -B / (2*A)"""
    return -c.B / (2 * c.A)


def y(c: Coefficients) -> float:
    """y = -C / (2*A)"""
    return -c.C / (2 * c.A)


def r(c: Coefficients) -> float:
    """r = ((B^2 + C^2 - 4AD) / (4A^2))**0.5"""
    return ((c.B ** 2 + c.C ** 2 - 4 * c.A * c.D) / (4 * c.A ** 2)) ** 0.5


data = "(2,2),(6,2),(2,6)"
points = str_to_points(data)
coeff = Coefficients(A(points), B(points), C(points), D(points))
_x = x(coeff)
_y = y(coeff)
_r = r(coeff)

print(_x, _y, _r)

# These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == "__main__":
#     assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
#     assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
