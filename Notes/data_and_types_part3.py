## This is a continuation of data_and_types.py and data_and_types_part2.py.
## Please refer back to those for examples of things.

## max(iterable, ...) or max(num1, num2, num3, ...)
## separators and end 
import string
print("hello world", "text file", "goodgrnjsf", sep= '')

num1 = 32.5
num2 = 30183

print("max = ", max(num1, num2))
print("min = ", min(num1, num2))

## Libraries, woo!
## import libraryName
## from libraryName import func1, func2
## import libraryName as mylib

import math
import random

## degrees = float(input("Enter a number: "))
## numOut = math.cos(degrees*math.pi/180)
## print("cosine = ", numOut)


## Random Number generator guessing game
randumbgame = '''
n = random.randrange(1,10)
guess = int(input("Enter any number between 1 and 10: "))
while n!= guess:
    if guess < n:
        print("Too low!")
        guess = int(input("Guess another number! "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Guess another number! "))
    else:
        break
print("Good job!")
'''
## phrase = "hello world"
## new_phrase = ""
## for c in phrase:
##     if(c not in string.punctuation):
##         new_phrase += c

## print(new_phrase)

