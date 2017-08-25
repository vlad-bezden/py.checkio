'''Node Disconnected Users mission from check.io

Welcome to the GridLand.
All the citizens here are connected through the global internal network
because the main way for communication here is via email.
Every new district of the city starts with building a node – center of the
district. All the citizens will be connected to this node in order to send and
receive emails. All nodes of GridLand are connected so one node can send
emails between connected nodes. In such a way, no matter how big the city is
all users can send messages between each other as long as all of the nodes are
connected.

The Mayor of GridLand is using this network to quickly send emergency emails
to all citizens when necessary. But the system is not perfect.
When one of city nodes gets crushed it may leave the citizens of this node
district disconnected from these emergency emails. It may also leave districts
around the crushed node disconnected if their nodes do not have other ways to
connect. To resolve this occurrence, the Mayor uses mail-pigeons – an old
method of sending mail that was invented before the global internal network.
All of the connected citizens still connected to the network received the
emergency emails, but the disconnected citizens receive their from these
pigeons.

Your mission is to figure out how many pigeons you need when some of the
nodes are crushed.

Input: Four arguments. Network structure
(as list of connections between nodes), users on each node
(as dict where keys are node-name and values are amount of users),
name of node that sends email, list of crashed nodes.

Output: Int. Amount of users that wouldn't receive an email.
'''


def build_graph(net, source, crushes):
    '''Creates graph all connected points'''

    graph = {}

    for node1, node2 in (edge for edge in net
                         if edge[0] not in crushes and edge[1] not in crushes):
        node = graph.get(node1, [])
        if not node:
            graph[node1] = node
        node.append(node2)
    return graph


def find_connected_nodes(graph, source):
    '''Finds all nodes that connected with source'''

    processed = [source]
    if source in graph:
        to_process = graph[source]
        while to_process:
            node = to_process.pop()
            if node not in processed:
                processed.append(node)
                if node in graph:
                    to_process.extend(graph[node])
    return set(processed)


def find_disconnected_nodes(net, connected_with_source):
    '''Finds all disconnected nodes'''

    all_nodes = {node for edge in net for node in edge}
    return all_nodes.difference(connected_with_source)


def disconnected_users(net, users, source, crushes):
    graph = build_graph(net, source, crushes)
    connected_with_source = find_connected_nodes(graph, source)
    disconnected_nodes = find_disconnected_nodes(net, connected_with_source)
    return sum(users[node] for node in disconnected_nodes)


if __name__ == '__main__':
    # These 'asserts' using only for self-checking and not necessary for
    # auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, 'First'

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, 'Second'

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, 'Third'

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'C': 30,
        'B': 20,
        'D': 40
    },
        'A', ['A']) == 100, 'Forth'
