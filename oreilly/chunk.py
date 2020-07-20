"""Chunk.

    https://py.checkio.org/en/mission/chunk/

    You have a lot of work to do, so you might want to split it into smaller pieces.
    This way you'll know which piece you'll do on Monday,
    which will be for Tuesday and so on.

    Split a list into smaller lists of the same size (chunks).
    The last chunk can be smaller than the default chunk-size.
    If the list is empty, then you shouldn't have any chunks at all.

    Input: Two arguments. A List and chunk size.
    Output: An List with chunked List.

    Precondition: chunk-size > 0
"""

from typing import List


def chunking_by(items: List[int], size: int) -> List[List[int]]:
    return [items[s : s + size] for s in range(0, len(items), size)]


if __name__ == "__main__":
    assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
    assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
    assert list(chunking_by([5, 4], 7)) == [[5, 4]]
    assert list(chunking_by([], 3)) == []
    assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]
    print("PASSED!!!")
