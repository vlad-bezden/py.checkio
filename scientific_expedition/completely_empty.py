"""Completely Empty

You need to figure if a wellfounded and wellsized iterable is completely empty.

An iterable x0 is wellfounded if there is no infinite sequence

x1,x2,x3... such that ... in x3 in x2 in x1 in x0 (where in is meant iteratively,
x(n+1) will be encountered while iterating through xn).
A wellfounded iterable is wellsized if it has only finitely many iterable elements,
and all of them are wellsized.

A wellfounded iterable is completely empty when all its elements are completely empty.

Some consequences of the above definitions:
* any empty iterable is completely empty
* a non-iterable is never completely empty
* the only wellfounded string is '', and it is completely empty
* bytes, and (possibly nested) tuples/frozensets of them are always
wellfounded and wellsized
* {'': 'Nonempty'} is a wellfounded and completely empty iterable
* after c=[]; c.append(c), c is a non-wellfounded iterable
* itertools.repeat(()) is wellfounded but not wellsized
* itertools.repeat(5) is wellfounded and wellsized

Input: A wellfounded and wellsized iterable.
Output: A bool.
"""

from typing import Iterable


def completely_empty(val: Iterable) -> bool:
    try:
        return all(map(completely_empty, val))
    except Exception:
        return False


if __name__ == "__main__":
    assert completely_empty([]) is True, "First"
    assert completely_empty([1]) is False, "Second"
    assert completely_empty([[]]) is True, "Third"
    assert completely_empty([[], []]) is True, "Forth"
    assert completely_empty([[[]]]) is True, "Fifth"
    assert completely_empty([[], [1]]) is False, "Sixth"
    assert completely_empty([0]) is False, "[0]"
    assert completely_empty([""]) is True, "['']"
    assert completely_empty([[], [{"": "No WAY"}]]) is True
    assert (
        completely_empty(type("", (), {"__getitem__": ().__getitem__})()) is True
    ), "__getitem__"
    assert completely_empty([iter(())]) is True, "[iter(())]"

    print("DONE!!!")
