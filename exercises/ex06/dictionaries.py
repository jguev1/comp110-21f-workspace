"""Practice with dictionaries."""

__author__ = "730328302"


def invert(a: dict[str, str]) -> dict[str, str]:
    """A function that inverts key-value pairings in a dictionary."""
    a_list: list[str] = []
    for key in a:
        a_list.append(a[key])
    c = count(a_list)
    b: dict[str, str] = {}
    for keys in c:
        if c[keys] == 1:
            new_dict = {}
            for keys in a:
                new_dict[(a[keys])] = keys
                b = new_dict   
        else:
            raise KeyError("bleh")
    return b         
    
             
def favorite_color(a: dict[str, str]) -> str:
    """A function that returns the color that appears the most."""
    a_list: list[str] = []
    for key in a:
        a_list.append(a[key])
    b = count(a_list)
    highest_int = 0
    favorite = ""
    for key in b:
        if b[key] > highest_int:
            highest_int = b[key]
            favorite = key
    return favorite


def count(a: list[str]) -> dict[str, int]:
    """A function that returns a dictionary with the count."""
    new_dict: dict[str,int]
    new_dict = dict()
    i = 0
    while i < len(a):
        if a[i] in new_dict:
            new_dict[a[i]] += 1
        else:
            new_dict[a[i]] = 1
        i += 1
    return new_dict 