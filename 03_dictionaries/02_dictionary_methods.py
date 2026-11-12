"""
Party Check-in: practising dictionary methods.

A guest list is stored as a dictionary of guest name -> party size.
Guests are checked in as they arrive, and a report is printed at the end.

Topics covered:
    - Making independent copies with .copy()
    - Removing a key and getting its value back with .pop()
    - Emptying a dictionary with .clear()
    - Counting keys with len()
    - Checking whether a key exists with `in`
    - Looping through key/value pairs with .items()

Usage:
    python 02_dictionary_methods.py

Example run:
    Welcome! 4 parties expected tonight.
    4 parties still to arrive.
    Who has arrived? sara
    Welcome, Sara! Party of 2.
    3 parties still to arrive.
    Who has arrived? Tom
    Sorry, Tom is not on the list.
    3 parties still to arrive.
    Who has arrived? Ali
    Welcome, Ali! Party of 4.
    2 parties still to arrive.
    Who has arrived? close
    Doors closed.

    --- Party report ---
    People inside: 6
    Sara (2): arrived
    Ali (4): arrived
    Omar (1): no-show
    Lina (3): no-show
"""


# =============================================================================
# CONCEPT: COPYING A DICTIONARY
# =============================================================================
# `=` does NOT copy a dictionary. It gives the same dictionary a second name:
#
#     waiting = GUESTS          # one dictionary, two names
#     waiting.pop("Sara")       # Sara is now missing from GUESTS too!
#
# .copy() creates a new, separate dictionary, so changes to one
# don't affect the other:
#
#     waiting = GUESTS.copy()   # two dictionaries
#     waiting.pop("Sara")       # GUESTS still has Sara


# Guest name -> party size (how many people, including the guest).
GUESTS = {"Sara": 2, "Ali": 4, "Omar": 1, "Lina": 3}


def main():
    """Check guests in until everyone arrives or the doors close."""
    # guest_list keeps everyone for the final report;
    # waiting shrinks as guests are checked in.
    guest_list = GUESTS.copy()
    waiting = GUESTS.copy()

    # Created BEFORE the loop so they keep growing across rounds.
    people_inside = 0
    arrived = []

    print(f"Welcome! {len(waiting)} parties expected tonight.")

    # Keep checking guests in until nobody is left waiting.
    while len(waiting) > 0:
        print(f"{len(waiting)} parties still to arrive.")

        # .strip().title() so "  sara " matches the key "Sara".
        name = input("Who has arrived? ").strip().title()

        if name == "":
            print("Please type a name.")

        elif name == "Close":
            # Emptying the dictionary makes len(waiting) 0,
            # so the while condition is False and the loop ends.
            waiting.clear()
            print("Doors closed.")

        elif name in waiting:
            # .pop() removes the guest AND returns their party size.
            size = waiting.pop(name)
            people_inside += size
            arrived.append(name)
            print(f"Welcome, {name}! Party of {size}.")

        elif name in arrived:
            # Already popped from waiting, so check arrived before saying
            # the guest isn't on the list.
            print(f"{name} is already inside.")

        else:
            print(f"Sorry, {name} is not on the list.")

    print_report(guest_list, arrived, people_inside)


def print_report(guest_list, arrived, people_inside):
    """Print the total head count and each guest's status."""
    print("\n--- Party report ---")
    print(f"People inside: {people_inside}")

    for name, size in guest_list.items():
        status = "arrived" if name in arrived else "no-show"
        print(f"{name} ({size}): {status}")


if __name__ == "__main__":
    main()
