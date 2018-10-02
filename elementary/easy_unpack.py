"""
Easy Unpack.

Your mission here is to create a function that gets an tuple
and returns a tuple with 3 elements -
first, third and second to the last for the given array

Input: a list of strings.
Output: a string.
"""

from operator import itemgetter
from typing import Tuple


def easy_unpack(elements: Tuple[int]) -> Tuple[int]:
    """
    Returns a tuple with 3 elements - first, third and second to the last
    """

    return itemgetter(0, 2, -2)(elements)


if __name__ == "__main__":
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
