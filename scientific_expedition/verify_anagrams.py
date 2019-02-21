"""
Verify Anagrams

An anagram is a type of word play, the result of rearranging the letters of a word or
phrase to produce a new word or phrase, using all the original letters exactly once.
Two words are anagrams to each other if we can get one from another by rearranging
the letters. Anagrams are case-insensitive and don't take account whitespaces.
For example: "Gram Ring Mop" and "Programming" are anagrams.
But "Hello" and "Ole Oh" are not.

You are given two words or phrase. Try to verify are they anagrams or not.

Input: Two arguments as strings.

Output: Are they anagrams or not as boolean (True or False)

Precondition: 0 < |first_word| < 100;
0 < |second_word| < 100;
Words contain only ASCII latin letters and whitespaces.

Performance:
verify_anagrams_counter took: 0.281242
verify_anagrams_sorted took: 0.049765
"""

from collections import Counter
from timeit import timeit


def verify_anagrams_sorted(a: str, b: str) -> bool:
    """Using sorted algorithm."""
    return sorted(a.lower().replace(" ", "")) == sorted(b.lower().replace(" ", ""))


def verify_anagrams_counter(a: str, b: str) -> bool:
    """Using Counter object."""
    return Counter(a.lower().replace(" ", "")) == Counter(b.lower().replace(" ", ""))


if __name__ == "__main__":
    for f in [verify_anagrams_counter, verify_anagrams_sorted]:
        assert isinstance(f("a", "z"), bool), "Boolean!"
        assert f("Programming", "Gram Ring Mop") is True, "Gram of code"
        assert f("Hello", "Ole Oh") is False, "Hello! Ole Oh!"
        assert f("Kyoto", "Tokyo") is True, "The global warming crisis of 3002"
        assert f("The Morse Code", "There Come Dots") is False, "Checkio"

        t = timeit(
            stmt="f('The Morse Code', 'There Come Dots')",
            number=10000,
            globals=globals(),
        )
        print(f"{f.__name__} took: {t:.6f}")
    print("Done!")
