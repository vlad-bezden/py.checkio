'''
I start to feed one of the pigeons. A minute later two more fly by and a minute
after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). One portion of food
lasts a pigeon for a minute, but in case there's not enough food for all the
birds, the pigeons who arrived first ate first. Pigeons are hungry animals and
eat without knowing when to stop.
If I have N portions of bird feed, how many pigeons will be fed with at least
one portion of wheat?

Input: A quantity of portions wheat as a positive integer.

Output: The number of fed pigeons as an integer.

Precondition: 0 < N < 105.
'''


def checkio(number: int) -> int:

    pigeons = 1
    counter = 1

    while number > pigeons:
        number -= pigeons
        counter += 1
        if number < pigeons + counter:
            break
        pigeons += counter

    return number if number > pigeons else pigeons


if __name__ == '__main__':
    assert checkio(1) == 1, '1st example'
    assert checkio(2) == 1, '2nd example'
    assert checkio(3) == 2, '3rd example'
    assert checkio(5) == 3, '4th example'
    assert checkio(10) == 6, '5th example'
    assert checkio(40) == 15, '6th example'
