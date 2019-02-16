"""
Positive integers can be expressed as sums of consecutive positive
integers in various ways.
For example, 42 can be expressed as such a sum in four different ways:
(a) 3+4+5+6+7+8+9,
(b) 9+10+11+12,
(c) 13+14+15 and
(d) 42.
As the last solution (d) shows, any positive integer can always be trivially
expressed as a singleton sum that consists of that integer alone.

Compute how many different ways it can be expressed as a sum of consecutive
positive integers.

Input: Int.

Output: Int.

Precondition: Input is always a positive integer.

Performance:
count_consecutive_summers_slow took: 0.114300
count_consecutive_summers_fast took: 0.006804
"""

from itertools import count
from timeit import timeit


def count_consecutive_summers_fast(num: int) -> int:
    counter = 0
    for i in count(1):
        # find middle + half spread = end
        end = (num // i) + (i // 2 + 1)
        start = end - i
        if start <= 0:
            break
        if sum(range(start, end)) == num:
            counter += 1

    return counter


def count_consecutive_summers_slow(num: int) -> int:
    return sum(not num % i for i in range(1, num + 1, 2))


if __name__ == "__main__":
    for f in [count_consecutive_summers_slow, count_consecutive_summers_fast]:
        assert f(42) == 4
        assert f(99) == 6
        assert f(105) == 8
        assert f(1) == 1
        assert f(2) == 1

        num = 10000
        t = timeit(stmt=f"f({num})", number=100, globals=globals())
        print(f"{f.__name__} took: {t:.6f}")

    print("DONE")
