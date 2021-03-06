'''
Node Subnetworks mission in py.checkio.org

Sometimes damaged nodes are unrecoverable. In that case, people that were
connected to the crushed node must migrate to another district while
administration attempts to fix the node.
But if a crushed node disconnects multiple districts from one another,
then the network splits into two sub-networks and every sub-network should
have their own Mayor. And Mayors must use pigeons for mailing between each
other. In that case, when the network is split you don’t need hundreds of
pigeons.
Your mission is to figure out how many Mayors you need to control the entire
city when some nodes are crushed. In other words, you need to figure out how
many sub-networks will be formed after some nodes are crush and not recovered.

Input: Two arguments. Network structure (as list of connections between nodes)
and list of crashed nodes
Output: Int. The amount of sub-networks after crushing nodes.
'''


def subnetworks(net, crushes):
    one_cities = []
    mult_cities = []

    for x in net:
        for y in crushes:
            if y in x:
                x.remove(y)
        if len(x) == 1:
            one_cities.append(x[0])
        elif len(x) > 1:
            mult_cities.append(x)

    return len(mult_cities) + \
        len([x for x in one_cities if x not in sum(mult_cities, [])])


if __name__ == '__main__':
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['B']) == 2, 'First'
    assert subnetworks([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['D', 'F']
    ], ['A']) == 3, 'Second'
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D']) == 1, 'Third'

    print('Done! Check button is waiting for you!')
