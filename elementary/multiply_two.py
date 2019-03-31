"""
Multiplpy two numbers.

Compares different options to multiply two numbers:

Performance:
mul            0.1389
<lambda>       0.1693
mul_func       0.1708
"""

from operator import mul
from timeit import timeit
from random import sample

mul_lambda = lambda a, b: a * b


def mul_func(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    for f in [mul, mul_lambda, mul_func]:
        a, b = sample(range(0, int(1e9)), 2)
        t = timeit(stmt="f(a, b)", number=int(1e6), globals=globals())
        print(f"{f.__name__:<15}{t:.4f}")
