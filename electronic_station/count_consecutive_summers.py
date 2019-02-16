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
"""

import math


def count_consecutive_summers(num: int) -> int:
    # TODO:
    if num <= 2:
        return 1
    counter = []
    for i in range(1, math.ceil(math.sqrt(num)) + 2):
        middle = int(math.floor(num / i))
        end = middle + i // 2 + 1
        start = end - i
        if sum(range(start, end)) == num:
            counter.append((i, start, end))

    return len(counter)


if __name__ == "__main__":
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("DONE")
