## Jacob Hardin
## Triangles
## CSCI 110 Beg. Programming - Python
## This program uses functions to do funny math-type things to find
## all the information about a triangle. It first queries the user to
## give some side lengths. Then, it calculates whether this is a "legal"
## triangle. If the triangle is NOT legal, it says so and ends the program.
## Otherwise, it resolves perimeter, area, and angles in degrees.


import math

## Area function
def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

## Perimeter function
def calculate_perimeter(a, b, c):
    return a + b + c

## Angles function
def calculate_angles(a, b, c):
    angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_c = 180 - angle_a - angle_b
    return angle_a, angle_b, angle_c

## Validity of the triangle
def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

## Asking for inputs - floats!
def main():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

## Start of calculations - starts with validity, then does area, perimeter
## and angles. Prints everything on separate lines.
    if is_valid_triangle(a, b, c):
        area = calculate_area(a, b, c)
        perimeter = calculate_perimeter(a, b, c)
        angles = calculate_angles(a, b, c)
        print("Area of the triangle:", area)
        print("Perimeter of the triangle:", perimeter)
        print("Angles of the triangle (in degrees):")
        print("Angle A:", angles[0], end='°\n')
        print("Angle B:", angles[1], end='°\n')
        print("Angle C:", angles[2], end='°\n')
    else:
        print("The given side lengths do not form a valid triangle.")


if __name__ == "__main__":
    main()