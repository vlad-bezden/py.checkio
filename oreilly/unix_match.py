"""Unix Match

    https://py.checkio.org/en/mission/unix-match/

    Sometimes you find yourself in a situation where among a huge number of
    files on your computer or in a separate folder you need to find files of
    a certain type - for example, images with the extension '.jpg' or
    documents with the extension '.txt', or even files that have the word
    'butterfly' in their name. Doing this manually can be time-consuming.
    'Matching' or patterns for searching files by a specific mask are just
    what you need for these sort of challenges.

    This mission will help you understand how this works.

    You need to find out if the given unix pattern matches the given filename.

    Let me show you a couple of small examples of matching the filenames
    in the unix-shell. For example, * matches everything and *.txt
    matches all of the files that have txt extension. Here is a small
    table that shows symbols that can be used in patterns.

    *	matches everything
    ?	matches any single character
    [seq]	matches any character in seq
    [!seq]	matches any character not in seq

    Input: Two arguments. Both are strings.
    Output: Bool.
"""

import re


def unix_match(filename: str, pattern: str) -> bool:
    reg_exp = pattern
    for k, v in {
        ".": r"\.",
        "*": ".*",
        "?": ".",
        "[!": "[^",
        "[[]": r"\[",
        "[]]": r"\]",
        "[.]": r"\?",
        "[.*]": r"\*",
    }.items():
        reg_exp = reg_exp.replace(k, v)

    try:
        return re.match(reg_exp, filename) is not None
    except re.error:
        return filename == pattern


if __name__ == "__main__":
    assert unix_match("somefile.txt", "*") is True
    assert unix_match("other.exe", "*") is True
    assert unix_match("my.exe", "*.txt") is False
    assert unix_match("log1.txt", "log?.txt") is True
    assert unix_match("log1.txt", "log[1234567890].txt") is True
    assert unix_match("log12.txt", "log?.txt") is False
    assert unix_match("log12.txt", "log??.txt") is True
    assert unix_match("name.txt", "name[]txt") is False
    assert unix_match("1name.txt", "[!abc]name.txt") is True
    assert unix_match("1name.txt", "[!1234567890]*") is False
    assert unix_match("txt", "????*") is False
    assert unix_match("[?*]", "[[][?][*][]]") is True
    assert unix_match("[!]check.txt", "[!]check.txt") is True

    print("PASSED!!!")
