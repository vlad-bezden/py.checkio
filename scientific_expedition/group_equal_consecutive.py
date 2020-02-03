"""Group Equal consecutive.

Given a list of elements, create and return a list whose elements are lists that
contain the consecutive runs of equal elements of the original list.
Note that elements that aren’t duplicated in the original list should become
singleton lists in the result, so that every element gets included in the
resulting list of lists.

Input: List of str and int.

Output: List of lists of str and int

Example:

group_equal([1, 1, 4, 4, 4, "hello", "hello", 4])
    == [[1,1],[4,4,4],["hello","hello"],[4]]
group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
group_equal([1]) == [[1]]
group_equal([]) == []
"""

from itertools import groupby
from typing import List, Union

DataType = List[Union[str, int]]


def group_equal(items: DataType) -> List[DataType]:
    return [[*g] for _, g in groupby(items)]


if __name__ == "__main__":
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [
        [1, 1],
        [4, 4, 4],
        ["hello", "hello"],
        [4],
    ]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("PASSED!!!")
