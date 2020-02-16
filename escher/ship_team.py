"""The Ship Team.

You have to divide all your crew members into 2 teams with the next rules:
those who are elder than 40 y.o. or younger than 20, should be on the first ship
and all the others - on the second. It will helps the young sailors gain the experience
of the elder collegues.

The input data will be the dictionary where keys will be the surnames
of the sailors and the values will be their ages. After the crew formating,
you should sort all of the sailors in the alphabetical order in the
each list of surnames.

Input: Dictionary with the sailors and their ages.
Output: List of the lists with 2 teams.

Precondition:
1 <= amount of the sailors <= 100
"""

from typing import Dict, List

Sailors = Dict[str, int]


def two_teams(sailors: Sailors) -> List[List[str]]:
    teams = [[], []]
    for name, age in sorted(sailors.items()):
        teams[20 <= age <= 40].append(name)
    return teams


if __name__ == "__main__":
    assert two_teams({"Smith": 34, "Wesson": 22, "Coleman": 45, "Abrahams": 19}) == [
        ["Abrahams", "Coleman"],
        ["Smith", "Wesson"],
    ]

    assert two_teams({"Fernandes": 18, "Johnson": 22, "Kale": 41, "McCortney": 54}) == [
        ["Fernandes", "Kale", "McCortney"],
        ["Johnson"],
    ]

    assert two_teams({"Carlos": 34, "Richardson": 20, "Dow": 40}) == [
        [],
        ["Carlos", "Dow", "Richardson"],
    ]
    print("PASSED!!!")
