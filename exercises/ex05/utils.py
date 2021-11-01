"""List utility functions part 2."""

__author__ = "730328302"


def only_evens(a: list[int]) -> list[int]:
    """A function that returns even numbers from a list of ints."""
    b: list[int] = []
    for number in a:
        if number % 2 == 0:
            b.append(number)
    return b


def sub(input_list: list[int], start_index: int, end_index: int) -> list[int]:
    """A function that returns a subset of a list between given indexes."""
    new_list: list[int] = []
    i = start_index
    j = end_index
    if start_index < 0:
        i += -start_index
    if end_index > len(input_list):
        dif = j - len(input_list)
        j = j - dif
        j -= (len(input_list) - j)
    if len(input_list) == 0 or start_index >= len(input_list) or end_index < 0:
        return new_list
    else:
        while i < j:
            new_list.append(input_list[i])
            i += 1
    return new_list


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """A function that concatenates two lists in order."""
    list_prime: list[int] = []
    for integer in list_a:
        list_prime.append(integer)
    for integer in list_b:
        list_prime.append(integer)
    return list_prime