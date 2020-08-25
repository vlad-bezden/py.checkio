"""What Is Wrong With This Family?

    https://py.checkio.org/en/mission/wrong-family/

    Michael always knew that there was something wrong with his family.
    Many strangers were introduced to him as part of it.
    Michael should figure this out. He's spent almost a month parsing
    the family archives. He has all father-son connections of his entire
    family collected in one place.
    With all that data Michael can easily understand who the strangers are.
    Or maybe the only stranger in this family is Michael? Let's see.

    You have a list of family ties between father and son.
    Each element on this list has two elements.
    The first is the father's name, the second is the son's name.
    All names in the family are unique. Check if the family tree is correct.
    There are no strangers in the family tree.
    All connections in the family are natural.

    Input:  List of lists. Each element has two strings.
            The list has at least one element
    Output: bool. Is the family tree correct.

    Example:
    is_family([
        ['Logan', 'Mike']
    ]) == True
    is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack']
    ]) == True
    is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == True
    is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Logan']
    ]) == False  # Can you be a father for your father?
    is_family([
        ['Logan', 'Mike'],
        ['Logan', 'Jack'],
        ['Mike', 'Jack']
    ]) == False  # Can you be a father for your brother?
    is_family([
        ['Logan', 'William'],
        ['Logan', 'Jack'],
        ['Mike', 'Alexander']
    ]) == False  # Looks like Mike is a stranger in Logan's family

    Precondition: 1 <= len(tree) < 100
"""

from collections import defaultdict
from typing import List, Set


def is_family(tree: List[List[str]]) -> bool:
    ancestors: defaultdict[str, Set[str]] = defaultdict(set)
    for father, son in tree:
        if (
            father == son
            or son in ancestors[father]
            or father in ancestors[son]
            or ancestors[son].intersection(ancestors[father])
        ):
            return False
        ancestors[son].update([father])
    # check if there is only one parent in the tree.
    # parent's ancestors set is always empty, since it's root of the tree
    return 1 == sum(1 for parent in ancestors if ancestors[parent] == set())


if __name__ == "__main__":
    assert is_family([["Logan", "Mike"]]) is True, "One father, one son"
    assert is_family([["Logan", "Mike"], ["Logan", "Jack"]]) is True, "Two sons"
    assert (
        is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Alexander"]]) is True
    ), "Grandfather"
    assert (
        is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Logan"]]) is False
    ), "Can you be a father to your father?"
    assert (
        is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Jack"]]) is False
    ), "Can you be a father to your brother?"
    assert (
        is_family([["Logan", "William"], ["Logan", "Jack"], ["Mike", "Alexander"]])
        is False
    ), "Looks like Mike is stranger in Logan's family"

    print("PASSED!!!")
