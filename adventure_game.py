import time

import random

places = ["an open field", "a forest", "a dry swamp"]

weapons = ["Sword", "Bow with Arrows", "Big Knife",
           "Thor's Battle Axe !!", "nothing",
           "Elder Wand and knowledge of the spell of Avada Kedavra"]

villains = ["An ogre", "An ugly bear", "A bad Witch", "A bad fairy"]

place = random.choice(places)
villain = random.choice(villains)
weapon = random.choice(weapons)

# Let's write the needs of our Game


def replay():
    replay = input("Wanna play again ?\n"
                   "Please anwser with y or n.\n")
    if replay == "y":
        field()
    elif replay == "n":
        return(printPause("OK, goodbye."))
    else:
        printPause("Please anwser with y or n.")
        replay()


def printPause(message):
    print(message)
    time.sleep(2)


def cave():
    printPause("You entering the cave and you can't see anything..")
    printPause("You saw a little "
               "shine light..")
    printPause("You reached the source of that little "
               "shiny light and it's a closed box")
    printPause("You opened the box and found " + weapon)
    printPause("You take ur weapon and go outside the cave")
    printPause("Which way do you want to go?\n")
    field()


def shanty():
    printPause("You are on the way to the shanty now..")
    printPause("You reached it and knock on the door of it..")
    printPause(villain + " opened the door and decided to attack u\n")
    reaction = int(input("What u will do now ?\n"
                         "1.Running away\n"
                         "2.Fighting the villain\n"
                         "Please enter 1 or 2 only.\n"))
    if reaction == 1:
        printPause("You running back..")
        printPause("Now What ?")
        field()
    elif reaction == 2:
        printPause("You decided to fight the villain with ur " + weapon + "\n")
        if weapon == "nothing":
            printPause("Ur bare hands r weak and u can't defeat the villain\n"
                       "U have been defeated !!\n")
            printPause("GAME OVER\n")
            replay()
        elif weapon != "nothing":
            printPause("Ur weapon is powerful and u defeated the villain")
            printPause("U beat the villain and save "
                       "the people around the " + place)
            printPause("U r VICTORIOUS")
            replay()
    else:
        printPause("Please enter 1 or 2 only.\n")


def field():
    choice = int(input("Enter 1 to go to the shanty.\n"
                       "Enter 2 to peer into the cave.\n"
                       "Please enter 1 or 2.\n"))
    if choice == 1:
        shanty()
    elif choice == 2:
        cave()
    else:
        printPause("Please enter 1 or 2.\n")
        field()


def play():
    printPause("You find yourself in " + place)
    printPause("In front of you are two passageways. one of them "
               "to a cave and the another one to an alone shanty")
    printPause("Which way do you want to go?")
    field()


# All the line before this made for making our game runs perfectly
# This is the Main lines of program which runs the Game

play()

# Made with Love
# All rights reserved to Omar Yehia Tawfeek
