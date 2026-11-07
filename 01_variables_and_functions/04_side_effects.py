"""
Side effects and pure functions.

Topics covered:
    - What a side effect is, with common examples
    - Pure functions vs functions that modify their arguments
    - A basic introduction to lists (append, sum, indexing)
    - Designing a shopping cart with one mutating and one pure function

Usage:
    python 04_side_effects.py
"""


# Copied from 03_return_values.py (Problem 4) so this file runs on its own.
def item_cost(price, count):
    """Return the total cost of `count` items at `price` each."""
    return price * count


# =============================================================================
# CONCEPT — SIDE EFFECTS
# =============================================================================
# A side effect is any change a function makes outside itself, beyond
# returning a value. Common examples:
#   - printing to the screen               print("hi")
#   - modifying a list passed in           my_list.append(5)
#   - modifying a global variable          global count
#   - writing to a file, sending a request, etc.
#
# A pure function has no side effects:
#   - it depends only on its parameters and communicates only via return
#   - the same inputs always produce the same output
#   - nothing outside the function changes
#
# Side effects aren't inherently bad (programs need to print and save data).
# The aim is to keep them explicit and predictable.
#
# List basics used in this file:
#     prices = [2.5, 1.2]      # an ordered collection of values
#     prices.append(0.75)      # add to the end -> [2.5, 1.2, 0.75]
#     sum(prices)              # add all values -> 4.45

def double_pure(numbers):
    """Pure: return a new list with each number doubled. The input is unchanged."""
    new_list = []
    for n in numbers:
        new_list.append(n * 2)
    return new_list


def double_in_place(numbers):
    """Side effect: double each number in the given list in place. Returns None."""
    for i in range(len(numbers)):   # loop over each index: 0, 1, 2, ...
        numbers[i] = numbers[i] * 2


def concept_4_demo():
    """Show that the in-place version changes the caller's list and the pure one doesn't."""
    print("\n--- Concept 4: Side effects ---")

    original = [1, 2, 3]
    result = double_pure(original)
    print("Pure:       original =", original, "| result =", result)

    original = [1, 2, 3]
    result = double_in_place(original)
    print("In place:   original =", original, "| result =", result)
    # `original` changed without being reassigned here: a side effect.


# -----------------------------------------------------------------------------
# PROBLEM 5 — Shopping cart: side effect vs pure
# -----------------------------------------------------------------------------
# Task: write two functions:
#   add_to_cart(cart, cost)  -> side effect: appends cost to the cart list,
#                               returns nothing.
#   cart_total(cart)         -> pure: returns the total without modifying the cart.

def add_to_cart(cart, cost):
    """Append `cost` to `cart`. Modifies the caller's list (side effect)."""
    cart.append(cost)


def cart_total(cart):
    """Return the sum of all costs in `cart` without modifying it (pure)."""
    return sum(cart)


def problem_5():
    """Build a cart from user input, then show the total and the unchanged cart."""
    print("\n--- Problem 5: Shopping cart ---")

    cart = []

    notebook_price = float(input("Price of one notebook: "))
    notebook_count = int(input("How many notebooks? "))
    add_to_cart(cart, item_cost(notebook_price, notebook_count))  # reuses item_cost()
    print("Cart now:", cart)

    pen_price = float(input("Price of one pen: "))
    pen_count = int(input("How many pens? "))
    add_to_cart(cart, item_cost(pen_price, pen_count))
    print("Cart now:", cart)

    total = cart_total(cart)
    print("Total to pay:", round(total, 2))
    print("Cart after total:", cart, "(unchanged, cart_total is pure)")


# Applying this to earlier files:
#   say_hello, print_receipt_line -> have side effects (they print)
#   item_cost, add_and_return     -> pure


# Run the demos only when this file is executed directly
# (explained at the bottom of 01_variables.py).
if __name__ == "__main__":
    concept_4_demo()
    problem_5()
