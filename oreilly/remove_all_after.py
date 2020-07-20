"""Remove All After.

    https://py.checkio.org/en/mission/remove-all-after/

    Not all of the elements are important.
    What you need to do here is to remove all of the
    elements after the given one from list.

    For illustration, we have an list [1, 2, 3, 4, 5]
    and we need to remove all the elements that go after 3 -
    which is 4 and 5.

    We have two edge cases here:
    (1) if a cutting element cannot be found, then the list shoudn't be changed;
    (2) if the list is empty, then it should remain empty.

    Input: List and the border element.
    Output: Iterable (tuple, list, iterator ...).
"""

from typing import List


def remove_all_after(items: List[int], border: int) -> List[int]:
    return items[:items.index(border) + 1] if border in items else items


if __name__ == "__main__":
    assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
    assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_after([], 0)) == []
    assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]
    print("PASSED!!!")
