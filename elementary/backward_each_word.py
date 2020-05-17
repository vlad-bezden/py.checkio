"""Backward Each Word
    https://py.checkio.org/en/mission/backward-each-word/

    In a given string you should reverse every word,
    but the words should stay in their places.

    Input: A string.
    Output: A string.

    Example:
    backward_string_by_word('') == ''
    backward_string_by_word('world') == 'dlrow'
    backward_string_by_word('hello world') == 'olleh dlrow'
    backward_string_by_word('hello   world') == 'olleh   dlrow'

    Precondition: The line consists only from alphabetical symbols and spaces.
"""


def backward_string_by_word(text: str) -> str:
    return " ".join(w[::-1] for w in text.split(" "))


if __name__ == "__main__":
    assert backward_string_by_word("") == ""
    assert backward_string_by_word("world") == "dlrow"
    assert backward_string_by_word("hello world") == "olleh dlrow"
    assert backward_string_by_word("hello   world") == "olleh   dlrow"
    assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

    print("PASSED!!!")
