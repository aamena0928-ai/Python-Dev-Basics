"""
The mutable default argument pitfall.

Topics covered:
    - Default parameter values
    - Mutable vs immutable types
    - Why a mutable default (e.g. []) is shared between calls
    - The standard fix: default to None and create the object inside the function

Usage:
    python 06_mutable_defaults.py
"""


# =============================================================================
# CONCEPT — MUTABLE DEFAULT ARGUMENTS
# =============================================================================
# A default value is used when the caller omits that argument:
#
#     def greet(name="friend"):
#         print("Hello,", name)
#
#     greet()          # Hello, friend   (default used)
#     greet("Sam")     # Hello, Sam
#
# Mutable objects can be changed in place; immutable ones can only be replaced.
#     Mutable:    list [], dict {}, set()
#     Immutable:  int, float, str, bool, None
#
# The pitfall:
#   Default values are evaluated once, when the `def` statement runs, not on
#   every call. A mutable default is therefore shared by every call that
#   uses it, so changes from one call persist into the next. This is a
#   hidden side effect (see 04_side_effects.py).
#
#     def add_item(item, cart=[]):     # this list is created only once
#         cart.append(item)
#         return cart
#
#     add_item("pen")     # ['pen']
#     add_item("book")    # ['pen', 'book']   <- 'pen' carried over
#
# The fix: default to None and create a new object inside the function.
#
#     def add_item(item, cart=None):
#         if cart is None:
#             cart = []                # new list on every call
#         cart.append(item)
#         return cart
#
# `is None` is the idiomatic way to check for None (preferred over `== None`).
#
# Immutable defaults such as 0, "dog", 2.5 or None are safe; only mutable
# defaults ([], {}, set()) cause this problem.

def add_item_buggy(item, cart=[]):
    """Append item to cart. Bug: the default list is shared across calls."""
    cart.append(item)
    return cart


def add_item_fixed(item, cart=None):
    """Append item to cart, creating a new list if none is passed in."""
    if cart is None:
        cart = []
    cart.append(item)
    return cart


def concept_6_demo():
    """Compare the buggy and fixed versions and confirm the shared list with id()."""
    print("--- Concept 6: Mutable default arguments ---")

    print("Buggy version:")
    print("  add_item_buggy('pen')  ->", add_item_buggy("pen"))
    print("  add_item_buggy('book') ->", add_item_buggy("book"))   # still contains 'pen'

    print("Fixed version:")
    print("  add_item_fixed('pen')  ->", add_item_fixed("pen"))
    print("  add_item_fixed('book') ->", add_item_fixed("book"))   # new list each call

    print("Passing your own list still works:")
    my_cart = ["apple"]
    print("  add_item_fixed('pear', my_cart) ->", add_item_fixed("pear", my_cart))
    print("  add_item_fixed('orange', my_cart) ->", add_item_fixed("orange", my_cart))

    # id() returns an object's identity; equal ids confirm it's the same list.
    first = add_item_buggy("x")
    second = add_item_buggy("y")
    print("Buggy: same list object both times?", id(first) == id(second))   # True


# -----------------------------------------------------------------------------
# PROBLEM 7 — Fix the shared shopping cart
# -----------------------------------------------------------------------------
# Scenario: a shop uses this function to start a new order for each customer:
#
#     def new_order_buggy(item, order=[]):
#         order.append(item)
#         return order
#
# Because the default list is shared, customer 2's order includes customer 1's
# items. Task: write new_order(item, order=None) so each customer gets a fresh
# order unless an existing order is passed in.

def new_order_buggy(item, order=[]):
    """Start an order with item. Bug: all default orders share one list."""
    order.append(item)
    return order


def new_order(item, order=None):
    """Add item to order, starting a new order if none is passed in."""
    if order is None:
        order = []
    order.append(item)
    return order


def problem_7():
    """Show the shared-order bug with two customers, then the fixed behaviour."""
    print("\n--- Problem 7: Fix the shared shopping cart ---")

    item_1 = input("Customer 1, what do you want to buy? ")
    item_2 = input("Customer 2, what do you want to buy? ")

    print("\nBuggy version:")
    print("  Customer 1's order:", new_order_buggy(item_1))
    print("  Customer 2's order:", new_order_buggy(item_2), "<- has customer 1's item!")

    print("\nFixed version:")
    print("  Customer 1's order:", new_order(item_1))
    print("  Customer 2's order:", new_order(item_2), "<- only their own item")

    # Passing an existing order adds to it instead of starting a new one.
    order = new_order(item_1)
    order = new_order("bag", order)
    print("  Customer 1 adds a bag:", order)


# The same pitfall applies to dict defaults, and the same fix works:
#
#     def add_score(name, score, scores={}):     # buggy
#         scores[name] = score
#         return scores
#
#     add_score("Ali", 10)   -> {'Ali': 10}
#     add_score("Sara", 8)   -> {'Ali': 10, 'Sara': 8}   (expected {'Sara': 8})


# Run the demos only when this file is executed directly
# (explained at the bottom of 01_variables.py).
if __name__ == "__main__":
#    concept_6_demo()
  problem_7()
