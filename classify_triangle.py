#Rishikaa
def classify_triangle(a, b, c):
    """
    Classifies the type of triangle based on side lengths a, b, and c.

    Parameters:
        a (float): The length of side a.
        b (float): The length of side b.
        c (float): The length of side c.
    Returns:
        str: A string specifying the type of triangle.
    """
    
    # Ensure inputs are valid
    if not (a + b > c and a + c > b and b + c > a):
        return "Invalid triangle"

    # Equilateral Triangle
    if a == b == c:
        return "Equilateral"

    # Isosceles Triangle
    elif a == b or b == c or a == c:
        if round(a**2 + b**2, 5) == round(c**2, 5) or \
           round(b**2 + c**2, 5) == round(a**2, 5) or \
           round(a**2 + c**2, 5) == round(b**2, 5):
            return "Isosceles and Right Triangle"
        return "Isosceles"
    
    # Scalene Triangle
    else:
        if round(a**2 + b**2, 5) == round(c**2, 5) or \
           round(b**2 + c**2, 5) == round(a**2, 5) or \
           round(a**2 + c**2, 5) == round(b**2, 5):
            return "Scalene and Right Triangle"
        return "Scalene"


def main():
    """
    Main function that takes user input and classifies the triangle.
    """
    print("Enter the lengths of the three sides of the triangle:")
    a = float(input("Length of side a: "))
    b = float(input("Length of side b: "))
    c = float(input("Length of side c: "))
    
    # Call the classify_triangle function
    result = classify_triangle(a, b, c)
    
    # Print the result
    print(f"The triangle is: {result}")

# Run the main function
if __name__ == "__main__":
    main()