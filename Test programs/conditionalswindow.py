import tkinter as tk

def addition(*args):
    add = sum(args)
    return add

## Product - multiplies all the numbers together
def product(*args):
    prod = 1
    for num in args:
        prod *= num
    return prod

## Average - adds everything and divides by the number of inputs
def average(*args):
    total = addition(*args)
    ave = total / len(args)
    return ave

## Largest - returns the largest number of the inputs
def largest(*args):
    largest_num = args[0]
    for num in args[1:]:
        if num > largest_num:
            largest_num = num
    return largest_num
## Smallest - returns the smallest of the inputs
def smallest(*args):
    smallest_num = args[0]  
    for num in args[1:]:
        if num < smallest_num:
            smallest_num = num
    return smallest_num

## Main Function - does the things   
def main():
    args = [int(entry.get()) for entry in entry_list if entry.get()]
    if not args:
        output_label.config(text="No numbers provided.")
        return
    f = choice.get()
    if f == "add":
        output_label.config(text="The numbers added together is: " + str(addition(*args)))
    elif f == "multiply":
        output_label.config(text="The product of the numbers is: " + str(product(*args)))
    elif f == "average":
        output_label.config(text="The average of the numbers is: " + str(average(*args)))
    elif f == "largest":
        output_label.config(text="The largest number is: " + str(largest(*args)))
    elif f == "smallest":
        output_label.config(text="The smallest number is: " + str(smallest(*args)))
    elif f == "all":
        output_label.config(text="The numbers added together is: " + str(addition(*args)) +
                                      "\n The product of the numbers is: " + str(product(*args)) +
                                      "\n The average of the numbers is: " + str(average(*args)) +
                                      "\n The largest number is: " + str(largest(*args)) +
                                      "\n The smallest number is: " + str(smallest(*args)))

## Function to add more rows without breaking things
def add_entry():
    global entry_row
    if len(entry_list) % 5 == 0:  # Add new row after every 5 entries
        entry_row += 1
        # Move the buttons down
        add_button.grid(row=entry_row + 1, columnspan=5)
        operation_menu.grid(row=entry_row + 2, columnspan=5)
    new_entry = tk.Entry(input_frame, width=5)
    new_entry.grid(row=entry_row, column=len(entry_list) % 5)
    entry_list.append(new_entry)

## Creates a window called "Calculator".
root = tk.Tk()
root.title("Calculator")

## Input section
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

## Creates an entry list
entry_list = []
entry_row = 0
for i in range(5):
    entry = tk.Entry(input_frame, width=5)
    entry.grid(row=entry_row, column=i)
    entry_list.append(entry)

## Adds a button to click for more numbers
add_button = tk.Button(input_frame, text="More Numbers", command=add_entry)
add_button.grid(row=entry_row + 1, columnspan=5)

## Initializes a tkinter variable with default value "add".
choice = tk.StringVar()
choice.set("add")

## Adds a menu to select operation
operation_menu = tk.OptionMenu(input_frame, choice, "add", "multiply", "average", "largest", "smallest", "all")
operation_menu.grid(row=entry_row + 2, columnspan=5)

## Output section
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

## Button to execute
execute_button = tk.Button(root, text="Execute", command=main)
execute_button.pack(pady=5)

## This is what keeps the window open and lets you do stuff.
root.mainloop()
