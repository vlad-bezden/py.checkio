"""
Currency Style.

Many countries use different conventions for the thousands separator and decimal mark.
For example in the Netherlands one million one thousand two hundred and eighty
one-hundredths is written as 1.001.200,80, but in the US this is written as
1,001,200.80. Use your coding skills to convert dollars in the first style
(Netherlands, Germany, Russia, Turkey, Brazil, and others) to the second style
(US, UK, Canada, China, Japan, Mexico, and others).

Only currency amounts in dollars should be converted: $1.234,50 to $1,234.50,
$1.000 to $1,000, and $4,57 to $4.57. But don't convert your router's IP address
192.168.1.1. Also leave currency in the US style unchanged.

Input: A string containing dollar amounts to be converted.
Output: A string with converted currencies.

Precondition: 0 < len(text) ≤ 1000;
len(fractional_part_of_currency) in {0,2};
all(s[-1].isdigit() for s in currency_substrings);
all(s[0] == '$' for s in currency_substrings)
"""


def checkio(text: str) -> str:
    return ""


if __name__ == "__main__":
    assert checkio("$1.234.567,89") == "$1,234,567.89", "1st Example"
    assert checkio("$0,89") == "$0.89", "2nd Example"
    assert (
        checkio("Euro Style = $12.345,67, US Style = $12,345.67")
        == "Euro Style = $12,345.67, US Style = $12,345.67"
    ), "European and US"
    assert (
        checkio("Us Style = $12,345.67, Euro Style = $12.345,67")
        == "Us Style = $12,345.67, Euro Style = $12,345.67"
    ), "US and European"
    assert (
        checkio("$1.234, $5.678 and $9") == "$1,234, $5,678 and $9"
    ), "Dollars without cents"
