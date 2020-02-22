"""Parity Bit Generator
    https://py.checkio.org/en/mission/parity-bit-generator/

    R2HI 2.0 interface specification:
    1. Data packages (message) are represented as a list of int numbers
    (0 ≤ number ≤ 255):
    [d1, d2, d3, ..., dn], where d1 is the first letter in message
    2. Each decimal number is an ASCII-code of respective characters
    in binary + parity bit
    Example:
        Chr | Dec  |   Bin   |P|  Bin + P | Dec
        ---------------------------------------
        'P' |  80  | 1010000 |0| 10100000 | 160
        'y' | 121  | 1111001 |1| 11110011 | 243
        't' | 116  | 1110100 |0| 11101000 | 232
        'h' | 104  | 1101000 |1| 11010001 | 209
        'o' | 111  | 1101111 |0| 11011110 | 222
        'n' | 110  | 1101110 |1| 11011101 | 221

            Message = [160, 243, 232, 209, 222, 221]

    You have to implement an "R2HI 2.0 translator/analyzer" that translates a received
    data package (list of int) into a string message. Before the translation,
    erroneous numbers must be removed from the package (list).
    Erroneous means the decimal value contains a wrong (odd) number of '1' in a
    binary form:

    'P' → 80 → 1010000 + 0 → 10100000 → ...10110000... → 10110000
    (Erroneous, 4-th bit was inverted)
    Notice: During the data transmission one bit can be wrong (substituted) at most.

    How it Works:
    Input message: [144, 16, 210, 214]
    Remove erroneous characters (binary): [10010000, 00010000, 11010010, 11010110]
    Binary result (remove parity bit): [10010000, 11010010]
    Decimal: [72, 105]
    Message string (ASCII): "Hi"

    Input: A list of int numbers

    Output: Message as a string

    Precondition: 1 ≤ len(message) < 100
    all(m for m in message if i.isprintable())
    0 ≤ number ≤ 255
"""

checkio = lambda message: "".join(
    chr(int(i[:-1], 2))
    for i in (bin(i) for i in message)
    if i[:-1].count("1") % 2 == int(i[-1])
)


if __name__ == "__main__":
    assert (
        checkio(
            [
                135,
                134,
                124,
                233,
                209,
                81,
                42,
                202,
                198,
                194,
                229,
                215,
                230,
                146,
                28,
                210,
                145,
                137,
                222,
                158,
                49,
                81,
                214,
                157,
            ]
        )
        == "Checkio"
    )
    assert (
        checkio(
            [
                144,
                100,
                200,
                202,
                216,
                152,
                164,
                88,
                216,
                222,
                65,
                218,
                175,
                217,
                248,
                222,
                171,
                228,
                216,
                205,
                254,
                201,
                193,
                220,
            ]
        )
        == "Hello World"
    )

    print("PASSED!!!")
