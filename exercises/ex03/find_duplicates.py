"""Finding duplicate letters in a word."""

__author__ = "730328302"

inp: str = input("Enter a word: ")

i = 0
j= 0
letter_one = 0
letter_two = 1

while i < len(inp) - 1:
    if inp[letter_one] == inp[letter_two]:
        print ("True")
        i= i + 1
        j= j +1
        letter_one = letter_one + 1
        letter_two = letter_two + 1
    else:
        letter_one = letter_one + 1
        letter_two = letter_two + 1
        i = i + 1

if j == 0:
    print ("False")





    

