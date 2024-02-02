name = input("Please enter your name: ")
name = name + "."
print("Hello, ", name, "Here's a few playing cards. Don't show anyone else your hand!")

f= open(r'assignments\stdIO\ascii_art.txt','r')

print(''.join([line for line in f]))