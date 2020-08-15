"""Isomorphic Strings

    https://py.checkio.org/en/mission/isometric-strings/

    Maybe it's a cipher? Maybe, but we don’t know for sure.
    Maybe you can call it "homomorphism"? i wish I know this word before.
    You need to check that the 2 given strings are isometric.
    This means that a character from one string can become a match
    for characters from another string.

    One character from one string can correspond only to one character
    from another string. Two or more characters of one string can
    correspond to one character of another string, but not vice versa.


    Input: Two arguments. Both strings.
    Output: Boolean.

    Example:
    isometric_strings('add', 'egg') == True
    isometric_strings('foo', 'bar') == False

    Precondition:
    both strings are the same size
"""

from timeit import repeat
from dataclasses import dataclass
from typing import Callable, Sequence, Tuple


@dataclass
class Test:
    data: Tuple[str, str]
    expected: bool


TESTS = [
    Test(("add", "egg"), True),
    Test(("foo", "bar"), False),
    Test(("", ""), True),
    Test(("all", "all"), True),
    Test(("paper", "title"), True),
    Test(("paper", "words"), False),
    Test(("hall", "hoop"), False),
]


def isometric_strings_translate(str1: str, str2: str) -> bool:
    trans = str.maketrans(str1, str2)
    return str1.translate(trans) == str2


def isometric_strings_set(str1: str, str2: str) -> bool:
    return len(set(zip(str1, str2))) == len(set(str1))


def isometric_strings_dict(str1: str, str2: str) -> bool:
    map = {}
    for s1, s2 in zip(str1, str2):
        if map.setdefault(s1, s2) != s2:
            return False
    return True


def validate(funcs: Sequence[Callable[[str, str], bool]]) -> None:
    for test in TESTS:
        for f in funcs:
            result = f(*test.data)
            assert result == test.expected, f"{f.__name__}({test}), {result = }"
    print("PASSED!!!\n")


if __name__ == "__main__":
    funcs = [isometric_strings_set, isometric_strings_dict, isometric_strings_translate]
    validate(funcs)
    for test in TESTS:
        for f in funcs:
            t = repeat(
                stmt=f"f('{test.data[0]}', '{test.data[1]}')",
                repeat=10,
                number=100,
                globals=globals(),
            )
            print(f"{f.__name__}{test.data}. Exec time = {min(t):.6f}")
        print()
