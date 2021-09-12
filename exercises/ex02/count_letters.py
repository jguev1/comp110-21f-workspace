"""Counting letters in a string."""

__author__ = "730328302"

letter_searched: str = input("What letter do you want to look for?: ")
word_entered: str = input("Enter a word: ")

i: int = 0
count: int = 0

while i < len(word_entered):
    if word_entered[i] == letter_searched:
        count = count + 1
    i = i + 1

print("Count: " + str(count))
