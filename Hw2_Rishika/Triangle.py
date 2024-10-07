def classifyTriangle(a, b, c):
    # Step 1: Input validation
    # Check if all inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    
    # Check if inputs are positive and less than or equal to 200
    if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    # Step 2: Check for Not a Triangle (Triangle Inequality Theorem)
    # The sum of the lengths of any two sides must be greater than the third side
    if (a + b <= c) or (b + c <= a) or (c + a <= b):
        return 'NotATriangle'
    
    # Step 3: Classify the triangle
    # Check if the triangle is equilateral (all sides are equal)
    if a == b == c:
        return 'Equilateral'
    
    # Check if the triangle is a right triangle (Pythagoras theorem)
    # Sort the sides to easily apply the theorem: a^2 + b^2 = c^2
    sides = sorted([a, b, c])  # Sorting helps easily compare the largest side (c)
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return 'Right'
    
    # Check if the triangle is isosceles (two sides are equal)
    if a == b or b == c or c == a:
        return 'Isosceles'
    
    # If none of the above, the triangle is scalene (all sides are different)
    return 'Scalene'
