# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    # Test right triangles
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 should be a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 should be a Right triangle')

    # Test equilateral triangle
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be Equilateral')

    # Test scalene triangle
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(7, 8, 9), 'Scalene', '7,8,9 should be Scalene')
    
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene', '10,11,12 should be Scalene')

    # Test isosceles triangle
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles', '5,5,8 should be Isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(5, 8, 5), 'Isosceles', '5,8,5 should be Isosceles')

    # Test invalid triangles (triangle inequality violation)
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', '1,1,3 is not a valid triangle')
    
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(10, 1, 1), 'NotATriangle', '10,1,1 is not a valid triangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(1, 10, 1), 'NotATriangle', '1,10,1 is not a valid triangle')

    # Test invalid inputs (negative numbers)
    def testInvalidInputNegative(self):
        self.assertEqual(classifyTriangle(-1, 5, 5), 'InvalidInput', '-1,5,5 should be InvalidInput')

    # Test invalid inputs (sides greater than 200)
    def testInvalidInputTooLarge(self):
        self.assertEqual(classifyTriangle(201, 199, 199), 'InvalidInput', '201,199,199 should be InvalidInput')

    # Test invalid inputs (non-integer values)
    def testInvalidInputNonIntegerA(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput', '3.5,4,5 should be InvalidInput')

    def testInvalidInputNonIntegerB(self):
        self.assertEqual(classifyTriangle('a', 5, 5), 'InvalidInput', 'Non-integer values should return InvalidInput')

if __name__ == '__main__':
    # Customize the test result display
    class CustomTestRunner(unittest.TextTestRunner):
        def run(self, test):
            result = super().run(test)
            if result.wasSuccessful():
                print("\nAll tests passed successfully!")
            else:
                print("\nSome tests failed.")
                for failure in result.failures:
                    print(f"Test {failure[0]} failed: {failure[1]}")
            return result
    
    print('Running unit tests')
    unittest.main(testRunner=CustomTestRunner(verbosity=2))  