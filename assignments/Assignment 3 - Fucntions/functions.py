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
    div = a / b
    mod = a % b
    return div, mod

## Exponents
def exponent(a, b):
    exp = a**b
    return exp

## Square roots
def sqrt(a, b):
    roota = math.sqrt(a)
    rootb = math.sqrt(b)
    return roota, rootb


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


## Sets a loop. If user inputs anything other than "yes", program ends.
if __name__ == "__main__":
    while True:
        main()
        another = input(r'Another one? yes/no: ')
        if another == "yes":
            continue
        else:
            break