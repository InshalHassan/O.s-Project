import tkinter as tk
from tkinter import messagebox
import math

# Create the main window
window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("400x600")

# Variable to store the expression entered by the user
expression = ""

# Function to update the expression when a button is clicked
def button_click(value):
    global expression
    expression += str(value)
    entry_var.set(expression)

# Function to clear the input field
def clear():
    global expression
    expression = ""
    entry_var.set(expression)

# Function to evaluate the expression
def evaluate():
    try:
        global expression
        result = str(eval(expression))
        entry_var.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression")
        expression = ""

# Function to handle scientific functions
def scientific_function(func):
    global expression
    try:
        if func == "sin":
            expression = str(math.sin(math.radians(float(expression))))
        elif func == "cos":
            expression = str(math.cos(math.radians(float(expression))))
        elif func == "tan":
            expression = str(math.tan(math.radians(float(expression))))
        elif func == "sqrt":
            expression = str(math.sqrt(float(expression)))
        elif func == "log":
            expression = str(math.log10(float(expression)))
        entry_var.set(expression)
    except Exception as e:
        messagebox.showerror("Error", "Invalid input for scientific function")
        expression = ""

# Tkinter variable to hold the expression
entry_var = tk.StringVar()

# Entry widget to display the expression
entry = tk.Entry(window, textvar=entry_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout for the calculator
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("sqrt", 5, 3),
    ("log", 6, 0), ("(", 6, 1), (")", 6, 2), ("C", 6, 3)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=10, height=3, font=("Arial", 14), command=evaluate)
    elif text == "C":
        button = tk.Button(window, text=text, width=10, height=3, font=("Arial", 14), command=clear)
    elif text in ["sin", "cos", "tan", "sqrt", "log"]:
        button = tk.Button(window, text=text, width=10, height=3, font=("Arial", 14), command=lambda func=text: scientific_function(func))
    else:
        button = tk.Button(window, text=text, width=10, height=3, font=("Arial", 14), command=lambda value=text: button_click(value))
    
    button.grid(row=row, column=col)

# Run the Tkinter event loop
window.mainloop()
