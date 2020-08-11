"""Count Inversions

    https://py.checkio.org/en/mission/count-inversions/

    In computer science and discrete mathematics,
    an inversion is a pair of places in a sequence where the elements
    in these places are out of their natural order.
    So, if we use ascending order for a group of numbers,
    then an inversion is when larger numbers appear before lower number in a sequence.

    Check out this example sequence: (1, 2, 5, 3, 4, 7, 6)
    and we can see here three inversions
    - 5 and 3;
    - 5 and 4;
    - 7 and 6.
    You are given a sequence of unique numbers and you should
    count the number of inversions in this sequence.

    Input: A sequence as a tuple of integers.
    Output: The inversion number as an integer.
    Example:

    count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3
    count_inversion((0, 1, 2, 3)) == 0

    Precondition: 2 < len(sequence) < 200
    len(sequence) == len(set(sequence))
    all(-100 < x < 100 for x in sequence)
"""

from typing import Sequence
from itertools import combinations


def count_inversion(sequence: Sequence[int]) -> int:
    return sum(j < i for i, j in combinations(sequence, 2))


if __name__ == "__main__":
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("PASSED!")
