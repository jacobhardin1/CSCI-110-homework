'''

Jacob Hardin
2/21/2024
Source: https://open.kattis.com/problems/sith

Step 1: Get name. Can be blank.
Step 2, 3, 4: Get 2 numbers
Step 4: Subtract step 2 from step 3
Step 5: check validity from step 4
Step 6: Determine jedi, sith, or unknown

'''

def main():
    input()
    a = int(input())
    b = int(input())
    c = int(input())
    if(a  - b > 0):
        print("VEIT EKKI")
    elif(a - b == c):
        print("Jedi")
    else:
        print("sith")

main()