## This is a continuation of the file named "data_and_types.py".

## Bitwise

## There are several number system bases.
## binary (base 2, 0 and 1)
## Octal (base 8, 0 through 7. Think counting w/ fingers, except thumbs missing)
## Decimal (base 10, 0 through 9. Think counting w/ fingers)
## Hexadecimal (Base 16, 0 through 9 + a through f)
## base 360 (circles! We don't use this except in circle math)

print("This is the hexadecimal form of the decimal number 255: ", hex(255))
print("This is the binary form of the decimal number 255: ", bin(255))
print("This is the binary form of the hex number FD: ", bin(0xFD))
print("This is the dec number of the hex number FD: ", int(0xFD))
## Negative numbers

## Two's complement - invert all bits. Add one.

## bitwise left shift: << - multiply bin number by 2 (imagine multiplying by 10)
## bitwise right shift: >> - divide bin num by 2 (imagine div by 10)
## bitwise AND - &
## bitwise OR - |
## bitwise NOT - ~
## bitwie XOR - ^

## format(value, format_spec) = formats the given value using the format.

print(format(11, 'b'))

## chr(uniCode)
## returns the unicode pointer where uniCode = integer pointer. eg:

print(chr(65)) # prints the character A <- capital
print(chr(606)) # prints the character ɞ 

## Globals & Locals

## id(object)
## Returns the identity of the object. 

x = 99
y = 98

print(id(x))
print(id(y))

## Everything is an object, according to Python

## divmod(a, b)
## given two non-complex numbers, returns a pair of numbers as tuple
## consisting of quotient and remainder. uses integer division

print(divmod(99, 4))

time = 111
print(divmod(time, 60))

## When something calls something else, it uses last known object.

c = 99
d = divmod(c, 2)
print(d)
c = 22
print(d)

## Notice that when we printed d, it kept c as 99, instead of updating.

## eval(expression, globals=None, locals=None)
## Evaluates the expression as python expression
## syntax errors reported as exceptions.

