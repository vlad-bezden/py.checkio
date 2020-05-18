"""Goes Right After
    https://py.checkio.org/en/mission/goes-after/

    In a given word you need to check if one symbol goes right after another.

    Cases you should expect while solving this challenge:

    If more than one symbol is in the list you should always count the first one
    one of the symbols are not in the given word - your function should return False;
    any symbol appears in a word more than once - use only the first one;
    two symbols are the same - your function should return False;
    the condition is case sensitive, which means 'a' and 'A' are two different symbols.
    Input: Three arguments. The first one is a given string,
    second is a symbol that should go first, and the third is a
    symbold that should go after the first one.

    Output: A bool.

    Example:

    goes_after('world', 'w', 'o') == True
    goes_after('world', 'w', 'r') == False
    goes_after('world', 'l', 'o') == False
    goes_after('panorama', 'a', 'n') == True
    goes_after('list', 'l', 'o') == False
    goes_after('', 'l', 'o') == False
    goes_after('list', 'l', 'l') == False
    goes_after('world', 'd', 'w') == False
"""


def goes_after(word: str, first: str, second: str) -> bool:
    return 0 <= (f := word.find(first)) and word.find(second) - f == 1


if __name__ == "__main__":
    assert goes_after("world", "w", "o") is True
    assert goes_after("world", "w", "r") is False
    assert goes_after("world", "l", "o") is False
    assert goes_after("panorama", "a", "n") is True
    assert goes_after("list", "l", "o") is False
    assert goes_after("", "l", "o") is False
    assert goes_after("list", "l", "l") is False
    assert goes_after("world", "d", "w") is False
    assert goes_after("almaz", "m", "a") is False
    assert goes_after("almaz", "r", "a") is False
    print("PASSED!!!")
