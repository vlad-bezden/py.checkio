"""
In the previous mission - Army battles, you've learned how to make a battle between 2 armies.
But we have only 2 types of units - the Warriors and Knights.
Let's add another one - the Defender. It should be the subclass of the Warrior class
and have an additional defense parameter, which helps him to survive longer.
When another unit hits the defender, he loses a certain amount of his health according to the next formula:
enemy attack - self defense (if enemy attack > self defense). Otherwise, the defender doesn't lose his health.

The basic parameters of the Defender:
health = 60
attack = 3
defense = 2

Input: The warriors and armies.
Output: The result of the battle (True or False).
Precondition: 3 types of units
"""

from itertools import cycle, permutations
from typing import Union
from collections import deque


class Warrior:
    def __init__(self):
        self.health: int = 50
        self.attack: int = 5

    @property
    def is_alive(self):
        return self.health > 0

    def fight(self, enemy: "Warrior") -> None:
        self.health -= enemy.attack


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health: int = 60
        self.attack: int = 3
        self.defence: int = 2

    def fight(self, enemy: Warrior) -> None:
        self.health -= (
            (enemy.attack - self.defence) if enemy.attack > self.defence else 0
        )


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


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
            y.fight(x)
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

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False
    assert fight(bob, mike) is False
    assert fight(lancelot, rog) is True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is False
    assert battle.fight(army_3, army_4) is True
