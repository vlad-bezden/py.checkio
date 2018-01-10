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


def most_crucial(net, users):
    return ['B']


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

    print('Nobody expected that, but you did it! It is time to share it!')
