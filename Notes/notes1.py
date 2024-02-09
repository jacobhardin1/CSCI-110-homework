import math

def main():
    print("hello world.")
    area = calc_area(1)
    print(area)

def calc_area(radius):
    area = math.pi * radius **2
    return area




main()