#!usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle with n rows.

    Args:
        n (int): Number of rows in the Pascal's triangle.

    Returns:
        list of lists of int: Pascal's triangle represented as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            # Each element (except the first and last) is the sum of the two elements above it in the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    # Test the pascal_triangle function
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)
