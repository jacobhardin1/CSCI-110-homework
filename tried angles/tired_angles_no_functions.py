## Jacob Hardin
## Triangles
## CSCI 110 Beg. Programming - Python
## This program does not use the def keyword, unlike the other file
## in this folder. It first queries the user to give some side lengths.
## Then, it calculates whether this is a "legal" triangle.
## If the triangle is NOT legal, it says so and ends the program.
## Otherwise, it resolves perimeter, area, and angles in degrees.

## Heron's Formula: √s(s-a)(s-b)(s-c), where s = semi-perimeter,
## and a, b, c = side lengths

## This program, given valid side lengths, will return the perimeter,
## area, and angles of the triangle

## Here's the math library
import math

## a, b, and c are side lengths. They're also floats because angles
## and area can be floats too.
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

## Check if the sides form a valid triangle
if a + b > c and a + c > b and b + c > a:
    ## Calculate the perimeter
    perimeter = a + b + c

    ## Calculate the semi-perimeter
    s = perimeter / 2

    ## Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    ## Calculate angles using cosine rule
    angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_c = 180 - angle_a - angle_b

    ## Printer
    print("Area of the triangle:", area)
    print("Perimeter of the triangle:", perimeter)
    print("Angles of the triangle (in degrees):")
    print("Angle A:", angle_a, end='°\n')
    print("Angle B:", angle_b, end='°\n')
    print("Angle C:", angle_c, end='°\n')
else:
    print("The given side lengths do not form a valid triangle.")
