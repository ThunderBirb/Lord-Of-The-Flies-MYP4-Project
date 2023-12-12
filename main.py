import time
import sys

ValueTable = {
    "A": 1,
    "B": 2,
    "C": 3
}


class Piggy:
    strengths = ["Has his glasses", "Smart"]
    weaknesses = ["Asthma", "Relies on glasses"]
    held = ["Glasses"]
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

class Ralph:
    strengths = ["Athletic", "Good Charisma", "Leader"]
    held = ["Bad with important decisions", "Fears a lot of things"]
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

class Jack:
    strengths = ["brave", "Leader of the hunters"]
    weaknesses = ["Fragile ego", "Overconfident"]
    held = []
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

class Roger:
    strengths = ["Good with weapons"]
    weaknesses = ["Isolation"]
    held = []
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

class Samneric:
    strengths = ["Civilised", "Reasonable"]
    weaknesses = ["Easily intimidated"]
    held = []
    relations = {
        "Name": 0,
        "Name": 0,
        "Name": 0
    }

def Choose(person, text="What would you like to do?", choices=[]):
    print(text)
    for x in choices:
        print(f"{choices.index(x)+1}. {x}")
    
    choice = input("Number: ")
    return choice


Choose(Piggy, "What would you like to dooooo", ["Sleep", "Take a bath", "Eat", "Trade"])

Choose(Piggy, choices=["sell", "Destroy", "Eat"])

