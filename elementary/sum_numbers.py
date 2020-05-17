"""Sum Numbers
    https://py.checkio.org/en/mission/sum-numbers/

    In a given text you need to sum the numbers.
    Only separated numbers should be counted.
    If a number is part of a word it shouldn't be counted.

    The text consists from numbers, spaces and english letters
    Input: A string.
    Output: An int.

    Example:

    sum_numbers('hi') == 0
    sum_numbers('who is 1st here') == 0
    sum_numbers('my numbers is 2') == 2
    sum_numbers('This picture is an oil on canvas painting by Danish artist Anna '
        'Petersen between 1845 and 1910 year') == 3755
    sum_numbers('5 plus 6 is') == 11
    sum_numbers('') == 0

    Summary:
        Using split twice faster than re
"""

import re


def sum_numbers_re(text: str) -> int:
    return sum(int(x) for x in re.findall(r"\b\d+\b", text))


def sum_numbers_split(text: str) -> int:
    return sum(int(word) for word in text.split() if word.isdigit())


if __name__ == "__main__":
    for f in [sum_numbers_re, sum_numbers_split]:
        assert f("hi") == 0
        assert f("who is 1st here") == 0
        assert f("my numbers is 2") == 2
        assert (
            f(
                "This picture is an oil on canvas "
                "painting by Danish artist Anna "
                "Petersen between 1845 and 1910 year"
            )
            == 3755
        )
        assert f("5 plus 6 is") == 11
        assert f("") == 0

    print("PASSED!!!")
