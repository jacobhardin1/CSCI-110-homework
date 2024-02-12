## Functions

import math


## Here are a couple defined functions. 
def main():
    print("hello world.")
    area = calc_area(float(input("Please enter the radius of the circle: ")))
    print("The area of your circle is: ", round(area, 3))

def calc_area(radius):
    area = math.pi * radius **2
    return area




main()