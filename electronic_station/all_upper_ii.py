"""All Upper II

    https://py.checkio.org/en/mission/all-upper-ii/

    Check if a given string has all symbols in upper case.
    If the string is empty or doesn't have any letter in it -
    function should return False.

    Input: A string.
    Output: a boolean.
"""

is_all_upper = lambda s: s.isupper()


if __name__ == "__main__":
    assert is_all_upper("ALL UPPER") is True
    assert is_all_upper("all lower") is False
    assert is_all_upper("mixed UPPER and lower") is False
    assert is_all_upper("") is False
    assert is_all_upper("     ") is False
    assert is_all_upper("DIGITS123") is True
    assert is_all_upper("123") is False
    print("PASSED!!!")
