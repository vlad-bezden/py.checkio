"""Acceptable Password I

    https://py.checkio.org/en/mission/acceptable-password-i/

    You are the beginning of a password series. Every mission will
    be based on the previous one. Going forward the missions will
    become slightly more complex.

    In this mission you need to create a password verification function.

    Those are the verification conditions:
    the length should be bigger than 6.

    Input: A string.

    Output: A bool.
"""

MIN_PASSWORD_LENGTH = 6

is_acceptable_password = lambda p: MIN_PASSWORD_LENGTH < len(p)


if __name__ == "__main__":
    assert is_acceptable_password("short") is False
    assert is_acceptable_password("muchlonger") is True
    assert is_acceptable_password("ashort") is False
    print("PASSED")
