"""
Probability Dice

You're on your way to a board game convention. Chances are there’ll be some stiff
competition, so you decide to learn more about dice probabilities since you suspect
you'll be rolling a lot of them soon.

Typically, when using multiple dice, you simply roll them and sum up all the result.
To get started with your investigation of dice probability,
write a function that takes the number of dice, the number of sides per die and a
target number and returns the probability of getting a total roll of
exactly the target value. The result should be given with four digits precision
as ±0.0001. For example, if you roll 2 six-sided dice, the probability of getting
exactly a 3 is 2/36 or 5.56%, which you should return as ≈0.0556.

For each test, assume all the dice are the same and are numbered from 1 to the number
of sides, inclusive. So a 4-sided die (D4) would have an equal chance of rolling
a 1, 2, 3 or 4. A 20-sided die (D20) would have an equal chance of
rolling any number from 1 to 20.

Tips: Be careful if you want to use a brute-force solution --
you could have a very, very long wait for edge cases.

Input: Three arguments. The number of dice, the number of sides per die and the
target number as integers.

Output: The probability of getting exactly target number on a
single roll of the given dice as a float.

Example:

Preconditions:
1 ≤ dice_number ≤ 10
2 ≤ sides ≤ 20
0 ≤ target < 1000
"""

from itertools import product
from math import isclose
from functools import partial
from typing import List
from numpy.polynomial.polynomial import polypow


def probability(dice_number, sides, target):
    """
    Using numpy polynomial
    The number of ways to obtain x as a sum of n s-sided dice
    is given by the coefficients of the polynomial:

    f(x) = (x + x^2 + ... + x^s)^n
    """

    # power series (note that the power series starts from x^1, therefore
    # the first coefficient is zero)
    powers = [0] + [1] * sides
    # f(x) polynomial, computed used polypow in numpy
    poly = polypow(powers, dice_number)
    return poly[target] / sides ** dice_number if target < len(poly) else 0


def polynomial(dice_number: int, sides: int) -> List[int]:
    """
    Calculates number of combinations for each target
    for instance dice_number: 2, sides: 6
    [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    for target: 4 there are 2 combinations, target: 5 -> 4 combinations
    """
    ret = [1] + [0] * (dice_number + 1) * sides  # extra length for negative indices
    for p in range(1, dice_number + 1):
        rolling_sum = 0
        for i in range(p * sides, p - 1, -1):
            rolling_sum += ret[i - sides] - ret[i]
            ret[i] = rolling_sum
        ret[p - 1] = 0
    return ret[:-sides]


def probability_1(dice_number: int, sides: int, target: int) -> float:
    """
    Using manually created polynomial
    """
    p = polynomial(dice_number, sides)
    return p[target] / sides ** dice_number if target < len(p) else 0


def probability_2(dice_number: int, sides: int, target: int) -> float:
    """
    Using brute force for all possible permutations.
    It works, but very slow for big number of dices sides
    """
    p = sum(
        1 for i in product(range(1, sides + 1), repeat=dice_number) if sum(i) == target
    )
    return p / sides ** dice_number


if __name__ == "__main__":
    almost_equal = partial(isclose, abs_tol=0.1 ** 4)

    assert almost_equal(probability(2, 6, 3), 0.0556), "Basic example"
    assert almost_equal(probability(2, 6, 4), 0.0833), "More points"
    assert almost_equal(probability(2, 6, 7), 0.1667), "Maximum for two 6-sided dice"
    assert almost_equal(probability(2, 3, 5), 0.2222), "Small dice"
    assert almost_equal(probability(2, 3, 7), 0.0000), "Never!"
    assert almost_equal(probability(3, 6, 7), 0.0694), "Three dice"
    assert almost_equal(probability(10, 10, 50), 0.0375), "Many dice, many sides"
    assert almost_equal(probability(1, 2, 9999), 0.0000), "Invalid Target"
    print("DONE!")
