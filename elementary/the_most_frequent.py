"""
The Most Frequent.

You have a sequence of strings, and you’d like to determine
the most frequently occurring string in the sequence.

Input: a list of strings.
Output: a string.
"""

from typing import List


def most_frequent(data: List[str]) -> str:
    return max(data, key=data.count)


if __name__ == "__main__":
    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
