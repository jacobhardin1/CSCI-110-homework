'''
Written by: Jacob Hardin
Date: 02/16/2024
Program description: 
    https://open.kattis.com/problems/digitswap
    
Algorithm steps:
    1. input a number, which will be 2 digits
    2. make a variable for each digit
    3. print them in opposite order'''

import sys

print("Enter a number: ", file=sys.stderr) # Kattis ignores this

number = input()

num1 = number[0]
num2 = number[1]

print(num2+num1)