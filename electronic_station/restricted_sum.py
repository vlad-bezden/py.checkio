"""Restricted Sum

Our new calculator is censored and as such it does not accept certain words.
You should try to trick by writing a program to calculate the sum of numbers.

Given a list of numbers, you should find the sum of these numbers.
Your solution should not contain any of the banned words,
even as a part of another word.

The list of banned words are as follows:

sum
import
for
while
reduce

Input: A list of numbers.
Output: The sum of numbers.
Precondition: The small amount of data. Let's creativity win!
"""

from typing import List


def checkio(data: List[int]) -> int:
    return 0 if not data else data.pop() + checkio(data)


if __name__ == "__main__":
    assert checkio([1, 2, 3]) == 6
    assert checkio([1, 2, 3, 4, 5, 6]) == 21
    assert checkio([2, 2, 2, 2, 2, 2]) == 12
