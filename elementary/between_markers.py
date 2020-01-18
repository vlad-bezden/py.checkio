"""
Between Markers.

You are given a string and two markers (the initial and final).
You have to find a substring enclosed between these two markers.
But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker then the beginning should be considered as the
beginning of a string.
If there is no final marker then the ending should be considered as the
ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker is standing in front of the initial one then return an empty string.
Input: Three arguments. All of them are strings.
The second and third arguments are the initial and final markers.

Output: A string.

Precondition: can't be more than one final marker and can't be more than one initial
"""


def between_markers(text: str, begin: str, end: str) -> str:
    """Returns substring between two given markers.

    It uses text[start:end] structure.
    [0, text.find(begin) + len(begin)][begin in text] - returns 'start' and
    it returns 0 if [begin in text] is equal to False (0)
    and it will return text.find(begin) + len(begin) if [begin in text] is equal to
    True (1). The same logic is for:
    [None, text.find(end)][end in text]
    """

    return text[
        [0, text.find(begin) + len(begin)][begin in text] : [None, text.find(end)][
            end in text
        ]
    ]


if __name__ == "__main__":
    assert between_markers("What is >apple<", ">", "<") == "apple", "One sym"
    assert (
        between_markers(
            "<head><title>My new site</title></head>", "<title>", "</title>"
        )
        == "My new site"
    ), "HTML"
    assert between_markers("No[/b] hi", "[b]", "[/b]") == "No", "No opened"
    assert between_markers("No [b]hi", "[b]", "[/b]") == "hi", "No close"
    assert between_markers("No hi", "[b]", "[/b]") == "No hi", "No markers at all"
    assert between_markers("No <hi>", ">", "<") == "", "Wrong direction"
