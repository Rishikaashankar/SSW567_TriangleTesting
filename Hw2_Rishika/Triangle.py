"""
This module provides a function to classify triangles based on side lengths.
"""

def is_right_triangle(a, b, c):
    """
    Checks if the triangle with sides a, b, c is a right triangle.

    Parameters:
    a (int): Length of the first side
    b (int): Length of the second side
    c (int): Length of the third side

    Returns:
    bool: True if the triangle is right, False otherwise
    """
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def classify_triangle(a, b, c):
    """
    Classifies a triangle based on the lengths of its sides.

    Parameters:
    a (int): Length of the first side
    b (int): Length of the second side
    c (int): Length of the third side

    Returns:
    str: Type of triangle (e.g., 'Equilateral', 'Isosceles', 'Scalene', 'Right', or 'NotATriangle')
    """
    # Step 1: Input validation
    if not all(isinstance(side, int) and 0 < side <= 200 for side in [a, b, c]):
        return 'InvalidInput'

    # Step 2: Check for Not a Triangle (Triangle Inequality Theorem)
    if not (a + b > c and b + c > a and c + a > b):
        return 'NotATriangle'

    # Step 3: Classify the triangle
    if a == b == c:
        triangle_type = 'Equilateral'
    elif a == b or b == c or c == a:
        triangle_type = 'Isosceles'
    else:
        triangle_type = 'Scalene'

    # Check if it is also a right triangle
    if is_right_triangle(a, b, c):
        triangle_type += ' Right'

    return triangle_type.strip()
