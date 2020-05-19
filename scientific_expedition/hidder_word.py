"""The Hidden Word mission from check.io

    https://py.checkio.org/en/mission/hidden-word/

    Nicola has solved this puzzle (and I am sure that you will do equally well).
    To be prepared for more such puzzles, Nicola wants to invent a method
    to search for words inside poetry. You can help him create a function
    to search for certain words.

    You are given a rhyme (a multiline string), in which lines
    are separated by "newline" (\n). Casing does not matter for your search,
    but whitespaces should be removed before your search.
    You should find the word inside the rhyme in the horizontal
    (from left to right) or vertical (from up to down) lines.
    For this you need envision the rhyme as a matrix (2D array).
    Find the coordinates of the word in the cut rhyme (without whitespaces).

    The result must be represented as a list --
    [row_start,column_start,row_end,column_end], where
    row_start is the line number for the first letter of the word.
    column_start is the column number for the first letter of the word.
    row_end is the line number for the last letter of the word.
    column_end is the column number for the last letter of the word.
    Counting of the rows and columns start from 1.

    Input: Two arguments. A rhyme as a string and a word as a string (lowercase).
    Output: The coordinates of the word.

    Precondition: The word is given in lowercase
    0 < |word| < 10
    0 < |rhyme| < 300
"""

from itertools import zip_longest
from difflib import SequenceMatcher
from typing import List, Optional, Union


def find_match(matrix: List[str], word: str) -> Optional[List[int]]:
    for idx, line in enumerate(matrix, start=1):
        sm = SequenceMatcher(None, word, line)
        if (m := sm.find_longest_match(0, len(word), 0, len(line))).size == len(word):
            return [idx, m.b + 1, m.b + m.size]
    return None


def checkio(text: str, word: str) -> Union[ValueError, List[int]]:
    matrix = text.lower().replace(" ", "").split("\n")
    if m := find_match(matrix, word):
        return [m[0], m[1], m[0], m[2]]
    # rotate text, to check match vertically
    matrix = ["".join(l) for l in zip_longest(*matrix, fillvalue="")]
    if m := find_match(matrix, word):
        return [m[1], m[0], m[2], m[0]]
    return ValueError("The rhyme doesn't contain word")


if __name__ == "__main__":
    result = checkio(
        """DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""",
        "ten",
    )
    assert result == [2, 14, 2, 16]

    result = checkio(
        """He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""",
        "noir",
    )
    assert result == [4, 16, 7, 16]

    result = checkio(
        """
        xa
        xb
        x
        """,
        "ab",
    )
    assert result == [1, 2, 2, 2]
print("PASSED!!!")
