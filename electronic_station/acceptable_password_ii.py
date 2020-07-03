"""Acceptable Password II

    https://py.checkio.org/en/mission/acceptable-password-ii/

    In this mission you need to create a password verification function.

    Those are the verification conditions:
    the length should be bigger than 6;
    should contain at least one digit.

    Input: A string.
    Output: A bool.
"""

MIN_PASSWORD_LENGTH = 6


def is_acceptable_password(password: str) -> bool:
    return MIN_PASSWORD_LENGTH < len(password) and any(c.isdigit() for c in password)


if __name__ == "__main__":
    assert is_acceptable_password("short") is False
    assert is_acceptable_password("muchlonger") is False
    assert is_acceptable_password("ashort") is False
    assert is_acceptable_password("muchlonger5") is True
    assert is_acceptable_password("sh5") is False
    print("PASSED!!!")
