## Functions can be defined by the user.

def greet():
    name = input("What is your name?")
    if 'john' in name:
        print("go away,", name)
    elif 'jane' in name:
        print("stop your nonsense,", name)
    else:
        print("Hello, ", name)
    


def add_two(number1, number2):
    sum = number1 + number2
    return sum




def main(): # Usually defined as the beginning of the program
    greet()
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(add_two(num1, num2))




## First unindented line that is not e definition or an import
## is the beginning of the program.
    
main()
