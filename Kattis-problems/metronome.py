'''
Jacob Hardin
02/19/2024
Problem source: https://open.kattis.com/problems/metronome

Step 1: input length as integer
Step 2: divide integer by 4
step 2.5: Output

'''

def divide(a):
    div = a/4
    return div

def main():
    a = int(input())
    print(divide(a))

main()
