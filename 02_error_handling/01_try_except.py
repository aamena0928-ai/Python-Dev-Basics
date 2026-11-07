"""
Handling errors with try / except.

Topics covered:
    - What exceptions are and when Python raises them
    - Catching specific exceptions with try / except
    - Accessing the error message with `except ... as error`
    - Making user input robust against invalid values

Usage:
    python 01_try_except.py
"""


# =============================================================================
# CONCEPT — EXCEPTIONS AND try / except
# =============================================================================
# When Python can't complete an operation, it raises an exception. If the
# exception isn't handled, the program stops and prints a traceback.
#
# Examples from earlier files:
#     float("abc")        -> ValueError          (text can't be converted to a number)
#     10 / 0              -> ZeroDivisionError   (division by zero)
#     score = score + 1   -> UnboundLocalError   (see 05_scope_and_globals.py)
#
# try / except catches an exception and handles it instead of crashing:
#
#     try:
#         ...code that might fail...
#     except ValueError:
#         ...code to run if that error occurs...
#
# Execution flow:
#   1. The `try` block runs line by line.
#   2. If no exception occurs, the `except` block is skipped.
#   3. If one occurs, execution jumps to the matching `except` block and the
#      rest of the `try` block is skipped.
#   4. The program then continues normally.
#
# Best practice: catch specific exceptions (e.g. `except ValueError:`).
# A bare `except:` catches everything and can hide real bugs.

def concept_1_demo():
    """Show caught and uncaught paths through try / except."""
    print("--- Concept 1: try / except ---")

    # 1. Unhandled, this line would stop the program:
    #    price = float("abc")

    # 2. Handled with try / except:
    try:
        price = float("abc")
        print("This line never runs, because the line above failed")
    except ValueError:
        print("Caught a ValueError: 'abc' is not a number")

    # 3. When no exception occurs, the except block is skipped:
    try:
        price = float("2.50")
        print("Converted fine:", price)
    except ValueError:
        print("This line never runs, because there was no error")

    # 4. `as error` gives access to Python's error message:
    try:
        result = 10 / 0
    except ZeroDivisionError as error:
        print("Caught:", error)

    print("The program is still running!")


# -----------------------------------------------------------------------------
# PROBLEM 1 — Shopping total that handles invalid input
# -----------------------------------------------------------------------------
# Background: in 01_variables_and_functions/01_variables.py (Problem 2),
# entering "abc" as a price raised a ValueError and stopped the program.
#
# Task: write read_number(message) that:
#   - prompts the user with input(message)
#   - converts the answer to a float and returns it
#   - on failure, prints "That's not a number, using 0" and returns 0.0
# Then use it to calculate a shopping total that never crashes.

def read_number(message):
    """Prompt for a number and return it as a float, or 0.0 if the input is invalid."""
    text = input(message)
    try:
        return float(text)
    except ValueError:
        print("  That's not a number, using 0")
        return 0.0                      # fall back to a safe default


def problem_1():
    """Calculate a shopping total using read_number() so invalid input can't crash it."""
    print("\n--- Problem 1: Shopping total that doesn't crash ---")

    notebook_price = read_number("Price of one notebook: ")
    notebook_count = read_number("How many notebooks? ")
    pen_price = read_number("Price of one pen: ")
    pen_count = read_number("How many pens? ")

    total = notebook_price * notebook_count + pen_price * pen_count
    print("Total to pay:", round(total, 2))


# Example: entering "abc" for any value prints a warning and uses 0 instead
# of stopping the program.
#
# Limitation: silently using 0 avoids a crash but may give a misleading total.
# A better approach is to re-prompt until a valid number is entered, using
# a loop combined with try / except.


# Run the demos only when this file is executed directly
# (explained at the bottom of 01_variables_and_functions/01_variables.py).
if __name__ == "__main__":
  #  concept_1_demo()
   problem_1()
