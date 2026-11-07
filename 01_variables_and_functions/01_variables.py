"""
Variables and user input in Python.

Topics covered:
    - Assigning and reassigning variables
    - Python's built-in types: int, float, str, bool
    - Doing calculations with variables
    - Reading user input with input() and converting it with int() / float()
    - Using the `if __name__ == "__main__":` entry-point guard

Usage:
    python 01_variables.py
"""


# =============================================================================
# CONCEPT — VARIABLES
# =============================================================================
# A variable is a name bound to a value. `=` is assignment, not equality:
# Python works out the right-hand side first, then binds the name to the result.
#
#     age = 25
#     age = age + 1     # evaluates 25 + 1, then rebinds `age` to 26
#
# Python infers the type from the value (dynamic typing):
#     int   -> whole numbers      25
#     float -> decimal numbers    1.65
#     str   -> text               "Aamena"
#     bool  -> True / False       True

def concept_1_demo():
    """Create variables of each basic type, print their types, and reassign one."""
    print("--- Concept 1: Variables ---")

    name = "Aamena"
    age = 25
    height = 1.65
    is_student = True

    print(name, age, height, is_student)
    print(type(name), type(age), type(height), type(is_student))

    age = age + 1
    print("Next year I'll be", age)


# -----------------------------------------------------------------------------
# PROBLEM 1 — Shopping total (fixed values)
# -----------------------------------------------------------------------------
# Task: 3 notebooks at 2.50 each and 2 pens at 1.20 each.
# Store each price and quantity in a variable, calculate the cost of each
# item and the overall total. Expected output: "Total to pay: 9.9"

def problem_1():
    """Calculate a shopping total from hard-coded prices and quantities."""
    print("\n--- Problem 1: Shopping total ---")

    notebook_price = 2.50
    notebook_count = 3
    pen_price = 1.20
    pen_count = 2

    notebooks_cost = notebook_price * notebook_count   # 7.5
    pens_cost = pen_price * pen_count                   # 2.4
    total = notebooks_cost + pens_cost                  # 9.9

    print("Notebooks:", notebooks_cost)
    print("Pens:", pens_cost)
    # Floats are stored in binary, so 7.5 + 2.4 can come out as
    # 9.899999999999999. round(..., 2) displays it to 2 decimal places.
    print("Total to pay:", round(total, 2))


# -----------------------------------------------------------------------------
# PROBLEM 2 — Shopping total (user input)
# -----------------------------------------------------------------------------
# Same calculation as Problem 1, but the prices and quantities come from the user.
#
# Key point: input() always returns a str, even when the user types a number.
#     "3" * 2      -> "33"   (string repetition, not multiplication)
# So the value has to be converted before doing any maths:
#     int("3")     -> 3
#     float("2.5") -> 2.5

def problem_2():
    """Calculate a shopping total from prices and quantities typed by the user."""
    print("\n--- Problem 2: Shopping total with input ---")

    # Convert input straight away: float for prices, int for quantities.
    notebook_price = float(input("Price of one notebook: "))
    notebook_count = int(input("How many notebooks? "))
    pen_price = float(input("Price of one pen: "))
    pen_count = int(input("How many pens? "))

    notebooks_cost = notebook_price * notebook_count
    pens_cost = pen_price * pen_count
    total = notebooks_cost + pens_cost

    print("Notebooks:", round(notebooks_cost, 2))
    print("Pens:", round(pens_cost, 2))
    print("Total to pay:", round(total, 2))


# Example run: entering 2.50, 3, 1.20, 2 prints "Total to pay: 9.9".
# Limitation: non-numeric input (e.g. "abc") raises a ValueError because it
# can't be converted. Handling this is covered in 02_error_handling/.


# -----------------------------------------------------------------------------
# ENTRY POINT
# -----------------------------------------------------------------------------
# `if __name__ == "__main__":` makes the demos run only when this file is
# executed directly. If another module imports it, the functions are available
# but nothing runs automatically.

if __name__ == "__main__":
    concept_1_demo()
    problem_1()
    problem_2()
