"""
So we have 3 types of units: the Warrior, Knight and Defender.
Let's make the battles even more epic and add another type - the Vampire!
Vampire should be the subclass of the Warrior class and have the additional vampirism parameter,
which helps him to heal himself. When the Vampire hits the other unit,
he restores his health by +50% of the dealt damage (enemy defense makes the dealt damage value lower).

The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%

Input: The warriors and armies.
Output: The result of the battle (True or False).
Precondition: 4 types of units
"""

from itertools import cycle, permutations
from typing import Union, Type
from collections import deque

Soldier = Union["Warrior", "Vampire", "Defender", "Knight"]


class Warrior:
    def __init__(self, health: int = 50, attack: int = 5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, enemy: Soldier) -> None:
        """Hit to the enemy by this object"""
        enemy.loss(self.demage)

    def loss(self, attack: int) -> None:
        self.health -= attack

    @property
    def demage(self) -> int:
        """Demage made by this object"""
        return self.attack


class Vampire(Warrior):
    def __init__(self):
        super().__init__(health=40, attack=4)
        self.vampirism: float = 0.5

    def hit(self, enemy: Soldier):
        enemy.loss(self.attack)
        self.health += (self.attack - enemy.demage) * self.vampirism


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defence: int = 2

    def loss(self, attack: int) -> None:
        self.health -= max(attack - self.defence, 0)


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Army(deque):
    def add_units(self, type: Type[Soldier], amount: int) -> None:
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


def fight(unit_1: Soldier, unit_2: Soldier) -> bool:

    for x, y in cycle(permutations((unit_1, unit_2))):
        if x.is_alive and y.is_alive:
            x.hit(y)
        else:
            break

    return unit_1.is_alive


if __name__ == "__main__":

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

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
    assert fight(eric, richard) is False
    assert fight(ogre, adam) is True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is False
    assert battle.fight(army_3, army_4) is True
    print("Coding complete? Let's try tests!")
