"""
First word (simplified).

You are given a string where you have to find its first word.

This is a simplified version of the First Word mission.

Input string consists of only english letters and spaces.
There aren’t any spaces at the beginning and the end of the string.
Input: A string.

Output: A string.

Example:
first_word("Hello world") == "Hello"

How it is used: The first word is a command in a command line.

Precondition: Text can contain a-z, A-Z and spaces.

Summary:
It uses Python 3.8 walrun operator, split, and find methods

find() is much-much faster for a long strings:

Results:
using_split t = 0.0430 sec
using_split t = 0.0240 sec
using_split t = 5.7674 sec
using_split t = 0.8268 sec

using_index t = 0.0314 sec
using_index t = 0.0277 sec
using_index t = 0.0314 sec
using_index t = 0.1834 sec

using_index_and_walrun t = 0.0306 sec
using_index_and_walrun t = 0.0282 sec
using_index_and_walrun t = 0.0379 sec
using_index_and_walrun t = 0.1804 sec
"""


def using_split(text: str) -> str:
    """Returns the first word in a given text."""
    return text.split()[0]


def using_index(text: str) -> str:
    """Returns the first word in a given text."""
    index = text.find(" ")
    return text[:index] if index != -1 else text


def using_index_and_walrun(text: str) -> str:
    """Returns the first word in a given text."""
    return text[:index] if (index := text.find(" ")) != -1 else text


if __name__ == "__main__":
    from timeit import timeit

    inputs = ["asdf we" * 10, "asdfawe" * 10, "asdf we" * 10_000, "asdfawe" * 10_000]

    for f in [using_split, using_index, using_index_and_walrun]:
        for input in inputs:
            t = timeit(stmt="f(input)", number=10000, globals=globals())
            print(f"{f.__name__} {t = :.4f} sec")
        print()
