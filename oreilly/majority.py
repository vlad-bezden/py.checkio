"""Majority

    https://py.checkio.org/en/mission/majority/

    We have a List of booleans. Let's check if the majority of elements are true.

    Some cases worth mentioning:
    1) an empty list should return false;
    2) if trues and falses have an equal amount, function should return false.

    Input: A List of booleans.
    Output: A Boolean.

    Example:
    is_majority([True, True, False, True, False]) == True
    is_majority([True, True, False]) == True
"""


from typing import List


def is_majority_1(items: List[bool]) -> bool:
    return len(items) // 2 < sum(items)


def is_majority_2(items: List[bool]) -> bool:
    return items.count(False) < items.count(True)


if __name__ == "__main__":
    assert is_majority_1([True, True, False, True, False]) is True
    assert is_majority_1([True, True, False]) is True
    assert is_majority_1([True, True, False, False]) is False
    assert is_majority_1([True, True, False, False, False]) is False
    assert is_majority_1([False]) is False
    assert is_majority_1([True]) is True
    assert is_majority_1([]) is False

    assert is_majority_2([True, True, False, True, False]) is True
    assert is_majority_2([True, True, False]) is True
    assert is_majority_2([True, True, False, False]) is False
    assert is_majority_2([True, True, False, False, False]) is False
    assert is_majority_2([False]) is False
    assert is_majority_2([True]) is True
    assert is_majority_2([]) is False
    print("PASSED!!!")
