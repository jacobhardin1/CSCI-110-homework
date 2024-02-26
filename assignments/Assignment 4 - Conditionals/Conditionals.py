## Jacob Hardin
## Conditionals
## CSCI 110 Beg. Programming - Python
## 

## Addition - adds the numbers together
def addition(a, b, c, d, e):
    add = a + b + c + d + e
    return add

## Product - multiplies all the numbers together
def product(a, b, c, d, e):
    prod = a * b * c * d * e
    return prod

## Average - adds everything and divides by 5
def average(a, b, c, d, e):
    ave = addition(a, b, c, d, e) / 5
    return ave

## Largest - returns the largest number of the 5 inputs
def largest(a, b, c, d, e):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    if d > largest:
        largest = d
    if e > largest:
        largest = e
    return largest

## Smallest - returns the smallest of the inputted numbers
def smallest(a, b, c, d, e):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    if d < smallest:
        smallest = d
    if e < smallest:
        smallest = e
    return smallest

## Assigns test cases.
def test():
    assert addition(3, 6, 9, 12, 15), 45
    assert addition(4, 8, 5, 2, 7), 26
    assert product(3, 5, 4, 9, 77), 41580
    assert product(6, 7, 2, 99, 88), 731808
    assert average(4, 8, 12, 22, 28), 14.8
    assert average(99, 2048, 776, 255, 1001), 835.8
    assert largest(100, 30001, 20, 99999, 1), 99999
    assert largest(25000, 10, 1, 0, -1), 25000
    assert smallest(1, 2, 5, -3, 2), -3
    assert smallest(3, 3, 2, 1, 2), 1

## Main Function - does the things   
def main():
    f = input("What would you like to do? Add/Multiply/Average/Largest/Smallest/All: ").lower()
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if f == "add":
        print("The numbers added together is: ", addition(a, b, c, d, e))
    elif f == "multiply":
        print("The product of the numbers is: ", product(a, b, c, d, e))
    elif f == "average":
        print("The average of the numbers is: ", average(a, b, c, d, e))
    elif f == "largest":
        print("The largest number is: ", largest(a, b, c, d, e))
    elif f == "smallest":
        print("The smallest number is: ", smallest(a, b, c, d, e))
    elif f == "all":
        print("The numbers added together is: ", addition(a, b, c, d, e))
        print("The product of the numbers is: ", product(a, b, c, d, e))
        print("The average of the numbers is: ", average(a, b, c, d, e))
        print("The largest number is: ", largest(a, b, c, d, e))
        print("The smallest number is: ", smallest(a, b, c, d, e))


test()
if __name__ == "__main__":
    while True:
        main()
        another = input(r'Another one? yes/no: ').lower()
        if another == "yes" or another == "y":
            continue
        else:
            break