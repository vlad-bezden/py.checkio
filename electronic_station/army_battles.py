"""
In the previous mission - Warriors - you've learned how to make a duels between 2 warriors happen.
Great job! But let's move to something that feels a little more epic - the armies!
In this mission your task is to add new classes and functions to the existing ones.
The new class should be the Army and have the method add_units() -
for adding the chosen amount of units to the army.
Also you need to create a Battle() class with a fight() function, which will determine the strongest army.

The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the
first warrior of the second army.
As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel,
and the surviving warrior continues to fight with his current health.
This continues until all the soldiers of one of the armies die.
In this case, the battle() function should return True, if the first army won, or False,
if the second one was stronger.

Input: The warriors and armies.
Output: Theresult of the battle (True or False).
Precondition: 2 types of units
"""

from itertools import cycle, permutations
from typing import Union
from collections import deque


class Warrior:
    def __init__(self, health: int=50, attack: int=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Army(deque):
    def add_units(self, type: Union[Warrior, Knight], amount: int) -> None:
        for _ in range(amount):
            self.append(type())


class Battle:
    def fight(self, army_1: Army, army_2: Army) -> bool:
        try:
            soldier_1 = army_1.popleft()
            soldier_2 = army_2.popleft()
            while True:
                soldier_1_alive = fight(soldier_1, soldier_2)
                if soldier_1_alive:
                    soldier_2 = army_2.popleft()
                else:
                    soldier_1 = army_1.popleft()
        except IndexError as ex:
            pass

        return soldier_1_alive


def fight(unit_1: Union[Warrior, Knight], unit_2: Union[Warrior, Knight]) -> bool:

    for x, y in cycle(permutations((unit_1, unit_2))):
        if x.is_alive and y.is_alive:
            y.health -= x.attack
        else:
            break

    return unit_1.is_alive


if __name__ == "__main__":
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is True
    assert battle.fight(army_3, army_4) is False
    print("Coding complete? Let's try tests!")
