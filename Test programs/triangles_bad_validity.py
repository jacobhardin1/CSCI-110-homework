## Jacob Hardin
## Triangles
## CSCI 110 Beg. Programming - Python
## Calculates the perimeter, angles, area, and validity of a triangle,
## given 3 input sides.

## Heron's Formula: √s(s-a)(s-b)(s-c), where s = semi-perimeter,
## and a, b, c = side lengths

## Here's the math library
import math

## a, b, and c are side lengths. They're also floats because angles
## and area can be floats too.
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

## Check if the sides form a valid triangle. As stated in the readme,
## this will never work as expected. Try the numbers 1, 2, and 3
## or 3, 5, and 8
if a + b >= c and a + c >= b and b + c >= a:
    ## Calculate the perimeter
    perimeter = a + b + c

    ## Calculate the semi-perimeter
    s = perimeter / 2

    ## Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    ## Calculate angles using cosine rule
    angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    
    ## Round angles to three decimal places
    angle_a = round(angle_a, 3)
    angle_b = round(angle_b, 3)

    ## angle_c defined in terms of the prior two and ensures 180 degrees.
    angle_c = round(180 - angle_a - angle_b, 3)
    

    ## Printer
    print("Area of the triangle:", area)
    print("Perimeter of the triangle:", perimeter)
    print("Angles of the triangle (in degrees):")
    print("Angle A:", angle_a, end='°\n')
    print("Angle B:", angle_b, end='°\n')
    print("Angle C:", angle_c, end='°\n')
else:
    print("The given side lengths do not form a valid triangle.")

