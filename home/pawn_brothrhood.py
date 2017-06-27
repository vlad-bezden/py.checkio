"""Pawn Brotherhood

A pawn is generally a weak unit, but we have 8 of them which we can use to
build a pawn defense wall. With this strategy, one pawn defends the others.
A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns.
You should design your code to find how many pawns are safe.
You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.
Output: The number of safe pawns as a integer.

Precondition:
0 < pawns ≤ 8
"""


def protecting_cells(cell) -> set:
    row = str(int(cell[1]) - 1)
    col = ord(cell[0])

    return {chr(col - 1) + row,
            chr(col + 1) + row}


def safe_pawns(pawns):
    counter = 0

    for p in pawns:
        cells = protecting_cells(p)
        if cells & pawns:
            counter += 1
    return counter


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
