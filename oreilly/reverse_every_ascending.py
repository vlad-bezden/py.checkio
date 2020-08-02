"""Reverse Every Ascending

    https://py.checkio.org/en/mission/reverse-every-ascending/

    Create and return a new iterable that contains the same elements
    as the argument iterable items, but with the reversed order of
    the elements inside every maximal strictly ascending sublist.
    This function should not modify the contents of the original iterable.

    Input: Iterable
    Output: Iterable
    Precondition: Iterable contains only ints
"""

from typing import List


def reverse_ascending(items: List[int]) -> List[int]:
    result = []
    cursor = 0
    for i in range(1, len(items)):
        if items[i] <= items[i - 1]:
            result.extend(reversed(items[cursor:i]))
            cursor = i
    result = result + [*reversed(items[cursor:])]
    return result


if __name__ == "__main__":
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
        10,
        7,
        5,
        4,
        8,
        7,
        2,
        3,
        1,
    ]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]

    print("PASSED!!!")
