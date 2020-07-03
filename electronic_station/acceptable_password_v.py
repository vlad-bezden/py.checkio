"""Acceptable Password V

    https://py.checkio.org/en/mission/acceptable-password-v/

    In this mission you need to create a password verification function.

    Those are the verification conditions:

    The length should be bigger than 6;
    Should contain at least one digit, but it cannot consist of just digits;
    Having numbers or containing just numbers does not apply
    to the password longer than 9.
    A string should not contain the word "password" in any case.

    Input: A string.
    Output: A bool.
"""

import re

MIN_PASSWORD_LENGTH = 6
NO_RULES = 9


def is_acceptable_password(password: str) -> bool:
    return (
        False
        if "PASSWORD" in password.upper()
        else (
            True
            if (NO_RULES < (n := len(password)))
            else 0 < len(re.findall("\d", password)) < n > MIN_PASSWORD_LENGTH
        )
    )


if __name__ == "__main__":
    assert is_acceptable_password("short") is False
    assert is_acceptable_password("short54") is True
    assert is_acceptable_password("muchlonger") is True
    assert is_acceptable_password("ashort") is False
    assert is_acceptable_password("muchlonger5") is True
    assert is_acceptable_password("sh5") is False
    assert is_acceptable_password("1234567") is False
    assert is_acceptable_password("12345678910") is True
    assert is_acceptable_password("password12345") is False
    assert is_acceptable_password("PASSWORD12345") is False
    assert is_acceptable_password("pass1234word") is True
    print("PASSED!!!")
