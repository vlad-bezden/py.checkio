"""Median of Three

    https://py.checkio.org/en/mission/median-of-three/

    Given an iterable of ints, create and return a new iterable
    whose first two elements are the same as in items,
    after which each element equals the median of the three elements
    in the original list ending in that position.

    Input: Iterable of ints.
    Output: Iterable of ints.
"""

from statistics import median
from typing import Iterable


def median_three(items: Iterable[int]) -> Iterable[int]:
    return items[:2] + [*map(median, zip(items, items[1:], items[2:]))]


if __name__ == "__main__":
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    assert list(median_three([])) == []

    print("PASSED!!!")
