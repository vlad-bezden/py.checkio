"""Remove Brackets
    https://py.checkio.org/en/mission/remove-brackets/

    Before solving this mission, you can try to solve the "Brackets" mission.

    Your task is to restore the balance of open and closed brackets by
    removing unnecessary ones, while trying to use the minimum number of deletions.

    Only 3 types of brackets (), [] and {} can be used in the given string.

    Only a parenthesis can close a parenthesis. That is. in this expression "(}" -
    the brackets aren’t balanced. In an empty string, i.e.,
    in a string that doesn’t contain any brackets - the brackets are balanced,
    but removing all of the brackets isn’t considered to be an optimal solution.

    If there are more than one correct answer, then you should choose the one
    where the character that can be removed is closer to the beginning.
    For example, in this case "[(])", the correct answer will be "()",
    since the removable brackets are closer to the beginning of the line.

    Input: A string of characters () {} []
    Output: A string of characters () {} []

    Example:
    remove_brackets('(()()') == '()()'
    remove_brackets('[][[[') == '[]'
"""


from itertools import combinations, dropwhile, takewhile
from collections import namedtuple


Test = namedtuple("Test", ["data", "expected"])

TESTS = [
    Test("(()()", "()()"),
    Test("[][[[", "[]"),
    Test("[[(}]]", "[[]]"),
    Test("[[{}()]]", "[[{}()]]"),
    Test("[[[[[[", ""),
    Test("[[[[}", ""),
    Test("", ""),
    Test("[(])", "()"),
    Test("[(()]", "[()]"),
]


BRACKETS_MAP = dict(zip("[{(", "]})"))


def is_balanced(expression: str) -> bool:
    """Check if expression is balanced.

        Balanced means when open brackets match closing brackets.
        etc. "([]){}"
    """
    stack = []
    for c in expression:
        if c in BRACKETS_MAP:
            stack.append(BRACKETS_MAP[c])
        elif c not in BRACKETS_MAP.values():
            raise ValueError(f"Invalid: '{c}' letter in expression")
        elif not (stack and stack.pop() == c):
            return False
    return not stack


def remove_brackets(expression: str) -> str:
    for length in range(len(expression), -1, -1):
        for combination in [*combinations(expression, length)][::-1]:
            if is_balanced(combination):
                return "".join(combination)


def main():
    for test, expected in TESTS:
        assert (
            result := remove_brackets(test)
        ) == expected, f"{test=}, {result=}, {expected=}"
    print("PASSED!!!")


if __name__ == "__main__":
    main()
