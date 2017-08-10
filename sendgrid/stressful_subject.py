"""Stressful Subject mission from checkio

The function should recognises if a subject line is stressful.
A stressful subject line means that all letters are uppercase,
and/or ends by at least 3 exclamation marks and/or contains at least one
of the following “red” words "help", "asap", "urgent".
Any of those "red" words can be spelled in different ways -
"HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
even in a very loooong way "HHHEEEEEEEEELLP"

Input: Subject line as a string
Output: Boolean.
Precondition: subject can be up to 100 letters
"""

import itertools

RED_WORDS = ['help', 'asap', 'urgent']


def is_all_upper(s):
    """Checks if all leetters are uppercase"""
    return all(c.isupper() for c in s if c.isalpha())


def is_ends_with_exlamations(s):
    """Checks if centence ends with 3 exclamation marks"""
    return s.endswith('!!!')


def remove_duplicate_chars(w):
    """Removes duplicate characters in the word"""
    return ''.join(c for c, _ in itertools.groupby(w))


def get_word(w):
    """Removes any non alpha characters from the word"""
    return ''.join(c for c in w if c.isalpha()).lower()


def contains_red_word(s):
    return any(remove_duplicate_chars(get_word(w)) in RED_WORDS
               for w in s.split())


def is_stressful(subj):
    """Recoognise stressful subject"""
    return any([is_all_upper(subj),
                is_ends_with_exlamations(subj),
                contains_red_word(subj)
                ])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert is_stressful('Hi') is False, 'First'
    assert is_stressful('I neeed HELP') is True, 'Second'
    assert is_stressful('h!e!l!p') is True, 'Third'
    assert is_stressful('UUUURGGGEEEEENT here') is True, 'Forth'
    print('Done! Go Check it!')
