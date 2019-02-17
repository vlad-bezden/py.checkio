"""
Sort the given iterable so that its elements end up in the decreasing frequency order,
that is, the number of times they appear in elements.
If two elements have the same frequency,
they should end up in the same order as the first appearance in the iterable.

Input: Iterable
Output: Iterable

Precondition: elements can be integers or strings

Performance:
frequency_sort_fast took: 0.182043
frequency_sort_slow took: 2.800217
"""

from typing import List, Any, Iterator, Union
from collections import Counter
from timeit import timeit

InputData = List[Any]
OutputData = Union[InputData, Iterator[Any]]


def frequency_sort_fast(items: InputData) -> OutputData:
    c = Counter(items)
    return sorted(c.elements(), key=lambda k: c[k], reverse=True)


def frequency_sort_slow(items: InputData) -> OutputData:
    return sorted(items, key=lambda k: (-items.count(k), items.index(k)))


if __name__ == "__main__":
    items = [*range(1000, 0, -1)]
    for f in [frequency_sort_fast, frequency_sort_slow]:
        assert list(f([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
        assert list(f([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
        assert list(f(["bob", "bob", "carl", "alex", "bob"])) == [
            "bob",
            "bob",
            "bob",
            "carl",
            "alex",
        ]
        assert list(f([17, 99, 42])) == [17, 99, 42]
        assert list(f([])) == []
        assert list(f([1])) == [1]

        t = timeit(stmt="f(items)", number=100, globals=globals())
        print(f"{f.__name__} took: {t:.6f}")

    print("DONE!")
