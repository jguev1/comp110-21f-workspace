"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730328302"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
i: int = int(randint(1, 4))

if i == 1:
    print("Do not do tomorrow what you can do today.")
else:
    if i == 2:
        print("You are on the path to success. Stay on it!")
    else:
        if i == 3: 
            print("Remember that everything happens for a reason!")
        else:
            if i == 4:
                print("Vibe check, turn that frown upside down!!")

print("Now, go spread positive vibes!")