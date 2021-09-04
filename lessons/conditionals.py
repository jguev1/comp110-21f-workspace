"""An example of conditional if-else statements"""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly")
    print("have a good day")
else: 
    print("sorry u wrong")
    if guess > SECRET:
        print("too high!")
    else:
        print("too low")
    print("try again")


print("Game over.")
