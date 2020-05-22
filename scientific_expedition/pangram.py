"""Pangram
    https://py.checkio.org/en/mission/pangram/

    A pangram (Greek:παν γράμμα, pan gramma, "every letter") or
    holoalphabetic sentence for a given alphabet is a sentence using
    every letter of the alphabet at least once. Perhaps you are
    familiar with the well known pangram "The quick brown fox jumps over the lazy dog".

    For this mission, we will use the latin alphabet (A-Z).
    You are given a text with latin letters and punctuation symbols.
    You need to check if the sentence is a pangram or not. Case does not matter.

    Input: A text as a string.
    Output: Whether the sentence is a pangram or not as a boolean.

    Example:
    check_pangram("The quick brown fox jumps over the lazy dog.") == True
    check_pangram("ABCDEF.") == False

    Precondition:
    all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
    0 < len(text)
"""

from string import ascii_lowercase as letters


def check_pangram(text: str) -> bool:
    return set(letters).issubset(set(text.lower()))


if __name__ == "__main__":
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram(
        "Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"
    ), "Bored?"

    print("PASSED!!!")
