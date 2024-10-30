# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
for the classify_triangle function.
"""

import unittest
from triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    """Unit tests for the classify_triangle function."""

    def test_right_triangle_a(self):
        """Test right triangle with sides 3, 4, 5."""
        self.assertEqual(
            classify_triangle(3, 4, 5),
            'Scalene Right',
            '3,4,5 should be a Scalene Right triangle'
        )

    def test_right_triangle_b(self):
        """Test right triangle with sides 5, 12, 13."""
        self.assertEqual(
            classify_triangle(5, 12, 13),
            'Scalene Right',
            '5,12,13 should be a Scalene Right triangle'
        )

    def test_equilateral_triangles(self):
        """Test equilateral triangle with sides 1, 1, 1."""
        self.assertEqual(
            classify_triangle(1, 1, 1),
            'Equilateral',
            '1,1,1 should be Equilateral'
        )

    def test_scalene_triangle(self):
        """Test scalene triangle with sides 7, 8, 9."""
        self.assertEqual(
            classify_triangle(7, 8, 9),
            'Scalene',
            '7,8,9 should be Scalene'
        )

    def test_scalene_triangle_b(self):
        """Test scalene triangle with sides 10, 11, 12."""
        self.assertEqual(
            classify_triangle(10, 11, 12),
            'Scalene',
            '10,11,12 should be Scalene'
        )

    def test_isosceles_triangle_a(self):
        """Test isosceles triangle with sides 5, 5, 8."""
        self.assertEqual(
            classify_triangle(5, 5, 8),
            'Isosceles',
            '5,5,8 should be Isosceles'
        )

    def test_isosceles_triangle_b(self):
        """Test isosceles triangle with sides 5, 8, 5."""
        self.assertEqual(
            classify_triangle(5, 8, 5),
            'Isosceles',
            '5,8,5 should be Isosceles'
        )

    def test_not_a_triangle_a(self):
        """Test invalid triangle with sides 1, 1, 3."""
        self.assertEqual(
            classify_triangle(1, 1, 3),
            'NotATriangle',
            '1,1,3 is not a valid triangle'
        )

    def test_not_a_triangle_b(self):
        """Test invalid triangle with sides 10, 1, 1."""
        self.assertEqual(
            classify_triangle(10, 1, 1),
            'NotATriangle',
            '10,1,1 is not a valid triangle'
        )

    def test_not_a_triangle_c(self):
        """Test invalid triangle with sides 1, 10, 1."""
        self.assertEqual(
            classify_triangle(1, 10, 1),
            'NotATriangle',
            '1,10,1 is not a valid triangle'
        )

    def test_invalid_input_negative(self):
        """Test invalid input with negative side -1, 5, 5."""
        self.assertEqual(
            classify_triangle(-1, 5, 5),
            'InvalidInput',
            '-1,5,5 should be InvalidInput'
        )

    def test_invalid_input_too_large(self):
        """Test invalid input with side greater than 200, 201, 199, 199."""
        self.assertEqual(
            classify_triangle(201, 199, 199),
            'InvalidInput',
            '201,199,199 should be InvalidInput'
        )

    def test_invalid_input_non_integer_a(self):
        """Test invalid input with non-integer value 3.5, 4, 5."""
        self.assertEqual(
            classify_triangle(3.5, 4, 5),
            'InvalidInput',
            '3.5,4,5 should be InvalidInput'
        )

    def test_invalid_input_non_integer_b(self):
        """Test invalid input with non-integer value 'a', 5, 5."""
        self.assertEqual(
            classify_triangle('a', 5, 5),
            'InvalidInput',
            'Non-integer values should return InvalidInput'
        )


if __name__ == '__main__':  # pragma: no cover
    print('Running unit tests')
    unittest.main(verbosity=2)
