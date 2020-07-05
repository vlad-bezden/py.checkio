"""Backward String

    https://py.checkio.org/en/mission/backward-string/

    You should return a given string in reverse order.

    Input: A string.
    Output: A string.
"""


def backward_string(val: str) -> str:
    return val[::-1]


if __name__ == "__main__":
    assert backward_string("val") == "lav"
    assert backward_string("") == ""
    assert backward_string("ohho") == "ohho"
    assert backward_string("123456789") == "987654321"
    print("PASSED!!!")