"""Prisoner's Dilemma."""

__author__ = "730328302"

from random import randint
player: str = ""
points: int = 1
points_opponent: int = 1
i: int = 0
round = int
COWBOY: str = "\U0001F920"
SAD_FACE: str = "\U0001F622"
PRISONER: str = "\U000026D3"
QUESTION_MARK: str = "\U0001F914"
BRAIN: str = "\U0001F9E0"


def greet() -> None:
    """A function that greets the player and asks for their name."""
    global player
    player = input("Hello there! What's your name? ")
    print(f"Hi, {player}! Welcome to Prisoner's Dilemma! {PRISONER} {QUESTION_MARK}")
    has_heard: str = str(input(f"Have you ever heard of the Prisoner's Dilemma, {player}? Type 'yes' or 'no' "))
    if has_heard == "yes":
        print(f"Wow smarty {BRAIN}! We'll be doing a simulation of it today")
    else:
        print("It's basically a thought experiment used in Game Theory that shows how two rational actors may make decisions that do not produce the optimal outcome for either actor.")
        print("We'll be doing a simulation of it today!")


def instructions() -> None:
    """Function that explains how the game works."""
    print("You and your opponent, Dave, are each given a coin and put on opposite sides of a magic box.")
    print("When you put a coin in the box, the OTHER player recieves 3 coins.")
    print("So if both of you put a coin in the box, you each leave with a net 2 coins.")
    print("However, both of you have to option to choose NOT to put a coin in the box, unbeknownst to your oppponent.")
    print("if you choose not to put a coin in the box, and your opponent chooses to contribute, you get to keep your coin, and the 3 coins you get from your opponent's contribution.")
    print("They, on the other hand, gave up one of their coins, and gained no coins from you, so they net -1 coins")
    print("If neither one of you contributes, no one gains or loses any coins")
    print("You will play for a random amount of rounds, so you won't know when the last round will take place.")
 

def options() -> None:
    """Function that let's player know what their options are."""
    print("If you wanna contribute, type, \"A\"")
    print("If you wanna cheat, type, \"B\"")
    print("If you wanna quit and see your points(coins), type, \"C\"")


def decision() -> None:
    """A function that asks the player what option they choose, and runs the appropriate function."""
    choice: str = str(input(f"Okay {player}, time to make a choice. What will it be? "))
    global points
    if choice == "A":
        ChoiceA()
    else:
        if choice == "B":
            ChoiceB(points)

        else:
            if choice == "C":
                quit()
            else:
                print("whoops you gotta choose one of the three")
                decision()
        

def quit() -> None:
    """A function that makes loop end, allowing player to quit the game."""
    global i
    i = i + 100


def ChoiceA() -> None:
    """Function that runs through option A."""
    global points
    global points_opponent
    points = points - 1
    points_opponent = points_opponent + 3 
    if Dave() == 0:
        print(f"Dave cheated! No coins for you{SAD_FACE}")
        print(f"Your coins: {points}")
        print(f"Dave's coins: {points_opponent}")
    else:
        points_opponent = points_opponent - 1
        points = points + 3
        print(f"Dave contributed! 2 coins for you{COWBOY}!")
        print(f"Your coins: {points}")
        print(f"Dave's coins: {points_opponent}")

   
def ChoiceB(coins: int) -> int:
    """Function that runs through option B."""
    global points_opponent
    global points
    if Dave() == 0:
        points = coins
        print("Both of you cheated! No coins for anyone {SAD_FACE}")
        print(f"Your coins: {points}")
        print(f"Dave's coins: {points_opponent}")
    else:
        points_opponent = points_opponent - 1
        points = coins + 3
        print("Dave contributed! Sucker!")
        print(f"Your coins: {points}")
        print(f"Dave's coins: {points_opponent}")
        points
    return(coins)


def Dave() -> int:
    """A function that randomly selects opponent's choice."""
    Dave_choice = randint(0, 1)
    if Dave_choice == 0:
        Dave_result = 0
    else:
        Dave_result = 3
    return Dave_result


def loop() -> None:
    """A function that chooses a random number of rounds for the game."""
    round = int(randint(4, 8))
    global i
    i = 0
    while i < round:
        print(f"---Round {(i+1)}---")
        decision()
        i = i + 1
   

def main() -> None:
    """Prisoners dilemma game."""
    greet()
    wants_instructions: str = input("Do you wanna hear the instructions? Type 'yes' or 'no': ")
    if wants_instructions == 'yes':
        instructions()
    else:
        print("Let's get to it")
    print("")
    options()
    loop()
    print("That's game")
    print(f"Thanks for playing, {player}, you ended the game with {points} coins! ")

 
if __name__ == "__main__":
    main()