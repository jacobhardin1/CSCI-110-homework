'''
Jacob Hardin
02/19/2024
Problem source: https://open.kattis.com/problems/leggjasaman

Step 1: Take input 1 and 2
Step 2: Add inputs together
Step 3: Print output

'''

def addition(a, b):
    sum = a+b
    return sum

def main():
    a = int(input('Enter a number'))
    b = int(input('Enter a number'))
    print(addition(a, b))
    

