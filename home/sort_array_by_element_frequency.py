"""
Sort the given iterable so that its elements end up in the decreasing frequency order,
that is, the number of times they appear in elements.
If two elements have the same frequency,
they should end up in the same order as the first appearance in the iterable.

Input: Iterable
Output: Iterable

Precondition: elements can be integers or strings
"""

from typing import List, Any, Iterator, Union
from collections import Counter

InputData = List[Any]
OutputData = Union[InputData, Iterator[Any]]


def frequency_sort(items: InputData) -> OutputData:
    c = Counter(items)
    result = sorted(c.elements(), key=lambda k: c[k], reverse=True)
    return result


if __name__ == "__main__":
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [
        4,
        4,
        4,
        4,
        2,
        2,
        2,
        6,
        6,
    ]
    assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
        "bob",
        "bob",
        "bob",
        "carl",
        "alex",
    ]
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("DONE!")
