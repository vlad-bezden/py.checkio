"""The Best Number Ever.

It was Sheldon's version and his best number. But you have the coding skills to prove
that there is a better number, or prove Sheldon sheldon right.
You can return any number, but use the code to prove your number is the best!

This mission is pretty simple to solve. You are given a function called "checkio"
which will return any number (integer or float).

Let's write an essay in python code which will explain why is your number is the best.
Publishing the default solution will only earn you 0 points as the goal is to
earn points through votes for your code essay.

Input: Nothing.

Output: A number as an integer or a float or a complex.
"""

import cmath


def checkio():
    imaginary = cmath.sqrt(-1)
    print(f"I am imaginary number {imaginary=}. \U0001F923")
    return imaginary


if __name__ == "__main__":
    assert isinstance(checkio(), (int, float, complex))
    print("DONE!!!")
