## Jacob Hardin
## Assignment - Standard Input and Output
## This program asks the user for their name, then gives them 4 cards.
## The name can be any string; the program does not care.

cardOne = r'''---------
|A      |
| /^\/^\|
| \    /|
|  \  / |
|   \/  |
|      A|
---------'''
cardTwo = r'''---------
|2      |
|   /\  |
|  /  \ |
|  \  / |
|   \/  |
|      2|
---------'''
cardThree = r'''---------
|K      |
|   O   |
|  O+O  |
|  _&_  |
|       |
|      K|
---------'''
cardFour = r'''---------
|7      |
|   /\  |
|  /  \ |
| (____)|
|   ||  |
|      7|
---------'''
name = input("Please enter your name: ")
name = name + "."
print("Hello, ", name, "Here's a few playing cards. Don't show anyone else your hand!")
print(cardOne)
print(cardTwo)
print(cardThree)
print(cardFour)

## This section calls the text file ascii_art.txt and prints the same
## cards seen above (cardOne through cardFour).
## I'm keeping it in as a comment, as it was just a first attempt to
## print out ascii, without cluttering up the top area with a set of
## multi-line variables.


## f= open(r'assignments\stdIO\ascii_art.txt','r')

## print(''.join([line for line in f]))