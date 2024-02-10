# homework

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
    Various clean-ups.
    Make it look nicer. It's readable, at least.
    Decide if you really want to define every little section.
    Rename files.

Definitions of triangles: 

    Scalene: all three sides are in different lengths, and all three angles are of different measures. However, the sum of all the interior angles is always equal to 180 degrees. Thus, it meets the angle sum property of the triangle.

    Isoscelese - two sides of equal length. The angles opposite to the two sides correspond to each other and are also equal.

    Equilateral - all three sides have the same length. All three angles are also the same.

    Oblong - The angle opposite the hypotenuse is larger than 90 degrees.

    Acute - all three angles are smaller than 90 degrees

    Right - The angle opposite the hypotenuse is exactly 90 degrees.

    There is a python script in Test programs where the validity check doesn't work properly. The generally accepted consensus of a triangle, in mathematics, is listed above in general terms.