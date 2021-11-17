"""Utility functions."""

__author__ = "730328302"

from csv import DictReader
from typing import Union
# Define your functions below

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a hanfle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Read that file (prepare to read as CSV rather than just a string)
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close that file when we're done, to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(a: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """A function that produces a column-based table with the first n rows of data from the original table."""
    #if rows > len(a):
        #rows -= (rows - len(a))
    new_dict: dict[str, list[str]] = {}
    i = 0
    for header in a:
        new_dict[header] = []
        while i < rows:
            new_dict[header].append(a[header][i])
            i += 1
        i = 0
    return new_dict


def select(table: dict[str, list[str]], wanted_headers: list[str]) -> dict[str, list[str]]:
    """A function that returns a subset of a table based on the headers selected."""
    new_table: dict[str, list[str]] = {}
    for header in table:
        if header in wanted_headers:
            new_table[header] = table[header]
    return new_table


def concat(table_a: dict[str, list[str]], table_b: dict[str, list[str]]) -> dict[str, list[str]]:
    """A function that combines two column-oriented tables."""
    new_table: dict[str, list[str]] = {}
    i: int = 0
    for header in table_a:
        new_table[header] = table_a[header]
    for header in table_b:
        if header not in new_table:
            new_table[header] = table_b[header]
        else:
            for i in range(len(table_b[header])):
                new_table[header].append(table_b[header][i])

    return new_table


def count(a: list[str]) -> dict[str, int]:
    """A function that returns a dictionary with the count."""
    new_dict: dict[str, int]
    new_dict = dict()
    i = 0
    while i < len(a):
        if a[i] in new_dict:
            new_dict[a[i]] += 1
        else:
            new_dict[a[i]] = 1
        i += 1
    return new_dict 


def mean(values: Union[list[str], list[int], list[float]]) -> float:
    """A function that takes a list of str, converts to float, and takes mean."""
    mean_is: float = 0.0
    sum_is: float = 0.0
    int_values: list[int] = []
    for i in range(len(values)):
        int_values.append(int(values[i]))
    
    for i in range(len(values)):
        sum_is += int_values[i]
    mean_is = sum_is / len(int_values)

    return mean_is


def median(values: Union[list[str], list[int]])-> float:
    """A function that takes a list of str, converts to float, and finds median"""
    median_is: float = 0.0
    ordered_ints: list[int] = order(convert_to_int(values))
    ordered_values: list[float] = convert_to_float(ordered_ints)
    if len(values) // 2 == 0:
        median_one_index: int = int((len(values)/2) - 1)
        median_two_index: int = int(len(values)/2)
        median_is = (ordered_ints[median_one_index] + ordered_ints[median_two_index])/2.0
    else:
        median_index: int = int((len(values) - 1) / 2)
        median_is = float(ordered_ints[median_index])
    return median_is


def mode(values: Union[list[str], list[int], list[float]]) -> list[int]:
    """A function that takes a list of str, converts to float, and finds mode"""
    values_as_str: list[str] = []
    values_count_list: list[int] = []
    mode_is: list = []
    for i in range(len(values)):
        values_as_str.append(str(values[i]))
    new_dict: dict = count(values_as_str)
    for key in new_dict:
        values_count_list.append((new_dict[key]))
    highest_count: int = max(values_count_list)
    for key in new_dict:
        if new_dict[key] == highest_count:
            mode_is.append(key)

    return mode_is
    

def min(input: Union[list[int], list[str], list[float]]) -> float:
    """A function that returns the smallest int or float in a list."""
    if isinstance (input, float) == False:
        convert_to_float(input)
    least: float = float(input[0])
    for i in range(len(input)):
        if input[i] <= least:
            least = float(input[i])
    return least


def order(input: list[int]) -> list[int]:
    """Puts a list of values in numerical order"""
    ordered_list: list[int] = []
    input_copy: list = input
    for i in range(len(input)):
        ordered_list.append(int(min(input_copy)))
        input_copy.remove(int(min(input_copy)))
    return ordered_list


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


def std_dev(input: Union[list[int], list[str], list[float]]) -> float:
    """A function that calculates the standard deviation of a list."""
    int_values: list[int] = []
    dev_step_two_list: list[float] = []
    for i in range(len(input)):
        int_values.append(int(input[i]))
    mean_is: float = mean(int_values)
    for i in range(len(int_values)):
        dev_step_two_list.append((int_values[i] - mean_is) ** 2)
    variance_is: float = mean(dev_step_two_list)
    std_dev_is: float = variance_is ** .5
    return std_dev_is


def sum( a_list: list[float]) -> float:
    """A function that adds up all of the values in a list."""
    sum_is: float = 0.0
    for i in range(len(a_list)):
        sum_is += a_list[i]
    return sum_is


def convert_to_float(a_list: Union[list[str], list[int], list[float]]) -> list[float]:
    """A function that converts lists that are not floats into floats."""
    float_list: list[float] = []
    for i in range(len(a_list)):
        float_list.append((float(a_list[i])))

    return float_list


def convert_to_int(a_list: Union[list[str], list[int], list[float]]) -> list[int]:
    """A function that converts lists that are not ints into ints."""
    int_list: list[int] = []
    for i in range(len(a_list)):
        int_list.append((int(a_list[i])))

    return int_list


def r_value(x_list: list[float], y_list: list[float]) -> float:
    """A function that calculates r value"""
    xy: list[float] = []
    x_sq: list [float] = []
    y_sq: list [float] = []

    

    for i in range(len(x_list)):
        xy.append((x_list[i] * y_list[i]))
    for i in range(len(x_list)):
        x_sq.append((x_list[i] ** 2))
    for i in range(len(x_list)):
        y_sq.append((y_list[i] ** 2))

    sigma_x: float = sum(x_list)
    sigma_y: float = sum(y_list)
    sigma_xy: float = sum(xy)
    sigma_x_sq: float = sum(x_sq)
    sigma_y_sq: float = sum(y_sq)
    n: int = len(x_list)

    step_one: float = (n * sigma_xy) - (sigma_x * sigma_y)
    step_two: float = (n * sigma_x_sq) - (sigma_x ** 2)
    step_three: float = (n * sigma_y_sq) - (sigma_y ** 2)
    step_four: float = (step_two * step_three) ** .5
    r_value_is: float = step_one / step_four
    return r_value_is 

   
if __name__ == "__main__":
    deb = convert_to_float(["5", "6", "7", "8"])
    print(deb)


   
    
    



    
