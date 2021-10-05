"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730328302"

def test_one_only_evens():
    """A test that has two odds and two evens."""
    assert only_evens([2,4,5,7,]) == [2,4]

def test_two_only_evens():
    """A test that has all even numbers."""
    assert only_evens([12,22,48,128]) == [12,22,48,128]

def test_three_only_evens():
    "A test with no even numbers."
    assert only_evens([5,15,23]) == []

def test_one_sub():
    """A test of the first and last indices."""
    assert sub([10, 20, 30, 40, 50, 60], 0, 5) == [10, 20, 30, 40, 50]

def test_index_two_sub():
    """Testing from the second index to the final index."""
    assert sub([10, 20, 30, 40, 50, 60], 2, 5) == [30, 40, 50]

def test_consecutive_indices_sub():
    "A test using two consecutive indeces."
    assert sub([10, 20, 30, 40, 50, 60], 3, 4) == [40]

def test_negative_index_sub():
    "A test using a negative index."
    assert sub([10, 20, 30, 40, 50, 60], -31, 4) == [10, 20, 30, 40]

def test_empty_list_sub():
    "Testing an empty list."
    assert sub([], 0, 5) == []

def test_use_concat():
    """Testing two simple lists."""
    assert concat([10, 20, 30, 40, 50, 60], [1, 2, 3, 4, 5, 6]) == [10, 20, 30, 40, 50, 60, 1, 2, 3, 4, 5, 6]

def test_duplicate_list_concat():
    """Testing two identical lists."""
    assert concat([23, 21, 15, 25, 12], [23, 21, 15, 25, 12]) == [23, 21, 15, 25, 12, 23, 21, 15, 25, 12]

def test_list_a_empty_concat():
    """Testing function when list a is empty."""
    assert concat([], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_list_b_empty_concat():
    """Testing function when list b is empty."""
    assert concat([1, 2, 3, 4, 5], []) == [1, 2, 3, 4, 5]