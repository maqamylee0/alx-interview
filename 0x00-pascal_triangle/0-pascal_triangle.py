#!/usr/bin/python3
"""
    scripts calculates pascal triangle using recursion
"""

def generate_row(row_number, prev_row):
    """method generates row in the triangle"""
    if row_number == 0:
        return [1]
    elif row_number == 1:
        return [1, 1]
    else:
        row = [1]  # First element of each row is always 1
        for i in range(1, row_number):
            row.append(prev_row[i - 1] + prev_row[i])
        row.append(1)  # Last element of each row is always 1
        return row
def pascal_triangle(n, current_row=0, triangle=None):
    """method calculates pasacl triangle to n levels"""
    if n <= 0:
        return []

    if triangle is None:
        triangle = []

    if current_row == n:
        return triangle

    row = generate_row(current_row, triangle[-1] if triangle else [])
    triangle.append(row)
    
    return pascal_triangle(n, current_row + 1, triangle)
