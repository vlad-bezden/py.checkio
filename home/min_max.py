"""Min and Max

Return the largest (smallest) item in an iterable or the largest(smallest) of
two or more arguments.
If one positional argument is provided, it should be an iterable.
The largest (smallest) item in the iterable is returned.
If two or more positional arguments are provided, the largest (smallest) of
the positional arguments is returned.
The optional keyword-only key argument specifies a function of one argument
that is used to extract a comparison key from each list element
(for example, key=str.lower).
If multiple items are maximal (minimal), the function returns the first
one encountered.

Input: One positional argument as an iterable or two or more positional
arguments. Optional keyword argument as a function.

Output: The largest item for the "max" function and the smallest for
the "min" function.
Precondition: All test cases are correct and functions don't have to
raise exceptions.
"""


def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    smallest, *rest = args if len(args) > 1 else args[0]
    for i in rest:
        if key(i) < key(smallest):
            smallest = i
    return smallest


def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    biggest, *rest = args if len(args) > 1 else args[0]
    for i in rest:
        if key(i) > key(biggest):
            biggest = i
    return biggest


if __name__ == '__main__':
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], \
        "lambda key"
    assert max([0]) == 0, "One value"
