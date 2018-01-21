'''
This mission is the first one of the series.
Here you should find the length of the longest substring that consists
of the same letter. For example, line 'aaabbcaaaa'
contains four substrings with the same letters 'aaa', 'bb','c' and 'aaaa'.
The last substring is the longest one which makes it an answer.

Input: String.

Output: Int.
'''

import re


def long_repeat(line):
    '''
    length the longest substring that consists of the same char

    Another solution is by using groupby function from itertools

    from itertools import groupby

    max([len(list(i)) for _, i in groupby(data)], default=0)
    max([len(list(i[1])) for i in groupby(data)], default=0)
    '''

    return max([len(i[0]) for i in re.findall(r'((.)\2*)', line)], default=0)


if __name__ == '__main__':
    # These 'asserts' using only for self-checking and not necessary
    # for auto-testing

    assert long_repeat('sdsffffse') == 4, 'First'
    assert long_repeat('ddvvrwwwrggg') == 3, 'Second'
    assert long_repeat('') == 0, 'Third'

    print('Run is good. How is Check?')
