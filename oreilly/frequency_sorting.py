"""Frequency Sorting

    https://py.checkio.org/en/mission/frequency-sorting/

    Your mission is to sort the list by the frequency of numbers included in it.
    If a few numbers have an equal frequency -
    they should be sorted according to their natural order.
    For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]

    Input: Chaotic list of numbers.
    Output: The list of numbers in which they are sorted by their frequency.

    Precondition:
    array length <= 100
    max number <= 100

    Results:
    frequency_sorting_1('[1, 2, 3, 4, 5]'). Exec time = 0.035906
    frequency_sorting_2('[1, 2, 3, 4, 5]'). Exec time = 0.084669
    frequency_sorting_3('[1, 2, 3, 4, 5]'). Exec time = 0.068811

    frequency_sorting_1('[3, 4, 11, 13, 11, 4, 4, 7, 3]'). Exec time = 0.075650
    frequency_sorting_2('[3, 4, 11, 13, 11, 4, 4, 7, 3]'). Exec time = 0.148404
    frequency_sorting_3('[3, 4, 11, 13, 11, 4, 4, 7, 3]'). Exec time = 0.151575

    frequency_sorting_1('[99, 99, 55, 55, 21, 21, 10, 10]'). Exec time = 0.083489
    frequency_sorting_2('[99, 99, 55, 55, 21, 21, 10, 10]'). Exec time = 0.158194
    frequency_sorting_3('[99, 99, 55, 55, 21, 21, 10, 10]'). Exec time = 0.160153

    Conclusion:
    Using sort twice is twice faster, because it is
"""

from collections import Counter
from timeit import timeit
from typing import Callable, List
from dataclasses import dataclass

FuncType = List[Callable[[List[int]], List[int]]]


@dataclass
class Test:
    data: List[int]
    expected: List[int]


TESTS = [
    Test([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    Test([3, 4, 11, 13, 11, 4, 4, 7, 3], [4, 4, 4, 3, 3, 11, 11, 7, 13,]),
    Test([99, 99, 55, 55, 21, 21, 10, 10], [10, 10, 21, 21, 55, 55, 99, 99,]),
]


def frequency_sorting_1(numbers: List[int]) -> List[int]:
    """Using sorting twice."""
    return sorted(sorted(numbers), key=numbers.count, reverse=True)


def frequency_sorting_2(numbers: List[int]) -> List[int]:
    """Using Counter."""
    c = Counter(numbers)
    return sorted(numbers, key=lambda x: (-c[x], x))


def frequency_sorting_3(numbers: List[int]) -> List[int]:
    """Using Tuple Sorting."""
    return sorted(numbers, key=lambda x: (-numbers.count(x), x))


def validate(funcs: FuncType) -> None:
    for test in TESTS:
        for f in funcs:
            result = f(test.data)
            assert result == test.expected, f"{f.__name__}({test}), {result = }"
    print("PASSED!!!")


if __name__ == "__main__":
    funcs: FuncType = [
        frequency_sorting_1,
        frequency_sorting_2,
        frequency_sorting_3,
    ]
    validate(funcs)
    for test in TESTS:
        for f in funcs:
            t = timeit(stmt=f"f('{test.data}')", number=10_000, globals=globals())
            print(f"{f.__name__}('{test.data}'). Exec time = {t:.6f}")
        print()
