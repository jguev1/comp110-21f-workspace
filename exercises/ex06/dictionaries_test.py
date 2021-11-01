"""Unit tests for dictionary functions."""
from exercises.ex06.dictionaries import invert, favorite_color, count


__author__ = "730328302"


def test_invert_basic():
    """A test for a basic dictionary with 3 entries."""
    names = {"Jose": "David",
             "Evan": "Maxwell",
             "Xan": "Der"}
    assert invert(names) == {"David": "Jose", "Maxwell": "Evan", "Der": "Xan"}


def test_invert_empty():
    """A test for an empty dictionary."""
    empty = {}
    assert invert(empty) == {}


def test_invert_same_name():
    """A test for a dictionary with the same key and value."""
    names = {"Jose": "Jose"}
    assert invert(names) == {"Jose": "Jose"}


# def test_invert_duplicate_keys():
#     """A test to make sure there will be no duplicate keys."""
#     names = {'Joe': 'Jonas', 'Nick': 'Jonas'}
#     assert invert(names) == KeyError("bleh")


def test_favorite_basic():
    """Testing for a simple case."""
    names: dict[str, str] = {"Jose": "Blue", "Jesus": "Orange", "Oscar": "Red", "Sarah": "Orange", "Evan": "Blue", "Emma": "Blue"}
    assert favorite_color(names) == "Blue"


def test_favorite_tie():
    """Test that in case of a tie, the first value stated is the one printed."""
    names: dict[str, str] = {"Jose": "Orange", "Jesus": "Orange", "Oscar": "Red", "Sarah": "Orange", "Evan": "Blue", "Emma": "Blue", "Nik": "Blue"}
    assert favorite_color(names) == "Orange"


def test_favorite_single():
    """A test for a dictionary with a single value."""
    names = {"Jose": "Blue"}
    assert favorite_color(names) == "Blue"


def test_count_basic():
    """Testing to see if counts are correct."""
    colors = ["Blue", "Green", "Green", "Red", "Green", "Orange", "Orange", "Orange", "Blue"]
    assert count(colors) == {"Blue": 2, "Green": 3, "Red": 1, "Orange": 3}


def test_count_simple():
    """Another simple count."""
    colors = ["Blue", "Blue", "Blue"]
    assert count(colors) == {"Blue": 3}


def test_count_single():
    """Testing for a single value."""
    colors = ["Blue"]
    assert count(colors) == {"Blue": 1}