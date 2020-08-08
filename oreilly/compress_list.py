"""Compress List.

    https://py.checkio.org/en/mission/compress-list/

    A given list should be "compressed" in a way so, instead of two
    (or more) equal elements, staying one after another, there is
    only one in the result Iterable (list, tuple, iterator ...).

    Input: List.
    Output: "Compressed" Iterable (list, tuple, iterator ...).

    Conclusion:
    groupby is twice faster than using zip or iterate over items:

    compress_groupby([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0]). Exec time = 0.000162
    compress_comprehension([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0]). Exec time = 0.000246
    compress_zip([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0]). Exec time = 0.000208

    compress_groupby([1, 1, 1, 1, 2, 2, 2, 1, 1, 1]). Exec time = 0.000125
    compress_comprehension([1, 1, 1, 1, 2, 2, 2, 1, 1, 1]). Exec time = 0.000202
    compress_zip([1, 1, 1, 1, 2, 2, 2, 1, 1, 1]). Exec time = 0.000176

    compress_groupby([7, 7]). Exec time = 0.000087
    compress_comprehension([7, 7]). Exec time = 0.000113
    compress_zip([7, 7]). Exec time = 0.000132

    compress_groupby([]). Exec time = 0.000048
    compress_comprehension([]). Exec time = 0.000083
    compress_zip([]). Exec time = 0.000080

    compress_groupby([1, 2, 3, 4]). Exec time = 0.000103
    compress_comprehension([1, 2, 3, 4]). Exec time = 0.000143
    compress_zip([1, 2, 3, 4]). Exec time = 0.000155

    compress_groupby([9, 9, 9, 9, 9, 9, 9]). Exec time = 0.000129
    compress_comprehension([9, 9, 9, 9, 9, 9, 9]). Exec time = 0.000157
    compress_zip([9, 9, 9, 9, 9, 9, 9]). Exec time = 0.000143
"""

from dataclasses import dataclass
from itertools import groupby
from typing import Callable, List, Sequence
from timeit import repeat


@dataclass
class Test:
    data: List[int]
    expected: List[int]


TESTS = [
    Test([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0], [5, 4, 5, 6, 5, 7, 8, 0,]),
    Test([1, 1, 1, 1, 2, 2, 2, 1, 1, 1], [1, 2, 1]),
    Test([7, 7], [7]),
    Test([], []),
    Test([1, 2, 3, 4], [1, 2, 3, 4]),
    Test([9, 9, 9, 9, 9, 9, 9], [9]),
]


def compress_groupby(items: List[int]) -> List[int]:
    return [key for key, _ in groupby(items)]


def compress_comprehension(items: List[int]) -> List[int]:
    return items[:1] + [x for i, x in enumerate(items[1:]) if items[i] != x]


def compress_zip(items: List[int]) -> List[int]:
    return items[:1] + [x1 for x1, x2 in zip(items[1:], items) if x1 != x2]


def validate(funcs: Sequence[Callable[[List[int]], List[int]]]) -> None:
    for test in TESTS:
        for f in funcs:
            result = f(test.data)
            assert result == test.expected, f"{f.__name__}({test}), {result = }"
    print("PASSED!!!")


if __name__ == "__main__":
    funcs = [compress_groupby, compress_comprehension, compress_zip]
    validate(funcs)
    for test in TESTS:
        for f in funcs:
            t = repeat(stmt=f"f({test.data})", repeat=3, number=100, globals=globals())
            print(f"{f.__name__}({test.data}). Exec time = {min(t):.6f}")
        print()
