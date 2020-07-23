"""Sort Except Zero.

    https://py.checkio.org/en/mission/sort-except-zero/

    Sort the numbers in an array. But the position of
    zeros should not be changed.

    Input: List[int]
    Output: List[int]
"""

from bisect import insort_right
from typing import List


def except_zero(items: List[int]) -> List[int]:
    result = []
    indexes = []
    for i, v in enumerate(items):
        if v == 0:
            indexes.append(i)
        else:
            insort_right(result, v)
    for i in indexes:
        result.insert(i, 0)
    return result


if __name__ == "__main__":
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]

    print("PASSED!!!")
