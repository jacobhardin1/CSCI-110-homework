# homework

NAME - JACOB HARDIN

Homework 1 - stdIO

Program asks for a name, then greets them using said name and prints out 4 cards for them.

Program meets all requirements.

Ran and tested the program several times, using various names, no name, numbers, special characters, escape characters, etc. No bugs found.

Self-evaluated grade: 100%.
Self-eval notes: I'm pretty sure I can make it smaller and/or faster. This program is a proof of concept that I can do it, not that this is the best possible way of doing it. I feel like I could spend more time on it.
Self-eval note 2: Program is easy to read and functions without bugs as far as I can tell.

TO-DO: N/A. Program is complete as is.


Included at the bottom is an additional 2 lines that are commented out, that print out the same ascii characters seen within the variables cardOne, cardTwo, cardThree, and cardFour from a text file rather than from said variables. I have not tested those two lines on a different machine, but they should work.



Homework 2 - Triangle resolver.
This program first queries the user to give some side lengths. Then, it calculates whether this is a valid triangle. If the triangle is NOT legal, it says so and ends the program. Otherwise, it resolves perimeter, area, and angles in degrees.

The formula used to find the area is Heron's Formula, which uses the 3 sides to determine the area. The program's perimeter calculation is rather simple - a + b + c = perimeter. We use the cosine function to find angle_a and angle_b, then round them.

angle_c is found by subtracting angle_a and angle_b from 180. In order to cut back on floating point rounding errors, it also rounds angle_c to 3 decimal places.

Math is done using floats, for angle and area calculations.

Self-eval: 110%
Self-eval notes: The very first thing the program does is check for triangle validity, by way of adding 2 lines and comparing to the third. It does this 3 times, checking to make sure 2 lines add to be bigger than the third.

TODO:
    N/A: Program complete.

Definitions of triangles: 

    Scalene: all three sides are in different lengths, and all three angles are of different measures. However, the sum of all the interior angles is always equal to 180 degrees. Thus, it meets the angle sum property of the triangle.

    Isoscelese - two sides of equal length. The angles opposite to the two sides correspond to each other and are also equal.

    Equilateral - all three sides have the same length. All three angles are also the same.

    Oblong - The angle opposite the hypotenuse is larger than 90 degrees.

    Acute - all three angles are smaller than 90 degrees

    Right - The angle opposite the hypotenuse is exactly 90 degrees.

    There is a python script in Test programs where the validity check doesn't work properly. The generally accepted consensus of a triangle, in mathematics, is listed above in general terms.

 Assignment 3 - Functions

    This program does math based on user inputs. First step - ask for inputs. After that, it iterates through several functions sequentially, using the two numbers provided. ALl math is done with floats.

Self-eval: 110%
Self-eval notes: Could be cleaned up. Otherwise is fine.

TODO:
    N/A - Project complete


Assignment 4 - Conditionals
    Project name: Conditionals.py

    This program does various things to 5 inputs:
        Addition - adds the numbers together
        Product - multiplies all the numbers together
        Average - adds everything and divides by 5
        Largest - returns the largest number of the inputs
        Smallest - returns the smallest of the inputted numbers
    
    The program can run one, none, or all of the functions described.

    In the Test programs folder is another program called conditionalswindow.py
    
    This program takes the previous program and encapsulates it into a separate window, and allows for fewer than or more than 5 numbers. That one is just for fun, to play with a library and see what I can do with it. It DOES use min and max for the smallest/largest numbers.

    Self-Eval: 110%.
        Notes: Does everything as intended, including a loop function. Loop counter included for fun.

    TODO: Testing


Assignment 5 - Guess The Number
    file name: numberguess.py

    Basic number guessing game. Range for number generator is 1 to 20. Asks user for name, then runs the game in a While True loop. Regardless of guessing correct number, the game will ask to play again. On a "yes", the game will generate a new random number and prompt user for gameplay action.

    The game also checks for a valid input - outside of range will ask for a non-float number within the range of numbers (1 through 20).

    The game ALSO clears the terminal fairly frequently.

    Self-eval: 110%
        Eval Notes: Everything works as intended.

    TODO: None
        Bug: when checking for "not yes", "not y" on play again, it would end the prgram if "not yes" was true, even if "y" was false.
            Fixed: Changed the OR statement to an AND statement.
        
