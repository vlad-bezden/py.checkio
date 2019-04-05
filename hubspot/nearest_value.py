"""
Find the nearest value to the given one.

You are given a list of values as set form and a value for which you need
to find the nearest one.

For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17,
and we need to find the nearest value to the number 9.
If we sort this set in the ascending order, then to the left of number 9
will be number 7 and to the right - will be number 10. But 10 is closer than 7,
which means that the correct answer is 10.

A few clarifications:

If 2 numbers are at the same distance, you need to choose the smallest one;
The set of numbers is always non-empty, i.e. the size is >=1;
The given value can be in this set, which means that it’s the answer;
The set can contain both positive and negative numbers, but they are always integers;
The set isn’t sorted and consists of unique numbers.
Input: Two arguments. A list of values in the set form. The sought value is an int.

Output: Int.

Performance:
    nearest_value_1     0.2098 secs
    nearest_value_2     0.1767 secs
    nearest_value_3     0.1796 secs
"""

from timeit import timeit
from typing import Set


def nearest_value_1(values: Set[int], one: int) -> int:
    """Using pure min generator comprehension."""
    return min((abs(i - one), i) for i in values)[1]


def nearest_value_2(values: Set[int], one: int) -> int:
    """Using pure min function."""
    return min(values, key=lambda i: abs(i - one))


def nearest_value_3(values: Set[int], one: int) -> int:
    """Using sort."""
    return sorted(values, key=lambda i: abs(i - one))[0]


if __name__ == "__main__":
    for f in (nearest_value_1, nearest_value_2, nearest_value_3):
        assert f({4, 7, 10, 11, 12, 17}, 9) == 10
        assert f({4, 7, 10, 11, 12, 17}, 8) == 7
        assert f({4, 8, 10, 11, 12, 17}, 9) == 8
        assert f({4, 9, 10, 11, 12, 17}, 9) == 9
        assert f({4, 7, 10, 11, 12, 17}, 0) == 4
        assert f({4, 7, 10, 11, 12, 17}, 100) == 17
        assert f({5, 10, 8, 12, 89, 100}, 7) == 8
        assert f({-1, 2, 3}, 0) == -1
        t = timeit(
            stmt="f({4, 7, 10, 11, 12, 17}, 100)", number=10000, globals=globals()
        )
        print(f"{f.__name__:<20}{t:.4f} secs")
