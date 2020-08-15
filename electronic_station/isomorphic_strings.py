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

    Outputs:
    isometric_strings_set('add', 'egg'). Exec time = 0.000110
    isometric_strings_dict('add', 'egg'). Exec time = 0.000098
    isometric_strings_translate('add', 'egg'). Exec time = 0.000057

    isometric_strings_set('foo', 'bar'). Exec time = 0.000102
    isometric_strings_dict('foo', 'bar'). Exec time = 0.000094
    isometric_strings_translate('foo', 'bar'). Exec time = 0.000056

    isometric_strings_set('', ''). Exec time = 0.000073
    isometric_strings_dict('', ''). Exec time = 0.000039
    isometric_strings_translate('', ''). Exec time = 0.000032

    isometric_strings_set('all', 'all'). Exec time = 0.000103
    isometric_strings_dict('all', 'all'). Exec time = 0.000096
    isometric_strings_translate('all', 'all'). Exec time = 0.000056

    isometric_strings_set('paper', 'title'). Exec time = 0.000121
    isometric_strings_dict('paper', 'title'). Exec time = 0.000133
    isometric_strings_translate('paper', 'title'). Exec time = 0.000070

    isometric_strings_set('paper', 'words'). Exec time = 0.000125
    isometric_strings_dict('paper', 'words'). Exec time = 0.000092
    isometric_strings_translate('paper', 'words'). Exec time = 0.000069

    isometric_strings_set('hall', 'hoop'). Exec time = 0.000111
    isometric_strings_dict('hall', 'hoop'). Exec time = 0.000113
    isometric_strings_translate('hall', 'hoop'). Exec time = 0.000064

    Conclusion:
    Using translate is 2-3 times faster then using set or dictionary
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
