"""Max Digit

    https://py.checkio.org/en/mission/max-digit/

    The mission is in Reviewing Mode.
    You can't see the solutions Leader Board, but you can see other
    user solutions through the Random Review after you solve the mission.
    You have a number and you need to determine which digit in this
    number is the biggest.

    Input: A positive int.

    Output: An Int (0-9).

    Example:

    max_digit(0) == 0
    max_digit(52) == 5
    max_digit(634) == 6
    max_digit(1) == 1
    max_digit(10000) == 1
"""


def max_digit(number: int) -> int:
    return int(max(str(number)))


if __name__ == "__main__":
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("PASSED!!!")
