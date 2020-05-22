"""Sum by Type
    Solution for check.io mission https://py.checkio.org/en/mission/sum-by-type/

    You have a list. Each value from that list can be either a string or an integer.
    Your task here is to return two values. The first one is a concatenation
    of all strings from the given list.
    The second one is a sum of all integers from the given list.

    Input: An array of strings ans integers

    Output: A list or tuple

    Example:

    sum_by_types([]) == ['', 0]
    sum_by_types([1, 2, 3]) == ['', 6]
    sum_by_types(['1', 2, 3]) == ['1', 5]
    sum_by_types(['1', '2', 3]) == ['12', 3]
    sum_by_types(['1', '2', '3']) == ['123', 0]
    sum_by_types(['size', 12, 'in', 45, 0]) == ['sizein', 57]
"""

from typing import Tuple, List, Any


def sum_by_types(items: List[Any]) -> Tuple[str, int]:
    result = zip(*[[("", x), (x, 0)][isinstance(x, str)] for x in items], ["", 0])
    return ("".join(next(result)), sum(next(result)))


if __name__ == "__main__":
    assert sum_by_types([]) == ("", 0)
    assert sum_by_types([1, 2, 3]) == ("", 6)
    assert sum_by_types(["1", 2, 3]) == ("1", 5)
    assert sum_by_types(["1", "2", 3]) == ("12", 3)
    assert sum_by_types(["1", "2", "3"]) == ("123", 0)
    assert sum_by_types(["size", 12, "in", 45, 0]) == ("sizein", 57)
    print("PASSED!!!")
