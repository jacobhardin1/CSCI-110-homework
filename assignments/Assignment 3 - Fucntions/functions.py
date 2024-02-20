## Jacob Hardin
## Functions - Math
## CSCI 110 Beg. Programming - Python
## This program does math based on user inputs

import math

def addition(a, b):
    add = a + b
    return add

def subtraction(a, b):
    sub = a - b
    return sub

def multiply(a, b):
    mult = a*b
    return mult

def division(a, b):
    div = a / b
    mod = a % b
    return div, mod

def exponent(a, b):
    exp = a**b
    return exp

def sqrt(a, b):
    roota = math.sqrt(a)
    rootb = math.sqrt(b)
    return roota, rootb

def main():
   a = float(input("Please enter a number: "))
   b = float(input("Please enter another number: "))
   print("The two numbers provided add up to: ", addition(a, b))
   print("The difference between the two numbers provided is: ", subtraction(a,b))
   print("The two numbers provided multiply together to make: ", multiply(a, b))
   print("The division and remainder of the two numbers is: ", division(a, b))
   print("The first number raised to the second number is: ", exponent(a, b))
   print("The square root of each numer is: ", sqrt(a, b))

while True:
    main()
    another = input(r'Another one? yes/no: ')
    if another == "yes":
        continue
    else:
        break