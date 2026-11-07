"""
Defining and calling functions.

Topics covered:
    - Defining a function with `def`
    - The difference between parameters and arguments
    - Calling the same function with different arguments
    - Using a function to remove repeated code

Usage:
    python 02_functions.py
"""


# =============================================================================
# CONCEPT — FUNCTIONS
# =============================================================================
# A function is a named, reusable block of code.
#
#     def function_name(parameter1, parameter2):
#         ...code that uses parameter1 and parameter2...
#
#   - Parameters are the names listed in the definition.
#   - Arguments are the actual values passed in when the function is called.
#
# Defining a function does not run it; it only runs when called with ():
#
#     def say_hello(name):          # definition: nothing runs yet
#         print("Hello,", name)
#
#     say_hello("Aamena")           # call -> Hello, Aamena
#     say_hello("Sam")              # same function, different argument
#
# Benefits: write logic once and reuse it, and give a task a descriptive
# name so the calling code is easier to read.

def say_hello(name):
    """Print a greeting for the given name."""
    print("Hello,", name)


def concept_2_demo():
    """Call say_hello() with different arguments."""
    print("\n--- Concept 2: Functions ---")
    say_hello("Aamena")     # "Aamena" is the argument; `name` is the parameter
    say_hello("Sam")        # same function, different argument


# -----------------------------------------------------------------------------
# PROBLEM 3 — Print a receipt using a function
# -----------------------------------------------------------------------------
# Task: 01_variables.py repeats the same calculation for each item. Replace
# that repetition with one function, print_receipt_line(item, price, count),
# called once per item. Each line should look like:
#     3 x notebook @ 2.5 = 7.5

def print_receipt_line(item, price, count):
    """Print one receipt line showing quantity, item, unit price and cost."""
    cost = price * count
    print(count, "x", item, "@", price, "=", round(cost, 2))


def problem_3():
    """Read prices and quantities, then print a receipt line for each item."""
    print("\n--- Problem 3: Receipt with a function ---")

    notebook_price = float(input("Price of one notebook: "))
    notebook_count = int(input("How many notebooks? "))
    pen_price = float(input("Price of one pen: "))
    pen_count = int(input("How many pens? "))

    print("\nYour receipt:")
    print_receipt_line("notebook", notebook_price, notebook_count)  # values from input
    print_receipt_line("pen", pen_price, pen_count)                  # values from input
    print_receipt_line("eraser", 0.75, 4)                            # literal values


# Limitation: print_receipt_line() only prints the cost, so the caller can't
# use it to calculate a total. 03_return_values.py solves this with `return`.


# Run the demos only when this file is executed directly
# (explained at the bottom of 01_variables.py).
if __name__ == "__main__":
    concept_2_demo()
    problem_3()
