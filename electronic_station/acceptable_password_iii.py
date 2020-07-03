"""Acceptable Password III

    https://py.checkio.org/en/mission/acceptable-password-iii/

    In this mission you need to create a password verification function.

    Those are the verification conditions:
    the length should be bigger than 6;
    should contain at least one digit, but cannot consist of just digits.

    Input: A string.
    Output: A bool.
"""

import re


MIN_PASSWORD_LENGTH = 6


def is_acceptable_password(password: str) -> bool:
    return 0 < len(re.findall("\d", password)) < len(password) > MIN_PASSWORD_LENGTH


if __name__ == "__main__":
    assert is_acceptable_password("short") is False
    assert is_acceptable_password("muchlonger") is False
    assert is_acceptable_password("ashort") is False
    assert is_acceptable_password("muchlonger5") is True
    assert is_acceptable_password("sh5") is False
    assert is_acceptable_password("1234567") is False

    print("PASSED!!!")
