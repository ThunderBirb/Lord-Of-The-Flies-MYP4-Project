import time
import sys

PeopleList = ["Piggy", "Ralph", "Jack", "Roger", "Samneric"]

ValueTable = {
    "Spear":2,
    "Face paint":2,
    "Glasses":3,
    "Boulder":4,
    "Castle rock":5
}

ItemTable =  {
    "Spear":"Increased chance to aggravate",
    "Face paint":"Lower chance to be recognized",
    "Glasses":"Bargaining tool",
    "Boulder":"Deadly weapon, be cautious",
    "Castle rock":"Height advantage for user(s)"
}

class Piggy:
    name = "Piggy"
    strengths = ["Has his glasses", "Smart"]
    weaknesses = ["Asthma", "Relies on glasses"]
    held = ["Glasses"]
    relations = {
        "Ralph": 1,
        "Jack": 2,
        "Roger": 3,
        "Samneric": 4
    }

class Ralph:
    name = "Ralph"
    strengths = ["Athletic", "Good Charisma", "Leader"]
    weaknesses = ["Bad with important decisions", "Fears a lot of things"]
    held = ["Bad with important decisions", "Fears a lot of things"]
    relations = {
        "Piggy": 1,
        "Jack": 2,
        "Roger": 3,
        "Samneric": 4
    }
class Jack:
    name = "Jack"
    strengths = ["brave", "Leader of the hunters"]
    weaknesses = ["Fragile ego", "Overconfident"]
    held = []
    relations = {
        "Piggy": 1,
        "Ralph": 2,
        "Roger": 3,
        "Samneric": 4
    }

class Roger:
    name = "Roger"
    strengths = ["Good with weapons"]
    weaknesses = ["Isolation"]
    held = []
    relations = {
        "Piggy": 1,
        "Ralph": 2,
        "Jack": 3,
        "Samneric": 4
    }

class Samneric:
    name = "Samneric"
    strengths = ["Civilised", "Reasonable"]
    weaknesses = ["Easily intimidated"]
    held = []
    relations = {
        "Piggy": 1,
        "Ralph": 2,
        "Jack": 3,
        "Roger": 4
    }

def Choice(person, text="What would you like to do?", choices=[]):
    print(text)
    for x in choices:
        print(f"{choices.index(x)+1}. {x}") #Lists the choices
    
    while True:
        choice = input("Number: ")
        try:
            choice = int(choice)
        except:
            print("That is not a valid answer, please answer again with a number")
        else:    
            if choice <= len(choices) and choice > 0:
                break
            print("That is not a valid answer, please answer again with a number")

    print("") #just adding space after line
    return choice

def ShowPersonInfo(person):    
    p = person

    print(f"Name: {p.name}")
    print(f"Held: {p.held}")
    print(f"Strengths: {p.strengths}")
    print(f"Weaknesses: {p.weaknesses}")
    print("Relations:")
    for x in p.relations:
        print(f"{x} = {p.relations[x]}") #printing the data in rows


#CODE TESTING AREA

#ShowPersonInfo(Ralph)

#Choice(Piggy, "What would you like to do", ["Sleep", "Take a bath", "Eat", "Trade"])

#Choice(Piggy, choices=["sell", "Destroy", "Eat"])



#MAIN AREA FOR RUNNING CODE
while True: #starting the main game loop
    print("Weclome to, Let's try... diplomacy!")
    time.sleep(1)
    print("This game is designed by Lila, Thomas, Thor, Viki and Zayan, and coded by Thor \n")
    time.sleep(3)
    print("This game is based on the book Lord Of The Flies written by William Golding")
    time.sleep(3)
    print("Your ojective in this game is to get the best outcome for your side")
    time.sleep(3)
    while True:
        print("Who would you like to play as?:")
        for x in ["Piggy", "Ralph", "Jack", "Roger", "Samneric"]:
            print(f"{PeopleList.index(x)+1}. {x}")
        PlayerChar = input("Number:")
        if PlayerChar == "1":
            PlayerChar = Piggy
            break
        elif PlayerChar == "2":
            PlayerChar = Ralph
            break
        elif PlayerChar == "3":
            PlayerChar = Jack
            break
        elif PlayerChar == "4":
            PlayerChar = Roger
            break
        elif PlayerChar == "5":
            PlayerChar = Samneric
            break
        else:
            print("That is not a valid answer, please answer again with a number")
    

    break #TEMPORARY SAFESTOP