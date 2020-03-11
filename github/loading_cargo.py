"""Loading Cargo

    https://py.checkio.org/en/mission/loading-cargo/

    You have been given a list of integer weights. You should help
    Stephen distribute these weights into two sets, such that the
    difference between the total weight of each set is as low as possible.

    Input data: A list of the weights as a list of integers.
    Output data: The number representing the lowest possible
    weight difference as a positive integer.

    Precondition:
    0 < len(weights) ≤ 10
    all(0 < x < 100 for x in weights)
"""

from itertools import combinations


def checkio(data):
    """ Finds difference between the total weight of each set

        Create all permutations and filter out the ones
        that are greater than half of the total value
        take the closest value to the half of the total
    """
    total = sum(data)
    max_combs = max(
        (
            s
            for i in range(1, len(data))
            for c in combinations(data, i)
            if (s := sum(c)) <= total // 2
        ),
        default=0,
    )
    return total - max_combs * 2


if __name__ == "__main__":
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 14, 27]) == 3, "3rd example"
    assert checkio([5, 5, 5, 6]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
    print("PASSED!")
