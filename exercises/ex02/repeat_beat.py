"""Repeating a beat in a loop."""

__author__ = "730328302"


# Begin your solution here...
beat_name: str = input("What beat do you want to repeat? ")
repeat_amount: int = int(input("How many times do you want to repeat it? "))
if repeat_amount <= 0:
    print("No beat...")
else:
    count: int = 1
    original_beat_name: str = beat_name
    while count < repeat_amount:
        beat_name = beat_name + " " + original_beat_name
        count = count + 1
    print(beat_name)