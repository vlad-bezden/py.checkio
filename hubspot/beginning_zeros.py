"""Beginning Zeros

    https://py.checkio.org/en/mission/beginning-zeros/

    You have a string that consist only of digits.
    You need to find how many zero digits ("0") are
    at the beginning of the given string.

    Input: A string, that consist of digits.
    Output: An Int.
    Precondition: 0-9
"""

import re


def beginning_zeros(number: str) -> int:
    m = re.match(r"0+", number)
    return len(m.group(0)) if m else 0


if __name__ == "__main__":
    assert beginning_zeros("100") == 0
    assert beginning_zeros("001") == 2
    assert beginning_zeros("100100") == 0
    assert beginning_zeros("001001") == 2
    assert beginning_zeros("012345679") == 1
    assert beginning_zeros("0000") == 4
    print("PASSED!!!")
