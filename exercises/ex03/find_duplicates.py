"""Finding duplicate letters in a word."""

__author__ = "730328302"

inp: str = input("Enter a word: ")

i: int = 0
j: int = i + 1
duplicate: bool = False

while i < len(inp) - 1:
    letter_one: str = inp[i]
    while j < len(inp):
        letter_two: str = inp[j]
        if letter_one == letter_two:
            duplicate = True
            j = len(inp)
        else:
            j = j + 1
    i = i + 1
    j = i + 1

if duplicate is True:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")