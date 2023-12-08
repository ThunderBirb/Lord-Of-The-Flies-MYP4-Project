import time
import sys

ValueTable = {
    "A": 1,
    "B": 2,
    "C": 3
}


class Piggy:
    strengths = ["Has his glasses", "Smart"]
    held = ["Glasses"]
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

class Ralph:
    strengths = ["Athletic", "Good Charisma"]
    held = []
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

class Jack:
    strengths = ["Leader of the hunters"]
    held = []
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

class Roger:
    strengths = ["Good with weapons"]
    held = []
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

class Samneric:
    strengths = ["Civilised", "Reasonable"]
    held = []
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

def Choice(person, text, choices):
    print(text)
    for x in choices:
        print(f"{choices.index(x)+1}. {x}")


Choice(Piggy, "What would you like to do?", ["Sleep", "Take a bath", "Eat", "Trade"])
