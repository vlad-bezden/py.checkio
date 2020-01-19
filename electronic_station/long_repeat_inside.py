"""Long Running Inside.

You should find a repeating sequence inside the substring.
for example: in a string "abababc" - "ab"
is a sequence that repeats more than once, so the answer will be "ababab"

Input: String.
Output: String. First the longest repeating substring.
"""


def repeating_times(line: str, sub: str) -> int:
    """Finds how many times string is repeated."""
    repeating = 0
    while line[len(sub) * repeating:].startswith(sub):
        repeating += 1
    return repeating


def repeat_inside(line: str) -> str:
    """First the longest repeating substring."""
    repeats = []
    i = 0
    for i, c in enumerate(line):
        if (j := line.find(c, i + 1)) == -1:
            continue
        repeating = 0
        sub = line[i:j]
        if times := repeating_times(line[j:], sub):
            repeats.append(sub * (times + 1))
    return max(repeats, key=len, default="")


if __name__ == "__main__":
    assert repeat_inside("aaaaa") == "aaaaa", "First"
    assert repeat_inside("aabbff") == "aa", "Second"
    assert repeat_inside("aababcc") == "abab", "Third"
    assert repeat_inside("abc") == "", "Forth"
    assert repeat_inside("abcabcabab") == "abcabc", "Fifth"
