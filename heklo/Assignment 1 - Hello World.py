## Jacob Hardin
## Assignment 1 - Hello World

# Importing datetime for time information
import datetime

time = datetime.datetime.now()

# Printing Hello World, then giving the time, then being done.
print("Hello World!")
print("Time: ", time.strftime("%Y-%m-%d %H:%M:%S"))