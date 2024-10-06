 #Rishika    
import unittest
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral(self):
        try:
            self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
            print("test_equilateral: Passed")
        except AssertionError:
            print("test_equilateral: Failed")

    def test_isosceles(self):
        try:
            self.assertEqual(classify_triangle(3, 3, 5), "Isosceles")
            print("test_isosceles: Passed")
        except AssertionError:
            print("test_isosceles: Failed")

    def test_scalene(self):
        try:
            self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right Triangle")
            print("test_scalene (3, 4, 5): Passed")
        except AssertionError:
            print("test_scalene (3, 4, 5): Failed")
        try:
            self.assertEqual(classify_triangle(5, 6, 7), "Scalene")
            print("test_scalene (5, 6, 7): Passed")
        except AssertionError:
            print("test_scalene (5, 6, 7): Failed")

    def test_right_triangle(self):
        try:
            self.assertEqual(classify_triangle(6, 8, 10), "Scalene and Right Triangle")
            print("test_right_triangle: Passed")
        except AssertionError:
            print("test_right_triangle: Failed")

    def test_invalid_triangle(self):
        try:
            self.assertEqual(classify_triangle(1, 1, 10), "Invalid triangle")
            print("test_invalid_triangle: Passed")
        except AssertionError:
            print("test_invalid_triangle: Failed")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
