"""Create Intervals.

From a set of ints you have to create a list of closed intervals as tuples,
so the intervals are covering all the values found in the set.

A closed interval includes its endpoints! The interval 1..5,
for example, includes each value x that satifies the condition 1 <= x <= 5.

Values can only be in the same interval if the difference between a value
and the next smaller value in the set equals one, otherwise a new interval begins.
Of course, the start value of an interval is excluded from this rule.
A single value, that does not fit into an existing interval
becomes the start - and endpoint of a new interval.

Input: A set of ints.
Output: A list of tuples of two ints, indicating the endpoints of the interval.
The Array should be sorted by start point of each interval
"""

from typing import List, Tuple, Set


def create_intervals_naive(data: Set[int]) -> List[Tuple[int, int]]:
    result = []
    if not data:
        return result
    data = sorted(data)

    start, cur = data[0], data[-1]

    for prev, cur in zip(data, data[1:]):
        if (cur - prev) != 1:
            result.append((start, prev))
            start = cur

    result.append((start, cur))

    return result


def create_intervals(data: Set[int]) -> List[Tuple[int, int]]:
    data = sorted(data)
    left = (l for l in data if l - 1 not in data)
    right = (r for r in data if r + 1 not in data)

    return list(zip(left, right))


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [
        (1, 5),
        (7, 8),
        (12, 12),
    ], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
