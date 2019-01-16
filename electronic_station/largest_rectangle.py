"""
Largest Rectangle in a Histogram

You have a histogram. Try to find size of the biggest rectangle you can build out of the histogram bars.

Input: List of all rectangles heights in histogram

Output: Area of the biggest rectangle
Precondition:
0 < len(data) < 1000
"""

from typing import List


def largest_histogram(histogram: List[int]) -> int:
    max_value = 0
    for i in range(max(histogram), 0, -1):
        adjacent_coutner = 0
        counter = 0
        for v in [i <= x for x in histogram]:
            if v:
                counter += 1
                adjacent_coutner = max(counter, adjacent_coutner)
            else:
                counter = 0
        max_value = max(max_value, adjacent_coutner * i)

    return max_value


if __name__ == "__main__":
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
