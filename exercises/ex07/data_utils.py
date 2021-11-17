"""Utility functions."""

__author__ = "730328302"

from csv import DictReader
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
    if rows > len(a):
        rows -= (rows - len(a))
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



