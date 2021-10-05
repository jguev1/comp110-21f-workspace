"""Drawing forests in a loop."""

__author__ = "730328302"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
constant_tree: str = '\U0001F332'

i: int = 1
j: int = 1

while i <= depth:
    print(TREE)
    TREE = TREE + constant_tree
    i = i + 1