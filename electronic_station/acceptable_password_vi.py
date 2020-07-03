"""Acceptable Password VI

    https://py.checkio.org/en/mission/acceptable-password-vi/

    In this mission you need to create a password verification function.

    Those are the verification conditions:

    The length should be bigger than 6.
    Should contain at least one digit, but it cannot consist of just digits.
    Having numbers or containing just numbers does not apply
    to the password longer than 9.
    A string should not contain the word "password" in any case.
    Should contain 3 different letters (or digits) even if it is longer than 10.

    Input: A string.
    Output: A bool.
"""


import re

MIN_PASSWORD_LENGTH = 6
NO_RULES = 9
MIN_UNIQUE_CHARS = 3
RULES = [
    lambda s: MIN_PASSWORD_LENGTH < len(s),
    lambda s: "PASSWORD" not in s.upper(),
    lambda s: True
    if (NO_RULES < (n := len(s)))
    else 0 < len(re.findall("\d", s)) < n > MIN_PASSWORD_LENGTH,
    lambda s: MIN_UNIQUE_CHARS <= len(set(s)),
]


is_acceptable_password = lambda password: all(rule(password) for rule in RULES)


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
    assert is_acceptable_password("aaaaaa1") is False
    assert is_acceptable_password("aaaaaabbbbb") is False
    assert is_acceptable_password("aaaaaabb1") is True
    print("PASSED!!!")
