"""YAML. More Types
    https://py.checkio.org/en/mission/yaml-more-types/

    This is the second task on parsing YAML.
    It represents the next step where parsing gets more complicated.
    The data types, such as null and bool, are being added,
    and besides that, you’re getting the ability to use quotes in strings.

    Here are some of the examples:

    name: "Bob Dylan"
    children: 6

    {
        "name": "Bob Dylan",
        "children": 6
    }

    As you can see, the string can be put in quotes. It can be both
    double and single quotes.

    name: "Bob Dylan"
    children: 6
    alive: false

    {
        "name": "Bob Dylan",
        "alive": False,
        "children": 6
    }

    true and false are the keywords defining the boolean type.

    name: "Bob Dylan"
    children: 6
    coding:

    {
        "coding": None,
        "name": "Bob Dylan",
        "children": 6
    }

    If no value is specified, it becomes undefined.
    There also is a keyword for this - null.

    Input: A format string.
    Output: An object.
"""

from typing import Union


def to_value(val: str) -> Union[str, int, bool, None]:
    if not val or val == "null":
        return None
    elif val.isnumeric():
        return int(val)
    elif val in "true false":
        return val in "true"
    return (
        (val[1:-1] if val[0] in "'\"" else val).encode("utf-8").decode("unicode_escape")
    )


def yaml(text: str) -> dict:
    return {
        (v := l.split(":"))[0]: to_value(v[1].strip()) for l in text.splitlines() if l
    }


if __name__ == "__main__":
    result = yaml("name: Alex\nage: 12")
    assert result == {"age": 12, "name": "Alex"}

    result = yaml("name: Alex Fox\n" "age: 12\n" "\n" "class: 12b")
    assert result == {
        "age": 12,
        "class": "12b",
        "name": "Alex Fox",
    }

    result = yaml('name: "Alex Fox"\n' "age: 12\n" "\n" "class: 12b")
    assert result == {
        "age": 12,
        "class": "12b",
        "name": "Alex Fox",
    }

    result = yaml('name: "Alex \\"Fox\\""\n' "age: 12\n" "\n" "class: 12b")
    assert result == {
        "age": 12,
        "class": "12b",
        "name": 'Alex "Fox"',
    }

    result = yaml('name: "Bob Dylan"\n' "children: 6\n" "alive: false")
    assert result == {
        "alive": False,
        "children": 6,
        "name": "Bob Dylan",
    }

    result = yaml('name: "Bob Dylan"\n' "children: 6\n" "coding:")
    assert result == {
        "children": 6,
        "coding": None,
        "name": "Bob Dylan",
    }

    result = yaml('name: "Bob Dylan"\n' "children: 6\n" "coding: null")
    assert result == {
        "children": 6,
        "coding": None,
        "name": "Bob Dylan",
    }

    result = yaml('name: "Bob Dylan"\n' "children: 6\n" 'coding: "null" ')
    assert result == {
        "children": 6,
        "coding": "null",
        "name": "Bob Dylan",
    }

    print("PASSED!!!")
