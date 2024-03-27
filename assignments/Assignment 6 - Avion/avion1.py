'''
Jacob Hardin
3/25/24
Kattis Problem: https://open.kattis.com/problems/avion
Logical Steps:
1. Accept inputs
2. Find CIA Blimps!
3. Return list location of each blimp
4. If no CIA Blimps, return "HE GOT AWAY!"


'''
import sys
## Checks for the literal string "FBI" in the string
def is_cia_blimp(code):
    return "FBI" in code

## Collects strings one at a time. Also makes all strings uppercase
## and also strips unnecessary characters.
def input_registration_codes():
    registrations = []
    print("Enter 5 blimp registration codes:", file=sys.stderr)
    for _ in range(5):
        registrations.append(input().strip().upper())
    return registrations

## Uses is_cia_blimp to iterate through the list, and adds any line where
## it finds the literal string "FBI"
def find_cia_blimps(registrations):
    cia_indices = []
    for i, code in enumerate(registrations, 1):
        if is_cia_blimp(code):
            cia_indices.append(i)
    return cia_indices

## If there ARE strings that match, it lists them. Otherwise, it prints
## "HE GOT AWAY".
def output_result(cia_indices):
    if cia_indices:
        print(" ".join(map(str, cia_indices)))
    else:
        print("HE GOT AWAY!")

## Test is_cia_blimp function
def test_is_cia_blimp():
    assert is_cia_blimp("FBI123") == True
    assert is_cia_blimp("123FBI") == True
    assert is_cia_blimp("F-B-I") == False
    assert is_cia_blimp("ABC123") == False
    print("is_cia_blimp tests passed.")

## Test input_registration_codes function
def test_input_registration_codes():
    ## Replace input() with a mocked input function for testing
    global input
    input = lambda: "FBI123"  # Simulate user input
    registrations = input_registration_codes()
    assert registrations == ["FBI123", "FBI123", "FBI123", "FBI123", "FBI123"]
    print("input_registration_codes tests passed.")

## Test find_cia_blimps function
def test_find_cia_blimps():
    registrations = ['ABC123', 'FBI456', 'XYZ789', 'HEY-FBI', '987-FBI-321']
    cia_indices = find_cia_blimps(registrations)
    assert cia_indices == [2, 4, 5]
    print("find_cia_blimps tests passed.")

## Test output_result function
def test_output_result():
    ## Replace print with a mocked print function for testing
    global print
    printed_output = ""
    def mocked_print(*args, **kwargs):
        nonlocal printed_output
        printed_output += " ".join(map(str, args)) + "\n"

    print = mocked_print

    cia_indices = [2, 4, 5]
    output_result(cia_indices)
    assert printed_output.strip() == "2 4 5"
    print("output_result tests passed.")

def main():
    registrations = input_registration_codes()
    cia_indices = find_cia_blimps(registrations)
    output_result(cia_indices)

def test():
    test_is_cia_blimp()
    test_input_registration_codes()
    test_find_cia_blimps()
    test_output_result()


if __name__ == "__main__":
    main()
