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
    div = a % b
    return div

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
   print(addition(a, b))
   print(subtraction(a,b))
   print(multiply(a, b))
   print(division(a, b))
   print(exponent(a, b))
   print(sqrt(a, b))

main()