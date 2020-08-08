"""Median of Three

    https://py.checkio.org/en/mission/median-of-three/

    Given an List of ints, create and return a new List
    whose first two elements are the same as in items,
    after which each element equals the median of the three elements
    in the original list ending in that position.

    Input: List of ints.
    Output: List of ints.

    Output:
    median_three_sorted([1, 2, 3, 4, 5, 6, 7]) => 0.000359
    median_three_zip([1, 2, 3, 4, 5, 6, 7]) => 0.000379

    median_three_sorted([1]) => 0.000080
    median_three_zip([1]) => 0.000119

    median_three_sorted([]) => 0.000060
    median_three_zip([]) => 0.000105

    Conclusion:
    Using sorted works faster when there are less items in the list. With more items
    both sorted and zip have almost the same time.
"""

from statistics import median
from typing import Callable, List, Sequence
from dataclasses import dataclass
from timeit import repeat


@dataclass
class Test:
    data: List[int]
    expected: List[int]


TESTS = [
    Test([1, 2, 3, 4, 5, 6, 7], [1, 2, 2, 3, 4, 5, 6]),
    Test([1], [1]),
    Test([], []),
]


def median_three_sorted(items: List[int]) -> List[int]:
    return [
        v if i < 2 else sorted(items[i - 2 : i + 1])[1]
        for i, v in enumerate(items)
    ]


def median_three_zip(items: List[int]) -> List[int]:
    return items[:2] + [*map(median, zip(items, items[1:], items[2:]))]


def validate(funcs: Sequence[Callable[[List[int]], List[int]]]) -> None:
    for test in TESTS:
        for f in funcs:
            result = f(test.data)
            assert result == test.expected, f"{f.__name__}({test}), {result = }"
    print("PASSED!!!")


if __name__ == "__main__":
    funcs = [median_three_sorted, median_three_zip]
    validate(funcs)
    for test in TESTS:
        for f in funcs:
            t = repeat(stmt=f"f({test.data})", repeat=3, number=100, globals=globals())
            print(f"{f.__name__}({test.data}) => {min(t):.6f}")
        print()
