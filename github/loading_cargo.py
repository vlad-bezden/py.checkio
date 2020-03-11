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

    Output:
        using_combinations 0.0041
        clear_solution 0.0023
        using_combinations 0.0025
        clear_solution 0.0015
        using_combinations 0.0167
        clear_solution 0.0107
        using_combinations 0.0091
        clear_solution 0.0050
        using_combinations 0.0283
        clear_solution 0.0151
        using_combinations 0.0090
        clear_solution 0.0056
"""

from itertools import combinations, compress, product
from timeit import timeit
from collections import namedtuple

Test = namedtuple("Test", ["data", "expected"])


def using_product(data):
    ans = mass = sum(data)
    for comb in product((0, 1), repeat=len(data)):
        ans = min(ans, abs(mass - 2 * sum(compress(data, comb))))
    return ans


def using_combinations(data):
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


def clear_solution(data):
    diffs = {0}
    total = sum(data)
    for i in data:
        temp = set()
        for diff in diffs:
            temp.add(abs(i - diff))
            temp.add(abs(i + diff))
        diffs = temp
    return min(diffs)


if __name__ == "__main__":
    tests = [
        Test([10, 10], 0),
        Test([10], 10),
        Test([5, 8, 13, 14, 27], 3),
        Test([5, 5, 5, 6], 1),
        Test([12, 30, 30, 32, 42, 49], 9),
        Test([1, 1, 1, 3], 0),
    ]

    for test in tests:
        for func in [using_product, using_combinations, clear_solution]:
            result = func(test.data)
            assert result == test.expected, f"{test.data=}, {test.expected=}, {result=}"
            t = timeit(stmt=f"func({test.data})", number=1_000, globals=globals())
            print(f"{func.__name__} {t:.4f}")
        print("\n")
    print("PASSED!")
