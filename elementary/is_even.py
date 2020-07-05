"""Is Even

    https://py.checkio.org/en/mission/is-even/

    Check is the given number is even or not.
    Your function should return True if the number is even,
    and False if the number is odd.

    Input: Int.
    Output: Bool.

    Example:

    is_even(2) == True
    is_even(5) == False
    is_even(0) == True


    Precondition: both given ints should be between -1000 and 1000

    Output:
    is_even_mod(2). Exec time = 0.001761
    is_even_bit(2). Exec time = 0.001911

    is_even_mod(5). Exec time = 0.001817
    is_even_bit(5). Exec time = 0.002831

    is_even_mod(0). Exec time = 0.002182
    is_even_bit(0). Exec time = 0.002328

    is_even_mod(1000). Exec time = 0.002081
    is_even_bit(1000). Exec time = 0.002067

    is_even_mod(-1000). Exec time = 0.001842
    is_even_bit(-1000). Exec time = 0.002492

    is_even_mod(999). Exec time = 0.002113
    is_even_bit(999). Exec time = 0.002464

    is_even_mod(-999). Exec time = 0.002032
    is_even_bit(-999). Exec time = 0.002509

    is_even_mod(1000000). Exec time = 0.001947
    is_even_bit(1000000). Exec time = 0.001984

    is_even_mod(1000001). Exec time = 0.002130
    is_even_bit(1000001). Exec time = 0.002245

    Conclusion: bit and mod operators perform almost the same
"""

from timeit import timeit
from dataclasses import dataclass
from typing import Callable, Sequence


@dataclass
class Test:
    data: int
    expected: bool


TESTS = [
    Test(2, True),
    Test(5, False),
    Test(0, True),
    Test(1000, True),
    Test(-1000, True),
    Test(999, False),
    Test(-999, False),
    Test(10 ** 6, True),
    Test(10 ** 6 + 1, False),
]


def is_even_mod(num: int) -> bool:
    """Check if number is even using modulo operator."""
    return num % 2 == 0


def is_even_bit(num: int) -> bool:
    """Check if number is even using and bit operator."""
    return num & 1 == 0


def validate(funcs: Sequence[Callable[[int], bool]]) -> None:
    for test in TESTS:
        for f in funcs:
            result = f(test.data)
            assert result == test.expected, f"{f.__name__}({test}), {result=}"
    print("PASSED!!!")


if __name__ == "__main__":
    funcs = [is_even_mod, is_even_bit]
    validate(funcs)
    for test in TESTS:
        for f in funcs:
            t = timeit(stmt=f"f({test.data})", number=10_000, globals=globals())
            print(f"{f.__name__}({test.data}). Exec time = {t:.6f}")
        print()
