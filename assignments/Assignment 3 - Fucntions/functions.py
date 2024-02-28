## Jacob Hardin
## Functions - Math
## CSCI 110 Beg. Programming - Python
## This program does math based on user inputs


## Import math - I only use this for square roots, as I'd rather not
## figure out how to do that using the base python functuins.
import math


## Addition
def addition(a, b):
    add = a + b
    return add

## Subtraction
def subtraction(a, b):
    sub = a - b
    return sub

## Multiplication
def multiply(a, b):
    mult = a*b
    return mult


## Division AND Modulo
def division(a, b):
    div = round(a / b, 3)
    mod = round(a % b, 3)
    return div, mod

## Exponents
def exponent(a, b):
    exp = round(a**b, 3)
    return exp

## Square roots
def sqrt(a, b):
    roota = round(math.sqrt(a), 3)
    rootb = round(math.sqrt(b), 3)
    return roota, rootb

## Finds the larger of two numbers
def isLarger(a, b):
    if a > b:
        return "The first number is larger."
    elif a < b:
        return "The second number is larger."
    else:
        return "Both are the same!"

def test():
    assert addition(3, 3), 6
    assert addition(4, 7), 11
    assert subtraction(3, 2), 1
    assert subtraction(99, 88), 11
    assert multiply(3, 2), 6
    assert multiply(22, 22), 484
    assert division(3, 1), [3, 0]
    assert division(20, 3), [6.667, 2]
    assert exponent(3, 3), 27
    assert exponent(20, 4), 160000
    assert sqrt(9, 4), [3, 2]
    assert sqrt(9801, 36), [99, 6]
    assert isLarger(9, 3), 9
    assert isLarger(1, 2), 2
## Main Function
## Asks for two numbers, then prints all of the above defined functions.
def main():
   a = float(input("Please enter a number: ")) # Asks for number 1
   b = float(input("Please enter another number: ")) #Asks for number 2
   print("The two numbers provided add up to: ", addition(a, b))
   print("The difference between the two numbers provided is: ", subtraction(a,b))
   print("The two numbers provided multiply together to make: ", multiply(a, b))
   print("The division and remainder of the two numbers is: ", division(a, b))
   print("The first number raised to the second number is: ", exponent(a, b))
   print("The square root of each numer is: ", sqrt(a, b))
   print(isLarger(a, b))


## Sets a loop. If user inputs anything other than "yes", program ends.
test()
if __name__ == "__main__":
    while True:
        main()
        another = input(r'Another one? yes/no: ').lower()
        if another == "yes" or another == "y":
            continue
        else:
            break