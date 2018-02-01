'''
Sophia's drones are not soulless and stupid drones; they can make and have
friends. In fact, they already are working for the their own social
network just for drones! Sophia has received the data about the connections
between drones and she wants to know more about relations between them.

We have an array of straight connections between drones. Each connection is
represented as a string with two names of friends separated by hyphen.
For example: 'dr101-mr99' means what the dr101 and mr99 are friends.
Your should write a function that allow determine more complex connection
between drones. You are given two names also. Try to determine if they are
related through common bonds by any depth. For example: if two drones have a
common friends or friends who have common friends and so on.

Let's look at examples:
scout2 and scout3 have the common friend scout1 so they are related.
super and scout2 are related through sscout, scout4 and scout1.
But dr101 and sscout are not related.

Input: Three arguments: Information about friends as a tuple of strings;
first name as a string; second name as a string.

Output: Are these drones related or not as a boolean.

Precondition: len(network) ≤ 45
if 'name1-name2' in network, then 'name2-name1' not in network
3 ≤ len(drone_name) ≤ 6

first_name and second_name in network.
'''

from collections import defaultdict
from typing import Tuple, Dict, Set


def create_graph(network: Tuple[str, ...]) -> Dict[str, Set[str]]:
    '''Creates graph of network as dict'''

    graph: Dict[str, Set[str]] = defaultdict(set)
    for k, v in (x.split('-') for x in network):
        graph[k].add(v)
        graph[v].add(k)

    return graph


def create_forests(graph: Dict[str, Set[str]]) -> Set[str]:
    '''Creates forests (subnetworks) if they are disconnected'''

    processed = set()
    forests = []

    for k, v in graph.items():
        if k in processed:
            continue
        forest = set()
        candidates = set([k])
        while candidates:
            node = candidates.pop()
            if node in processed:
                continue
            forest.add(node)
            processed.add(node)
            candidates.update(graph.get(node, {}))

        forests.append(forest)

    return forests


def check_for_friends(forests, friends):
    '''Check if names belong to the same network'''

    for forest in forests:
        if friends < forest:
            return True

    return False


def check_connection(network: Tuple[str, ...],
                     first: str, second: str) -> bool:

    graph = create_graph(network)
    forests = create_forests(graph)
    result = check_for_friends(forests, {first, second})

    return result


if __name__ == '__main__':
    assert check_connection(
        ('dr101-mr99', 'mr99-out00', 'dr101-out00', 'scout1-scout2',
         'scout3-scout1', 'scout1-scout4', 'scout4-sscout', 'sscout-super'),
        'scout2', 'scout3'), 'Scout Brotherhood'
    assert check_connection(
        ('dr101-mr99', 'mr99-out00', 'dr101-out00', 'scout1-scout2',
         'scout3-scout1', 'scout1-scout4', 'scout4-sscout', 'sscout-super'),
        'super', 'scout2'), 'Super Scout'
    assert not check_connection(
        ('dr101-mr99', 'mr99-out00', 'dr101-out00', 'scout1-scout2',
         'scout3-scout1', 'scout1-scout4', 'scout4-sscout', 'sscout-super'),
        'dr101', 'sscout'), 'I do not know any scouts.'
