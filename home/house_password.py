"""House Password

Stephan and Sophia forget about security and use simple passwords for
everything. Help Nikola develop a password security check module.
The password will be considered strong enough if its length is greater than
or equal to 10 symbols, it has at least one digit, as well as containing one
uppercase letter and one lowercase letter in it.
The password contains only ASCII latin letters or digits.

Input: A password as a string (Unicode for python 2.7).
Output: Is the password safe or not as a boolean or any data type that can be
converted and processed as a boolean.
In the results you will see the converted results.

Precondition:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
"""

MIN_LENGTH = 10

validations = [
    lambda x: any(i.isdigit() for i in x),
    lambda x: any(i.islower() for i in x),
    lambda x: any(i.isupper() for i in x),
    lambda x: len(x) >= MIN_LENGTH
]


def checkio(data):
    return all(v(data) for v in validations)


if __name__ == '__main__':
    assert not checkio('A1213pokl'), "1st example"
    assert checkio('bAse730onE4'), "2nd example"
    assert not checkio('asasasasasasasaas'), "3rd example"
    assert not checkio('QWERTYqwerty'), "4th example"
    assert not checkio('123456123456'), "5th example"
    assert checkio('QwErTy911poqqqq'), "6th example"
