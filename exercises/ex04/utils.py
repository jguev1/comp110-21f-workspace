"""List utility functions."""

__author__ = "123456789"
 

def all(a_list: list[int], an_int: int) -> bool:
    """A function that checks if a list is made up of a certain integer."""
    i = 0
    if a_list == []:
        return False
    else:
        while i < len(a_list):
            if a_list[i] != an_int:
                return False
            i += 1
        return True


def is_equal(a: list[int], b: list[int]) -> bool:
    """A function that says if two lists are equal."""
    if len(a) != len(b):
        return False
    else:
        i = 0
        while i < len(a):
            if a[i] != b[i]:
                return False
            else:
                i += 1
        return True 


def max(input: list[int]) -> int:
    """A function that returns the greatest int in a list."""
    i = 0
    greatest = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        while i < len(input):
            if input[i] >= greatest:
                greatest = input[i]
            i += 1
        return greatest