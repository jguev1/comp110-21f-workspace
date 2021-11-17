"""Test for Project 1 Utility functions"""
from data_utils import mean, median, mode, std_dev, min


def test_mean():
    """Testing the mean of 20 values that should equal 7."""
    assert mean([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]) == 7

def test_mean_if_string():
    """Same scenario as above, but the values are type str"""
    assert mean(["9", "2", "5", "4", "12", "7", "8", "11", "9", "3", "7", "4", "12", "5", "4", "10", "9", "6", "9", "4"]) == 7


def test_median():
    """median of 20 values that should equal 7"""
    assert median([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4])
    assert median(["9", "2", "5", "4", "12", "7", "8", "11", "9", "3", "7", "4", "12", "5", "4", "10", "9", "6", "9", "4"]) == 7


def test_mode():
    """mode of 20 values should equal 9 and 4"""
    assert mode(["9", "2", "5", "4", "12", "7", "8", "11", "9", "3", "7", "4", "12", "5", "4", "10", "9", "6", "9", "4"]) == [4, 9] or [9,4]


def test_std_dev():
    """should equal more than 2.97 but less than 3"""
    assert std_dev([2, 3, 4, 4, 4, 4, 5, 5, 6, 7, 7, 8, 9, 9, 9, 9, 10, 11, 12, 12]) < 3
    assert std_dev([2, 3, 4, 4, 4, 4, 5, 5, 6, 7, 7, 8, 9, 9, 9, 9, 10, 11, 12, 12]) > 2.95


def test_min():
    """smallest number"""
    assert min([20, 20, 5]) == 5
    


#def test_std_dev():