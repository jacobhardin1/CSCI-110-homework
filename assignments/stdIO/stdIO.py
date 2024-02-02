name = input("Please enter your name: ")
name = name + "."
print("Hello, ", name, "Here's a few playing cards. Don't show anyone else your hand!")

def print_ascii(fn):
    f= open(fn, 'r')
    print(' '.join([line for line in f]))

print_ascii('ascii_art.txt')