#!/usr/bin/python3

"""
This module defines a function `pascal_triangle(n)` that returns a list of lists 
representing Pascal's triangle up to `n` rows.
The function handles edge cases where `n` is less than or equal to 0.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle with `n` rows.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists where each inner list represents a row in Pascal's triangle.

    If `n <= 0`, an empty list is returned.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        row = [1]  # Start the row with [1]

        # Fill in the middle elements of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)  # End the row with [1]
        triangle.append(row)  # Add the row to the triangle

    return triangle


if __name__ == "__main__":
    # Test cases to print the Pascal's triangle for different values of n
    test_cases = [5, 1, 0, 10, 100]

    for n in test_cases:
        print(f"Pascal's triangle for n = {n}:")
        result = pascal_triangle(n)
        for row in result:
            print(row)
        print()  # Print an empty line between test cases
