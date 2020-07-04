"""End Zeros.

    https://py.checkio.org/en/mission/end-zeros/

    Try to find out how many zeros a given number has at the end.

    Input: A positive Int
    Output: An Int.

    Output:
    end_zeros_rstrip(0). Exec time = 0.005447
    end_zeros_findall(0). Exec time = 0.021252

    end_zeros_rstrip(1). Exec time = 0.005604
    end_zeros_findall(1). Exec time = 0.020506

    end_zeros_rstrip(10). Exec time = 0.005583
    end_zeros_findall(10). Exec time = 0.021389

    end_zeros_rstrip(101). Exec time = 0.005537
    end_zeros_findall(101). Exec time = 0.020509

    end_zeros_rstrip(245). Exec time = 0.005546
    end_zeros_findall(245). Exec time = 0.020894

    end_zeros_rstrip(100100). Exec time = 0.006040
    end_zeros_findall(100100). Exec time = 0.023233
"""

from timeit import timeit
from re import findall
from collections import namedtuple
from typing import Sequence, Callable

Test = namedtuple("Test", ["data", "expected"])

TESTS = [
    Test(0, 1),
    Test(1, 0),
    Test(10, 1),
    Test(101, 0),
    Test(245, 0),
    Test(100100, 2),
]


def end_zeros_rstrip(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip("0"))


def end_zeros_findall(num: int) -> int:
    return len(findall("0*$", str(num))[0])


def validate(funcs: Sequence[Callable[[int], int]]) -> None:
    for test in TESTS:
        for f in funcs:
            result = f(test.data)
            assert result == test.expected, f"{f.__name__}({test}), {result = }"
    print("PASSED!!!")


if __name__ == "__main__":
    funcs = [
        end_zeros_rstrip,
        end_zeros_findall,
    ]
    validate(funcs)
    for test in TESTS:
        for f in funcs:
            t = timeit(stmt=f"f({test.data})", number=10_000, globals=globals())
            print(f"{f.__name__}({test.data}). Exec time = {t:.6f}")
        print()
