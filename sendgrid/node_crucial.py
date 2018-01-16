'''
Citizens of GridLand are sending emails to each other all the time.
They send everything - what they just ate, a funny picture, questions or
thoughts that are bothering them right now.
All the citizens are happy because they have such a
wonderful network that keeps them connected.

The main goal of the Mayor is to control the city's happiness.
The city's happiness is a sum of all citizens happiness.
And the happiness of each citizens is equal to the number of citizens
(always including oneself) one can send emails to.

Because the city is growing, citizens decide the Mayor needs an
assistant to focus on node protection.

Your mission is to figure out what will be the first nodes to investigate
and protect for the new assistant. Remember, you should choose the most
important node in the network. If several nodes have maximal importance,
find all of them

Input: Two arguments. Network structure (as list of connections between nodes),
users on each node (as dict where keys are node-name and values are amount of
users).

Output: List of the most crusial nodes.
'''

from collections import defaultdict


ROOT_NODE = 'A'


def graph(net):
    '''Creates graph from network of nodes'''

    graph = defaultdict(set)

    for node in net:
        graph[node[0]].add(node[1])

    return graph


def network_candidates(network, node):
    '''
    Finds network candidates

    Assumption: First node in the graph is ROOT_NODE
    '''

    candidates = set()

    if node != ROOT_NODE:
        candidates.update(ROOT_NODE)

    if node in network:
        candidates.update(network[node])

    return candidates


def happiness_network(graph, node):
    '''
    Creates network for one of the nodes to be used

    This one is generated if node is a hub (key in the dict)
    '''

    networks_to_process = network_candidates(graph, node)
    networks = []
    candidates = []

    for city in networks_to_process:
        network = [city]
        candidates += graph[city]
        while candidates:
            vertex = candidates.pop()
            # exclude currently processing node/city
            # because it can't be part of the network
            if vertex == node:
                continue
            network.append(vertex)
            candidates += graph[vertex]

        networks.append(network)

    return networks


def calc_happiness(network, users, city):
    '''
    Goes through each node and calculates happiness for each one
    '''

    price = users[city]
    networks = happiness_network(network, city)

    for net in networks:
        price += (sum([users[n] for n in net])) ** 2

    return price


def most_crucial(net, users):
    '''Driver of the program'''

    cities = set(sum(net, []))

    # get unique nodes
    network = graph(net)

    # get happiness for each city/node
    results = [(calc_happiness(network, users, city), city) for city in cities]

    # since there might be more than one city with the same number of happiness
    # we need to return all of them
    return [city[1] for city in results if city[0] == min(results)[0]]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary
    # for auto-testing
    assert most_crucial([
        ['A', 'B'],
        ['B', 'C']
    ], {
        'A': 10,
        'B': 10,
        'C': 10
    }) == ['B'], 'First'

    assert most_crucial([
        ['A', 'B']
    ], {
        'A': 20,
        'B': 10
    }) == ['A'], 'Second'

    assert most_crucial([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E']
    ], {
        'A': 0,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10
    }) == ['A'], 'Third'

    assert most_crucial([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 10,
        'D': 20
    }) == ['B'], 'Forth'

    assert most_crucial([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'A']
    ], {
        'A': 10,
        'C': 10,
        'B': 5
    }) == ['A', 'C'], 'Fifth'

    print('Nobody expected that, but you did it! It is time to share it!')
