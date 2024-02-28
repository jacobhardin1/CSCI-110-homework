## Jacob Hardin
## Conditionals
## CSCI 110 Beg. Programming - Python
## 

## Addition - adds the numbers together
def addition(a, b, c, d, e):
    '''Adds numbers together.'''
    add = a + b + c + d + e
    return add

## Product - multiplies all the numbers together
def product(a, b, c, d, e):
    '''Multiplies numbers together.'''
    prod = a * b * c * d * e
    return prod

## Average - adds everything and divides by 5
def average(a, b, c, d, e):
    '''Returns the average of the numbers.'''
    ave = addition(a, b, c, d, e) / 5
    return ave

## Largest - returns the largest number of the 5 inputs
def largest(a, b, c, d, e):
    '''Finds the largest number.'''
    largest = a
    for num in [b, c, d, e]:
        if num > largest:
            largest = num
    return largest

## Smallest - returns the smallest of the inputted numbers
def smallest(a, b, c, d, e):
    '''Finds the smallest number.'''
    smallest = a
    for num in [b, c, d, e]:
        if num < smallest:
            smallest = num
    return smallest

## Assigns test cases.
def test():
    '''Test cases'''
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


## Main function - Loops while another == true
def main():
    i = 1
    while True:
         f = input("What would you like to do? Add/Multiply/Average/Largest/Smallest/All: ").lower()
         a, b, c, d, e = map(int, input().split())
         if f == "add":
             print(f"The numbers added together is: {addition(a, b, c, d, e)}")
         elif f == "multiply":
             print(f"The product of the numbers is: {product(a, b, c, d, e)}")
         elif f == "average":
             print(f"The average of the numbers is: {average(a, b, c, d, e)}")
         elif f == "largest":
             print(f"The largest number is: {largest(a, b, c, d, e)}")
         elif f == "smallest":
            print(f"The smallest number is: {smallest(a, b, c, d, e)}")
         elif f == "all":
             print("The numbers added together is: ", addition(a, b, c, d, e))
             print("The product of the numbers is: ", product(a, b, c, d, e))
             print("The average of the numbers is: ", average(a, b, c, d, e))
             print("The largest number is: ", largest(a, b, c, d, e))
             print("The smallest number is: ", smallest(a, b, c, d, e))
         another = input(r'Another one? yes/no: ').lower()
         if another == 'yes' or another == 'y':
             i += 1
             continue
         else:
             print(f'Loop successfully executed {i} times.')
             break

if __name__ == "__main__":
    main()