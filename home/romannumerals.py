"""
For this task, you should return a roman numeral using the
specified integer value ranging from 1 to 3999

Input: A number as an integer.
Output: The Roman numeral as a string.
Precondition: 0 < number < 4000

"""

ROMAN_NUMBERS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}


def checkio(data: int) -> str:
    result = ''
    for r, i in ROMAN_NUMBERS.items():
        quotion, reminder = divmod(data, i)
        if quotion != 0:
            result += r * quotion
            data = reminder
    return result


if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
