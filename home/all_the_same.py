'''
In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.
'''

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1


if __name__ == '__main__':
    assert all_the_same([1, 1, 1])
    assert not all_the_same([1, 2, 1])
    assert all_the_same(['a', 'a', 'a'])
    assert all_the_same([])
    assert all_the_same([1])
