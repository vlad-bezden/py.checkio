"""Replace First.

    https://py.checkio.org/en/mission/replace-first/

    In a given list the first element should become the last one.
    An empty list or list with only one element should stay the same.

    Input: List
    Output: Iterable
"""

from typing import List


def replace_first(items: List[int]) -> List[int]:
    return items[1:] + items[:1]


if __name__ == "__main__":
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("PASSED!!!")
