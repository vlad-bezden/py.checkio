"""
You have to return not a substring but a substring length.
You need to find a substring that repeats more than once in a given string.
This reiteration shouldn't have overlaps.
For example, in a string "abcab" the longest substring that repeats more than once is "ab",
so the answer should be 2 (length of "ab")

Input: String.

Output: Int.

Performance:
double_substring_re       0.0159 secs
double_substring_loop     0.0347 secs
double_substring_sm       0.1178 secs
"""

import re
from difflib import SequenceMatcher as sm
from timeit import timeit


def double_substring_sm(line: str) -> int:
    """Length of the longest substring that non-overlapping repeats more than once."""
    counter = 0
    for i, _ in enumerate(line, start=1):
        left, right = line[:i], line[i:]
        match = sm(None, left, right).find_longest_match(0, len(left), 0, len(right))
        counter = max(counter, match.size)
    return counter


def double_substring_re(line: str) -> int:
    return max(map(len, re.findall(r"(?=(.*).*\1)", line)))


def double_substring_loop(line: str) -> int:
    result = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line.count(line[i:j]) > 1:
                result = max(result, j - i)
    return result


if __name__ == "__main__":
    for f in [double_substring_re, double_substring_loop, double_substring_sm]:
        assert f("aaaa") == 2, "First"
        assert f("abc") == 0, "Second"
        assert f("aghtfghkofgh") == 3, "Third"
        t = timeit(stmt="f('aghtfghkofgh')", number=1000, globals=globals())
        print(f"{f.__name__:<25} {t:.4f} secs")
    print("DONE!")
