import time
import sys

ValueTable = {
    "A": 1,
    "B": 2,
    "C": 3
}

class RTeam:
    held = []
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

class JTeam:
    held = []
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

def Choice(team, text, choices):
    print(text)
    for x in choices:
        print(f"{choices.index(x)+1}. {x}")


Choice(RTeam, "What would you like to do?", ["Sleep", "Take a bath", "Eat", "Trade"])
