##def reverse_print():
##    n = int(input("Enter the number of integers: "))
##    numbers = []
##    for _ in range(n):
##        number = int(input("Enter an integer: "))
##        numbers.append(number)
##    print("Reversed list:")
##    for num in reversed(numbers):
##        print(num)

##reverse_print()

def reverse_print():
    n = int(input("Enter the number of integers: "))
    numbers = list(map(int, input("Enter the integers separated by spaces: ").split()))
    print("Reversed list:")
    for num in reversed(numbers):
        print(num)

reverse_print()