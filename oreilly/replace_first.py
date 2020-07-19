"""Replace Last.

    https://py.checkio.org/en/mission/replace-last/

    In a given list the last element should become the first one.
    An empty list or list with only one element should stay the same

    Input: List.
    Output: List.
"""

from collections import deque

from typing import List


def replace_last_slices(items: List[int]) -> List[int]:
    """Using slices."""
    return items[-1:] + items[:-1]


def replace_last_list(items: List[int]) -> List[int]:
    """Using list pop and insert list features."""
    if items:
        items.insert(0, items.pop())
    return items


def replace_last_deque(items: List[int]) -> List[int]:
    """Using collections.deque.rotate method."""
    q = deque(items)
    q.rotate(1)
    return list(q)


if __name__ == "__main__":
    assert list(replace_last_slices([2, 3, 4, 1])) == [1, 2, 3, 4]
    assert list(replace_last_slices([1])) == [1]
    assert list(replace_last_slices([])) == []

    assert list(replace_last_list([2, 3, 4, 1])) == [1, 2, 3, 4]
    assert list(replace_last_list([1])) == [1]
    assert list(replace_last_list([])) == []

    assert list(replace_last_deque([2, 3, 4, 1])) == [1, 2, 3, 4]
    assert list(replace_last_deque([1])) == [1]
    assert list(replace_last_deque([])) == []

    print("PASSED!!!")
