"""Network Attack

We are given information about the connections in the network and the security level
for each computer. Security level is the time (in minutes) that is required for the
virus to capture a machine. Capture time is not related to the number of infected
computers attacking the machine. Infection start from the 0th computer
(which is already infected).
Connections in the network are undirected. Security levels are not equal to
zero (except infected).

Information about a network is represented as a matrix NxN size, where N is a number
of computers. If ith computer connected with jth computer,
then matrix[i][j] == matrix[j][i] == 1, else 0.
Security levels are placed in the main matrix diagonal,
so matrix[i][i] is the security level for the ith computer.

You should calculate how much time is required to capture the whole network in minutes.

Input: Network information as a list of lists with integers.
Output: The total time of taken to capture the network as an integer.
Precondition:
3 ≤ len(matrix) ≤ 10
matrix[0][0] == 0
all(len(row) == len(matrix[0]) for row in matrix)
all(matrix[i][j] == matrix[j][i] for i in range(len(matrix))
    for j in range(len(matrix)))
all(0 < matrix[i][i] < 10 for i in range(1, len(matrix)))
all(0 ≤ matrix[i][j] ≤ 1 for i in range(len(matrix))
    for j in range(len(matrix)) if i != j)
"""

from itertools import compress, count
from typing import Dict, List, Iterable, Optional

INFINITY = 2 ** 63 - 1
# mypy doesn't like if int has None value.
VOID = -1
Matrix = List[List[int]]


def find_the_lowest_cost_node(
    matrix: Matrix, costs: Dict[int, int], processed: List[int]
) -> int:
    lowest_cost = INFINITY
    lowest_cost_node = VOID
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def get_neighbors(data: List[int], processed: List[int], node: int) -> Iterable[int]:
    # remove security level (diagonal value)
    mask = data[:node] + [0] + data[node + 1 :]
    # set mask = 0 to processed items
    for item in processed:
        mask[item] = 0
    return compress(count(), mask)


def capture(matrix: Matrix) -> int:
    nodes_values = {i: matrix[i][i] for i in range(len(matrix))}
    costs = {i: INFINITY for i in range(len(matrix))}
    costs[0] = nodes_values[0]
    processed: List[int] = []
    while 0 <= (node := find_the_lowest_cost_node(matrix, costs, processed)):
        neighbors = get_neighbors(matrix[node], processed, node)
        for n in neighbors:
            if (new_cost := costs[node] + nodes_values[n]) < costs[n]:
                costs[n] = new_cost
        processed.append(node)

    return max(costs.values())


if __name__ == "__main__":
    expected = 8
    result = capture(
        [
            [0, 1, 0, 1, 0, 1],
            [1, 8, 1, 0, 0, 0],
            [0, 1, 2, 0, 0, 1],
            [1, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 3, 1],
            [1, 0, 1, 0, 1, 2],
        ]
    )
    assert result == expected, f"Base example. {expected=}, {result=}"

    expected = 4
    result = capture(
        [
            [0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 0, 0],
            [0, 1, 2, 0, 0, 1],
            [1, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 3, 1],
            [1, 0, 1, 0, 1, 2],
        ]
    )
    assert result == expected, f"Low security. {expected=}, {result=}"

    expected = 9
    result = capture([[0, 1, 1], [1, 9, 1], [1, 1, 9]])
    assert result == expected, f"Small. {expected=}, {result=}"

    expected = 45
    result = capture(
        [
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 3, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 4, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 5, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 6, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 7, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 8, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
        ]
    )
    assert result == expected, f"Edge. {expected=}, {result=}"

    print("DONE!!!")
