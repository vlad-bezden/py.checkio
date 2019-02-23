"""
Conversion From Camel Case

Your mission is to convert the name of a function (a string) from CamelCase
("MyFunctionName") into the Python format ("my_function_name") where all chars
are in lowercase and all words are concatenated with an intervening underscore
symbol "_".

Input: A function name as a CamelCase string.
Output: The same string, but in under_score.

Precondition:
0 < len(string) <= 100
Input data won't contain any numbers.
"""
import re


def from_camel_case(name: str) -> str:
    return "_".join(re.findall("[A-Z][^A-Z]*", name)).lower()


if __name__ == "__main__":
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
