## Jacob Hardin
## Numbers, strings, etc
## CSCI 110 - Python

## Type functions determine what the class or type of a thing is.
print("Program Beginning")
print("Another line")
print(type(100))
print('"100.0"')


## Variables
variableName = "100"
print(type(variableName))
variableName = int(variableName)
print(type(variableName))

variableNameTwo = 3.74
print(type(variableNameTwo))
print(variableNameTwo*3.12)
## variableNameTwo = int(variableNameTwo)
print(variableNameTwo)

## Escape Sequences
## \n new line; \ backslash; \t tab; \r carriage return;
## \' single quote; \" double quote
## Triple quotes (''') can be used for almost any string

phrase = "'What\'s up\n Shaquille O\'Neill"
phrase3 = "My solution is \r\tbonkered. \n"
phrase2 = '''What's the good news, fam? Here's some triple quotes: \'\'\' '''

print(phrase)
print(phrase2)
print(phrase3)

## Variables cannot be keywords
## Always start with a letter, usually undercase
## Each word after the first is camelCase
## Type of variable is dynamic

## Numeric computation
## * asterisk is multiply
## + - / * basic operations
## integer division is // e.g. 10//3
## Remainder/modulus is % eg 10%3
## exponents are 2 asterisks (**)
## ^ symbol is for XOR operations.

time = 111
hours = time//60
minutes = time%60
print(hours, ":", minutes)

print("2 to the 3rd power is: ", 2**3)
print("2 XOR 3 is: ", 2^3)

## Order of operations, PEMDAS
## Paretheses
## Exponents
## Multiply
## Add
## Subtract
## If in doubt - USE PARETHESES

x = 3
y = 4
z = 5

print(3*x+y*z)
print(3*x, y*z)

fname = "John"
lname = "Doe"
fullName = fname + ' ' + lname + ' '
print(fullName * 10)

## Standard input

name = input("What is your name? ")
name = name + " "
print(name)

name_times = int(input('Enter how many times to print your name: '))

print(name * name_times)

next_line = name + "repeated " + str(name_times) + " times."
print(next_line)
