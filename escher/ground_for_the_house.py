"""Ground for the House.
https://py.checkio.org/en/mission/ground-for-the-house/

As the input data you will get the multiline string consists of '0' & '#'.
where '0' means the empty piece of the ground and the '#' is the piece of your house.
Your task is to count the minimal area of the rectangle ground which is
enough for the building.

Input: The plan of the house.
Output: The total area of the rectangle piece of the ground.

Precondition:
2x2 <= multiline string <= 10x10
"""


def house(plan: str) -> int:
    top_row = top_left = 10
    bottom_row = bottom_right = 0

    if "#" not in plan:
        return 0

    for row_num, row in (
        (i, row.strip()) for i, row in enumerate(plan.split()) if "#" in row
    ):
        top_row = min(top_row, row_num)
        bottom_row = max(bottom_row, row_num)
        top_left = min(top_left, row.index("#"))
        bottom_right = max(bottom_right, row.rindex("#"))

    return (bottom_right - top_left + 1) * (bottom_row - top_row + 1)


if __name__ == "__main__":

    assert (
        house(
            """
            0000000
            ##00##0
            ######0
            ##00##0
            #0000#0
            """
        )
        == 24
    )

    assert (
        house(
            """0000000000
            #000##000#
            ##########
            ##000000##
            0000000000
            """
        )
        == 30
    )

    assert (
        house(
            """0000
            0000
            #000
            """
        )
        == 1
    )

    assert (
        house(
            """0000
            0000
            """
        )
        == 0
    )

    assert (
        house(
            """
            0##0
            0000
            #00#
            """
        )
        == 12
    )

    assert house("\n0000000000\n000###0000\n000#######\n000###0000\n") == 21

    print("DONE!!!")
