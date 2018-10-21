"""Remove Accents

Assuming you are developing a user based system like facebook,
you will want to provide the functionality to search for other
members regardless of the presence of accents in a username.
Without using 3rd party collation library,
you will need to remove the accents from username before comparison.

é - letter with accent; e - letter without accent; ̀ and ́ - stand alone accents;

Input: A phrase as a string (unicode)
Output: An accent free Unicode string.
Precondition: 0≤|input|≤40
"""


def checkio(in_string):
    "remove accents"

    return in_string


if __name__ == "__main__":
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
