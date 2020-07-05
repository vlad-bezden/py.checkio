"""All Upper I
    https://py.checkio.org/en/mission/all-upper/

    Check if a given string has all symbols in upper case.
    If the string is empty or doesn't have any letter in it -
    function should return True.

    Input: A string.
    Output: a boolean.
"""


def is_all_upper(text: str) -> bool:
    return text.upper() == text


if __name__ == "__main__":
    assert is_all_upper("ALL UPPER") is True
    assert is_all_upper("all lower") is False
    assert is_all_upper("mixed UPPER and lower") is False
    assert is_all_upper("") is True
    assert is_all_upper("   ") is True
    assert is_all_upper("123") is True
    print("PASSED!!!")
