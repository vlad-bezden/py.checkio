"""
Flatten a List

Nicola likes to categorize all sorts of things. He categorized a series of numbers and
as the result of his efforts, a simple sequence of numbers became a deeply-nested list.
Sophia and Stephan don't really understand his organization and need to figure out
what it all means. They need your help to understand Nikolas crazy list.

There is a list which contains integers or other nested lists which may contain yet
more lists and integers which then… you get the idea
You should put all of the integer values into one flat list. The order should be as it
was in the original list with string representation from left to right.

We need to hide this program from Nikolas by keeping it small and easy to hide.
Because of this, your code should be shorter than 140 characters (with whitespaces).

Input data: A nested list with integers.

Output data: The one-dimensional list with integers.

Example:

flat_list([1, 2, 3]) == [1, 2, 3]
flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
Precondition: 0 ≤ |array| ≤ 100
∀ x ∈ array : -232 < x < 232 or x is a list
depth < 10

Performance results:
f_c took: 0.522254
f_r took: 0.546113
f_m took: 0.317996
"""

import itertools as it
import functools as ft
from timeit import timeit


def f_c(d):
    """using chain."""
    return [d] if type(d) == int else [*(it.chain(*[f_c(l) for l in d]))]


def f_r(d):
    """using reduce."""
    return [d] if type(d) == int else ft.reduce(lambda p, c: p + f_r(c), d, [])


def f_m(d):
    """using map."""
    return [d] if type(d) == int else sum(map(f_m, d), [])


if __name__ == "__main__":
    for f in [f_c, f_r, f_m]:
        assert f([1, 2, 3]) == [1, 2, 3], "First"
        assert f([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
        assert f([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [
            2,
            4,
            5,
            6,
            6,
            6,
            6,
            6,
            7,
        ], "Third"
        assert f([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
        t = timeit(
            stmt="f([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])",
            number=10000,
            globals=globals(),
        )

        print(f"{f.__name__} took: {t:.6f}")
    print("Done!")
