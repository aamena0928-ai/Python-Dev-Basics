"""
Variable scope and the `global` keyword.

Topics covered:
    - Local vs global scope
    - Why assigning inside a function causes UnboundLocalError
    - The `global` keyword and why it's best avoided
    - Refactoring global state into a pure function (parameter in, return out)

Usage:
    python 05_scope_and_globals.py
"""


# =============================================================================
# CONCEPT — SCOPE AND GLOBALS
# =============================================================================
# Scope determines where a variable can be accessed.
#
#   Global variable -> defined at the top level of the file. Any function
#                      can read it.
#   Local variable  -> defined inside a function. It exists only while the
#                      function runs and isn't visible outside it.
#
# Common pitfall:
#   If a name is assigned anywhere inside a function, Python treats it as
#   local for the entire function.
#
#     score = 0
#     def add_point():
#         score = score + 1    # UnboundLocalError
#
#   Because of the assignment, `score` is local, so reading it on the
#   right-hand side fails: the local hasn't been given a value yet.
#
# The `global` keyword makes this work, but is generally avoided:
#     def add_point():
#         global score         # refer to the module-level `score`
#         score = score + 1
#
# Why avoid `global`:
#   1. Hidden changes: calling add_point() modifies `score`, but nothing at
#      the call site shows it.
#   2. Harder debugging: any function could have changed the value, so
#      tracking down a wrong value means checking all of them.
#   3. Harder testing: results depend on what ran before, not only the inputs.
#
# Preferred approach: pass the value in as a parameter and return the new
# value, so every change is visible in the calling code:
#     score = add_point(score)

score = 0                           # global variable


def show_score():
    """Read the global `score` (reading a global needs no keyword)."""
    print("  show_score sees score =", score)


def set_score_local():
    """Assign to `score`, which creates a local variable; the global is unaffected."""
    score = 100
    print("  inside set_score_local, score =", score)
    # The local `score` is discarded when the function returns.


def set_score_global():
    """Use `global` to modify the module-level `score`."""
    global score
    score = 100


def add_point_broken():
    """Raises UnboundLocalError: `score` is local here but read before assignment."""
    score = score + 1


def add_point(current_score):
    """Return the score plus one. Preferred: value in, new value out."""
    return current_score + 1


def concept_5_demo():
    """Demonstrate local vs global assignment, the UnboundLocalError, and the pure alternative."""
    global score
    print("\n--- Concept 5: Scope and globals ---")

    score = 0
    show_score()                                     # 0

    set_score_local()                                # 100 inside the function...
    print("  after set_score_local, global score =", score)   # ...still 0 globally

    set_score_global()
    print("  after set_score_global, global score =", score)  # 100: global changed

    # Catch the error so the demo can continue
    # (try/except is covered in 02_error_handling/).
    try:
        add_point_broken()
    except UnboundLocalError as error:
        print("  add_point_broken crashed:", error)

    points = 0
    points = add_point(points)       # the update is visible at the call site
    points = add_point(points)
    print("  the better way: points =", points)    # 2


# -----------------------------------------------------------------------------
# PROBLEM 6 — Refactor the wallet to remove the global
# -----------------------------------------------------------------------------
# Starting point: a version that relies on a global variable:
#
#     wallet = 20.0
#     def buy_global(cost):
#         global wallet
#         if cost <= wallet:
#             wallet = wallet - cost
#
# Task: rewrite it as a pure function, buy(wallet, cost):
#   - If the item is affordable, return the new wallet amount.
#   - Otherwise, return the wallet unchanged.
#   - No `global` and no printing inside the function.

def buy(wallet, cost):
    """Return the wallet balance after buying an item, or unchanged if it can't be afforded."""
    if cost <= wallet:
        return wallet - cost    # enough money: deduct the cost
    return wallet               # not enough money: no change


def problem_6():
    """Read a wallet balance and two item prices, updating the balance after each purchase."""
    print("\n--- Problem 6: Wallet without globals ---")

    wallet = float(input("How much money is in your wallet? "))

    cost = float(input("Price of the first item: "))
    new_wallet = buy(wallet, cost)
    if new_wallet == wallet:
        print("  Not enough money!")
    wallet = new_wallet                          # update explicitly at the call site
    print("  Wallet now:", round(wallet, 2))

    cost = float(input("Price of the second item: "))
    new_wallet = buy(wallet, cost)
    if new_wallet == wallet:
        print("  Not enough money!")
    wallet = new_wallet
    print("  Wallet now:", round(wallet, 2))


# Design note: every change to `wallet` in problem_6() happens on an explicit
# `wallet = ...` line, so there are no hidden modifications.


# Run the demos only when this file is executed directly
# (explained at the bottom of 01_variables.py).
if __name__ == "__main__":
    #concept_5_demo()
    problem_6()
