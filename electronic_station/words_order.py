"""Words Order

    https://py.checkio.org/en/mission/words-order/

    You have a text and a list of words. You need to check if the words
    in a list appear in the same order as in the given text.

    Cases you should expect while solving this challenge:

    * a word from the list is not in the text - your function should return False;
    * any word can appear more than once in a text - use only the first one;
    * two words in the given list are the same - your function should return False;
    * the condition is case sensitive, which means 'hi' and 'Hi'
        are two different words;
    * the text includes only English letters and spaces;

    Input: Two arguments. The first one is a given text, the second is a list of words.
    Output: A bool.
"""

from typing import List


def words_order(text: str, words: List[str]) -> bool:
    try:
        idxs = [text.split().index(word) for word in words]
        return all(0 < y - x for x, y in zip(idxs[0:], idxs[1:]))
    except ValueError:
        return False


if __name__ == "__main__":
    assert words_order("hi world im here", ["world", "here"]) is True
    assert words_order("hi world im here", ["here", "world"]) is False
    assert words_order("hi world im here", ["world"]) is True
    assert words_order("hi world im here", ["world", "here", "hi"]) is False
    assert words_order("hi world im here", ["world", "im", "here"]) is True
    assert words_order("hi world im here", ["world", "hi", "here"]) is False
    assert words_order("hi world im here", ["world", "world"]) is False
    assert words_order("hi world im here", ["country", "world"]) is False
    assert words_order("hi world im here", ["wo", "rld"]) is False
    assert words_order("", ["world", "here"]) is False

    print("PASSED!!!")