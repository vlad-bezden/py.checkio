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


def graph(net):
    '''Creates graph from network of nodes'''

    graph = defaultdict(set)

    for node in net:
        graph[node[0]].add(node[1])

    return graph


def remove_city(network, city):
    '''Removes city and creates new netwrork(s)'''

    graph = defaultdict(set)

    for k, v in network.items():
        if city == k:
            # if city is a key
            next(graph[i] for i in v)
        elif city in v:
            # if city is connected to the key
            graph[k] = (v - {city})
        else:
            # it is not a city, add key, value to the dict
            graph[k] = v

    return graph


def happiness_network(graph, city):
    '''
    Creates network for one of the nodes to be used

    This one is generated if node is a hub (key in the dict)
    '''

    new_graph = remove_city(graph, city)
    all_networks = []
    processed = set()

    for k, v in new_graph.items():
        if k in processed:
            continue
        network = set()
        candidates = set(k)
        while candidates:
            vertex = candidates.pop()
            network.add(vertex)
            candidates.update(new_graph.get(vertex, {}))
            processed.add(vertex)

        all_networks.append(network)

    return check_network_connections(all_networks)


def check_network_connections(all_networks):
    '''Checks if networks have connections, and if so join them'''

    final_networks = []

    for net in all_networks:
        for sub in final_networks:
            if net & sub:
                sub.update(net)
                break
        else:
            final_networks.append(net)

    return final_networks


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
    return sorted([city[1] for city in results if city[0] == min(results)[0]])


if __name__ == '__main__':
    # These 'asserts' using only for self-checking and not necessary
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

    assert most_crucial([
        ['A', 'B'],
        ['B', 'C'],
        ['B', 'D'],
        ['C', 'E'],
        ['D', 'E'],
        ['E', 'F']
    ], {
        'A': 10,
        'C': 15,
        'B': 20,
        'E': 10,
        'D': 15,
        'F': 20}) == ['B'], 'Sixth'

    print('Nobody expected that, but you did it! It is time to share it!')
