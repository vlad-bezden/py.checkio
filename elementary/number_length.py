"""Number Length

    https://py.checkio.org/en/mission/number-length/

    You have a positive integer. Try to find out how many digits it has?

    Input: A positive Int
    Output: An Int.

    Result:
    number_length_str(10). Exec time = 0.003550
    number_length_log10(10). Exec time = 0.003452
    number_length_shift(10). Exec time = 0.005228
    number_length_rec(10). Exec time = 0.005739

    number_length_str(0). Exec time = 0.003442
    number_length_log10(0). Exec time = 0.001380
    number_length_shift(0). Exec time = 0.001987
    number_length_rec(0). Exec time = 0.002572

    number_length_str(4). Exec time = 0.003648
    number_length_log10(4). Exec time = 0.003695
    number_length_shift(4). Exec time = 0.002362
    number_length_rec(4). Exec time = 0.002822

    number_length_str(1234). Exec time = 0.003749
    number_length_log10(1234). Exec time = 0.003650
    number_length_shift(1234). Exec time = 0.009709
    number_length_rec(1234). Exec time = 0.011655

    number_length_str(987654321). Exec time = 0.005798
    number_length_log10(987654321). Exec time = 0.004167
    number_length_shift(987654321). Exec time = 0.021157
    number_length_rec(987654321). Exec time = 0.030328

    Conclusion:
    Using log10 or convert number to str and take length of it are the
    fastest ways to find length of the string. The slowest one is recursion
"""

from timeit import timeit
from collections import namedtuple
from math import log10
from typing import Sequence, Callable

Test = namedtuple("Test", ["data", "expected"])

TESTS = [
    Test(10, 2),
    Test(0, 1),
    Test(4, 1),
    Test(1234, 4),
    Test(987654321, 9),
]


def number_length_str(a: int) -> int:
    """Find number length by converting number to string and taking length of it."""

    return len(str(a))


def number_length_log10(a: int) -> int:
    """Find length of number using math.log10."""

    return int(log10(a or 1) + 1)


def number_length_shift(a: int) -> int:
    """Find length of number using shift operator."""

    base, result = 10, 1
    while base <= a:
        base = (base << 3) + (base << 1)
        result += 1
    return result


def number_length_rec(a: int) -> int:
    """Find length of number using recursion."""

    return 1 + ((b := a // 10) and number_length_rec(b))


def validate(funcs: Sequence[Callable[[int], int]]) -> None:
    for test in TESTS:
        for f in funcs:
            result = f(test.data)
            assert result == test.expected, f"{f.__name__}({test}), {result = }"
    print("PASSED!!!")


if __name__ == "__main__":
    funcs = [
        number_length_str,
        number_length_log10,
        number_length_shift,
        number_length_rec,
    ]
    validate(funcs)
    for test in TESTS:
        for f in funcs:
            t = timeit(stmt=f"f({test.data})", number=10_000, globals=globals())
            print(f"{f.__name__}({test.data}). Exec time = {t:.6f}")
        print()
