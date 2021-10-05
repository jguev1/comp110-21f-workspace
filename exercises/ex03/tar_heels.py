"""An exercise in remainders and boolean logic."""

__author__ = "730328302"


inp: int = int(input("Enter an int: "))

if inp % 2 == 0 and inp % 7 == 0:
    print("TAR HEELS")
else:
    if inp % 7 == 0:
        print("HEELS")
    else:
        if inp % 2 == 0:
            print("TAR")
        else: 
            print("CAROLINA")