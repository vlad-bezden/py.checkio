"""Ascending List

    https://py.checkio.org/en/mission/ascending-list/

    Determine whether the sequence of elements items is ascending so that its
    each element is strictly larger than (and not merely equal to) the
    element that precedes it.

    Input: Iterable with ints.
    Output: bool

    Output:
    is_ascending_all([-5, 10, 99, 123456]). Exec time = 0.000124
    is_ascending_set([-5, 10, 99, 123456]). Exec time = 0.000084

    is_ascending_all([99]). Exec time = 0.000082
    is_ascending_set([99]). Exec time = 0.000057

    is_ascending_all([4, 5, 6, 7, 3, 7, 9]). Exec time = 0.000142
    is_ascending_set([4, 5, 6, 7, 3, 7, 9]). Exec time = 0.000081

    is_ascending_all([]). Exec time = 0.000090
    is_ascending_set([]). Exec time = 0.000047

    is_ascending_all([1, 1, 1, 1]). Exec time = 0.000103
    is_ascending_set([1, 1, 1, 1]). Exec time = 0.000061

    Conclusion: using set works faster than iterating using zip
"""

from typing import Callable, Sequence
from timeit import repeat
from dataclasses import dataclass


@dataclass
class Test:
    data: Sequence[int]
    expected: bool


TESTS = [
    Test([-5, 10, 99, 123456], True),
    Test([99], True),
    Test([4, 5, 6, 7, 3, 7, 9], False),
    Test([], True),
    Test([1, 1, 1, 1], False),
]


def is_ascending_set(items: Sequence[int]) -> bool:
    return sorted(set(items)) == items


def is_ascending_zip(items: Sequence[int]) -> bool:
    return all(x < y for x, y in zip(items, items[1:]))


def validate(funcs: Sequence[Callable[[Sequence[int]], bool]]) -> None:
    for test in TESTS:
        for f in funcs:
            result = f(test.data)
            assert result == test.expected, f"{f.__name__}({test}), {result = }"
    print("PASSED!!!\n")


if __name__ == "__main__":
    funcs = [is_ascending_zip, is_ascending_set]
    validate(funcs)
    for test in TESTS:
        for f in funcs:
            t = repeat(stmt=f"f({test.data})", repeat=5, number=100, globals=globals())
            print(f"{f.__name__}({test.data}). Exec time = {min(t):.6f}")
        print()
