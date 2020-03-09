"""Pearls in the Box

    https://py.checkio.org/en/mission/box-probability/


    To start the game they put several black and white pearls in
    one of the boxes. Each robot has N moves, after which the
    initial set is being restored for the next game.
    Each turn, the robot takes a pearl out of the box and puts one
    of the opposite color back. The winner is the one who
    takes the white pearl on the Nth move.

    Our robots don't like uncertainty, that's why they want to
    know the probability of drawing a white pearl on the Nth move.
    The probability is a value between 0 (0% chance or will not happen)
    and 1 (100% chance or will happen). The result is a float
    from 0 to 1 with two decimal digits of precision (±0.01).

    You are given a start set of pearls as a string that contains
    "b" (black) and "w" (white) and the number of the move (N).
    The order of the pearls does not matter.

    Input: The start sequence of the pearls as a string and the move number as an integer.

    Output: The probability for a white pearl as a float.

    Example:

    checkio('bbw', 3) == 0.48
    checkio('wwb', 3) == 0.52
    checkio('www', 3) == 0.56
    checkio('bbbb', 1) == 0
    checkio('wwbb', 4) == 0.5
    checkio('bwbwbwb', 5) == 0.48

    Precondition: 0 < N ≤ 20
    0 < |pearls| ≤ 20
"""


def checkio(marbles, step):
    n = len(marbles)

    def move(w, b, step):
        if step == 1:
            return w / n
        p1 = 0 if b == 0 else move(w + 1, b - 1, step - 1)
        p2 = 0 if w == 0 else move(w - 1, b + 1, step - 1)
        return w / n * p2 + b / n * p1

    return round(move(marbles.count("w"), marbles.count("b"), step), 2)


if __name__ == "__main__":
    result = checkio("wbb", 3)
    assert result == 0.48, f"1st {result=}"
    result = checkio("wwb", 3)
    assert result == 0.52, f"2nd {result=}"
    result = checkio("www", 3)
    assert result == 0.56, f"3rd {result=}"
    result = checkio("bbbb", 1)
    assert result == 0, f"4th {result=}"
    result = checkio("wwbb", 4)
    assert result == 0.5, f"5th {result=}"
    result = checkio("bwbwbwb", 5)
    assert result == 0.48, f"6th {result=}"
    result = checkio("w" * 20, 20)
    assert result == 0.57, f"7th {result=}"
    result = checkio("b" * 20, 20)
    assert result == 0.43, f"8th {result=}"
    print("PASSED!")
