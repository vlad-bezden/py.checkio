"""
There are four substring missions that were born all in one day
and you shouldn’t be needed more than one day to solve them.
All of those mission can be simply solved by brute force,
but is it always the best way to go?
(you might not have access to all of those missions yet,
but they are going to be available with more opened islands on the map).

A very similar to the first is the second mission of the series
with only one distinction is that you should look in a completely different way.
You need to find the first longest substring with all unique letters.
For example, in substring "abca" we have two substrings with unique letters "abc" and "bca",
but we should take the first one, so the answer is "abc".

Input: String.

Output: String.
"""


def non_repeat(line: str) -> str:
    """
    The longest substring without repeating chars
    """
    candidates = []
    candidate = ""

    for l in line:
        if l in candidate:
            candidates.append(candidate)
            candidate = candidate.split(l)[-1]
        candidate += l
    candidates.append(candidate)

    return max(candidates, key=len)


if __name__ == "__main__":
    assert non_repeat("aaaaa") == "a", "First"
    assert non_repeat("abdjwawk") == "abdjw", "Second"
    assert non_repeat("abcabcffab") == "abcf", "Third"
    assert non_repeat("") == "", "Fourth"
    assert non_repeat("w") == "w", "Fifth"
    assert non_repeat("wq")
