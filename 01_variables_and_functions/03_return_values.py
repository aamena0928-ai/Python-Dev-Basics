"""
Returning values from functions.

Topics covered:
    - The difference between print() and return
    - Storing and reusing a function's result
    - Functions without a return statement give back None
    - Building a shopping total from returned values

Usage:
    python 03_return_values.py
"""


# =============================================================================
# CONCEPT — RETURN VALUES
# =============================================================================
# `return` sends a value back to the caller.
#
#     print()  -> displays a value; the caller receives nothing back.
#     return   -> hands a value back; the caller can store and reuse it.
#
#     def add(a, b):
#         return a + b
#
#     result = add(2, 3)     # the call evaluates to its return value, 5
#     print(result * 10)     # 50
#
# Notes:
#   1. `return` exits the function immediately; any lines after it don't run.
#   2. A function with no `return` statement returns None.

def add_and_print(a, b):
    """Print the sum of a and b. Returns None."""
    print(a + b)


def add_and_return(a, b):
    """Return the sum of a and b."""
    return a + b


def concept_3_demo():
    """Compare a function that prints its result with one that returns it."""
    print("\n--- Concept 3: Return values ---")

    x = add_and_print(2, 3)     # displays 5...
    print("x is", x)            # ...but x is None, since nothing was returned

    y = add_and_return(2, 3)    # displays nothing...
    print("y is", y)            # ...but y holds 5
    print("y * 10 is", y * 10)  # and can be used in further calculations


# -----------------------------------------------------------------------------
# PROBLEM 4 — Receipt with a total (using return)
# -----------------------------------------------------------------------------
# Task: write item_cost(price, count) that returns price * count, use it to
# calculate each item's cost, then add the results together for a total.

def item_cost(price, count):
    """Return the total cost of `count` items at `price` each."""
    return price * count


def problem_4():
    """Read prices and quantities, then print each item's cost and the total."""
    print("\n--- Problem 4: Total using return ---")

    notebook_price = float(input("Price of one notebook: "))
    notebook_count = int(input("How many notebooks? "))
    pen_price = float(input("Price of one pen: "))
    pen_count = int(input("How many pens? "))

    # Each call evaluates to the value it returns, so it can be stored.
    notebooks_cost = item_cost(notebook_price, notebook_count)
    pens_cost = item_cost(pen_price, pen_count)
    eraser_cost = item_cost(0.75, 4)

    # Possible because item_cost() returns its result instead of printing it.
    total = notebooks_cost + pens_cost + eraser_cost

    print("\nNotebooks:", round(notebooks_cost, 2))
    print("Pens:", round(pens_cost, 2))
    print("Erasers:", round(eraser_cost, 2))
    print("Total to pay:", round(total, 2))


# Run the demos only when this file is executed directly
# (explained at the bottom of 01_variables.py).
if __name__ == "__main__":
    concept_3_demo()
    problem_4()
