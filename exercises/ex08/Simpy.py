"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730328302"


class Simpy:
    """Simple version of Numpy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializing simpy object."""
        self.values = values

    def __str__(self) -> str:
        """String rep of a simpy."""
        return f"Simpy({self.values})"

    def fill(self, value_filled: float, times_filled: int) -> None:
        """Fills a simpy's value with a float repeating a designated amount of times."""
        a_list: list[float] = []
        for i in range((times_filled)):
            a_list.append(value_filled)
        self.values = a_list
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Creates list based off of start, stop and step parameters."""
        assert step != 0.0
        a_list: list[float] = []
        mutatable_value: float = start
        while abs(mutatable_value) <= abs(stop - step):
            a_list.append(mutatable_value)
            mutatable_value += step
        self.values = a_list

    def sum(self) -> float:
        """Sums up all values in a Simpy."""
        a_list: list[float] = []
        a_list = self.values
        sum_is: float = sum(a_list)
        return sum_is

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Addition overload."""
        sum_is: list[float] = []
        if isinstance(rhs, float) or isinstance(rhs, int):
            left_list: list[float] = self.values
            right_adder: float = rhs
            for i in range(len(left_list)):
                element_is: float = left_list[i] + right_adder
                sum_is.append(element_is)
            result = Simpy(sum_is)
            return result
        else:
            assert len(self.values) == len(rhs.values)
            left_list: list[float] = self.values
            right_list: list[float] = rhs.values
            for i in range(len(left_list)):
                element_is: float = left_list[i] + right_list[i]
                sum_is.append(element_is)
            result = Simpy(sum_is)
            return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponential overload."""
        product_is: list[float] = []
        if isinstance(rhs, float) or isinstance(rhs, int):
            left_list: list[float] = self.values
            right_power: float = rhs
            for i in range(len(left_list)):
                element_is: float = left_list[i] ** right_power
                product_is.append(element_is)
            result = Simpy(product_is)
            return result
        else:
            assert len(self.values) == len(rhs.values)
            left_list: list[float] = self.values
            right_list: list[float] = rhs.values
            for i in range(len(left_list)):
                element_is: float = left_list[i] ** right_list[i]
                product_is.append(element_is)
            result = Simpy(product_is)
            return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload for ==."""
        if isinstance(rhs, float) or isinstance(rhs, int):
            bool_list: list[bool] = []
            left_list: list[float] = self.values
            right_mask: float = rhs
            for i in range(len(left_list)):
                element_is: bool = left_list[i] == right_mask
                bool_list.append(element_is)
            result = bool_list
            return result
        else:
            assert len(self.values) == len(rhs.values)
            bool_list: list[bool] = []
            left_list: list[float] = self.values
            right_list: list[float] = rhs.values
            for i in range(len(left_list)):
                element_is: bool = left_list[i] == right_list[i]
                bool_list.append(element_is)
            result = bool_list
            return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload for greater than sign >."""
        bool_list: list[bool] = []
        if isinstance(rhs, float) or isinstance(rhs, int):
            left_list: list[float] = self.values
            right_mask: float = rhs
            for i in range(len(left_list)):
                element_is: bool = left_list[i] > right_mask
                bool_list.append(element_is)
            result = bool_list
            return result
        else:
            assert len(self.values) == len(rhs.values)
            left_list: list[float] = self.values
            right_list: list[float] = rhs.values
            for i in range(len(left_list)):
                element_is: bool = left_list[i] > right_list[i]
                bool_list.append(element_is)
            result = bool_list
            return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adding index operator."""
        left_list: list[float] = self.values
        masked_list: list = []
        masked_Simpy: Simpy = Simpy([])
        if isinstance(rhs, int):
            index: int = rhs
            return left_list[index]
        elif isinstance(rhs, list):
            for i in range(len(left_list)):
                if rhs[i] is True:
                    masked_list.append(left_list[i])
                masked_Simpy = Simpy(masked_list)
        return masked_Simpy