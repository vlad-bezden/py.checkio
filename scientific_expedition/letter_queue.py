"""Letter Queue

    https://py.checkio.org/mission/letter-queue/solve/


    In computer science, a queue is a particular kind of data type in which
    the entities in the collection are kept in order and the principal
    operations on the collection are the addition of entities to the
    rear terminal position (enqueue or push), and removal of entities
    from the front terminal position (dequeue or pop).
    This makes the queue a First-In-First-Out (FIFO) data structure.
    In a FIFO data structure, the first element added to the queue
    will be the first one to be removed. This is equivalent to the
    requirement that once a new element is added, all elements that
    were added before have to be removed before the new element can be removed.

    We will emulate the queue process with Python.
    You are given a sequence of commands:
    - "PUSH X" -- enqueue X, where X is a letter in uppercase.
    - "POP" -- dequeue the front position. if the queue is empty, then do nothing.
    The queue can only contain letters.

    You should process all commands and assemble letters which remain in the
    queue in one word from the front to the rear of the queue.

    Let's look at an example, here’s the sequence of commands:
    ["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]

    Command	Queue	Note
    PUSH A	A	    Added "A" in the empty queue
    POP		        Removed "A"
    POP		        The queue is empty already
    PUSH Z	Z
    PUSH D	ZD
    PUSH O	ZDO
    POP	    DO
    PUSH T	DOT	    The result

    Input: A sequence of commands as a list of strings.
    Output: The queue remaining as a string.

    Example:
    letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT"
    letter_queue(["POP", "POP"]) == ""
    letter_queue(["PUSH H", "PUSH I"]) == "HI"
    letter_queue([]) == ""

    Precondition:
    0 ≤ len(commands) ≤ 30;
    all(re.match("\APUSH [A-Z]\Z", c) or re.match("\APOP\Z", c) for c in commands)
"""

from typing import List


def letter_queue(commands: List[str]) -> str:
    queue = []
    for c in commands:
        if c.startswith("PUSH"):
            queue.append(c[-1])
        elif queue:
            queue.pop(0)
    return "".join(queue)


if __name__ == "__main__":
    assert (
        letter_queue(
            ["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]
        )
        == "DOT"
    ), "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"

    print("PASSED!!!")
