"""
Pantry Manager: practice everything so far, plus raising and handling exceptions.

Topics covered (review):
    - variables, functions, return values and calling functions
    - side effects: functions that change a dictionary passed in
    - dictionaries: .get(), .items(), .pop(), .copy()
    - tuples as dictionary values: {"rice": (price, quantity)}
    - lists: building one with .append(), joining with ", ".join()
    - for loops with enumerate(), while True with break / continue
    - if / elif / else to handle commands
    - strings: .strip().lower(), .title(), f-strings, f"{price:.2f}"
    - a default parameter: def low_stock(pantry, limit=3)

New topics:
    - try / except ValueError       (bad text typed in, e.g. "abc")
    - try / except KeyError         (looking up a key that isn't in a dictionary)
    - try / except / else           (else runs only when nothing went wrong)
    - pass inside a while loop      (ignore the error and ask again)
    - raise ValueError("...")       (a function reports a bad value)
    - raise Exception("...")        (a function reports a general problem)
    - calling a function that raises, and catching the error in the caller
    - ordering except blocks: ValueError before Exception

The pantry is a dictionary. Each key is an item name, and each value is
a tuple (price, quantity), e.g. {"rice": (2.50, 4), "beans": (0.90, 10)}.

Commands:
    add    add some of an item (adds to the quantity if it's already there)
    use    use some of an item (removes it when it reaches 0)
    list   show every item and the pantry's total value
    low    show items with fewer than 3 left
    quit   exit the program

Example run:

    Commands: add, use, list, low, quit
    Command: list
    1. Rice     4 x $2.50
    2. Beans    10 x $0.90
    Pantry value: $19.00
    Command: add
    Item: pasta
    Price: 1.20
    Quantity: abc
    Quantity: 2
    Added: 2 x Pasta
    Command: add
    Item: rice
    Price: 2.50
    Quantity: 0
    Quantity must be more than 0.
    Command: use
    Item: rice
    How many: 9
    Can't do that: only 4 rice left.
    Command: use
    Item: cheese
    How many: 1
    No cheese in the pantry.
    Command: use
    Item: rice
    How many: 2
    Used 2 rice. 2 left.
    Command: low
    Running low: Rice, Pasta
    Command: fly
    Unknown command: fly
    Command: quit
    Goodbye! 3 item(s) in the pantry.
"""


# The pantry the program starts with. main() works on a .copy() so this
# dictionary is never changed (see side effects in 04_side_effects.py).
STARTING_PANTRY = {"rice": (2.50, 4), "beans": (0.90, 10)}


def read_whole_number(prompt):
    """Keep asking until the user types a whole number, then return it."""
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            # int("abc") raises a ValueError. pass ignores it,
            # so the while loop simply asks again.
            pass
        else:
            # else only runs when the try block raised no error.
            return number


def check_quantity(quantity):
    """Raise a ValueError if quantity is 0 or less."""
    if quantity <= 0:
        # raise stops this function and sends the error to the caller.
        raise ValueError("Quantity must be more than 0.")


def add_item(pantry, name, price, quantity):
    """Add quantity of an item to the pantry (changes the pantry in place)."""
    # If check_quantity raises, add_item stops here too and the
    # error goes up to main(), which catches it.
    check_quantity(quantity)

    # .get() returns the item's (price, quantity) tuple, or the default
    # (price, 0) when the item is new, so one line handles both cases.
    old_price, old_quantity = pantry.get(name, (price, 0))
    pantry[name] = (price, old_quantity + quantity)


def use_item(pantry, name, amount):
    """Use some of an item and return how many are left.

    Raises:
        KeyError: the item isn't in the pantry.
        ValueError: amount is 0 or less.
        Exception: there isn't enough of the item.
    """
    # pantry[name] (not .get()) raises a KeyError if name is missing.
    price, have = pantry[name]
    check_quantity(amount)

    if amount > have:
        raise Exception(f"only {have} {name} left.")

    remaining = have - amount
    if remaining == 0:
        pantry.pop(name)  # none left, so remove the item completely
    else:
        pantry[name] = (price, remaining)  # tuples can't change, so store a new one
    return remaining


def pantry_value(pantry):
    """Return the total value of the pantry: price * quantity for each item."""
    total = 0
    # .items() gives (name, (price, quantity)), unpacked in one step.
    for name, (price, quantity) in pantry.items():
        total += price * quantity
    return total


def low_stock(pantry, limit=3):
    """Return a list of item names with fewer than limit left."""
    low = []
    for name, (price, quantity) in pantry.items():
        if quantity < limit:
            low.append(name.title())
    return low


def format_line(number, name, price, quantity):
    """Return one line for the list command, e.g. "1. Rice     4 x $2.50"."""
    # :<8 pads the name to 8 characters so the columns line up,
    # and :.2f shows the price with 2 decimal places.
    return f"{number}. {name.title():<8} {quantity} x ${price:.2f}"


def main():
    pantry = STARTING_PANTRY.copy()

    print("Commands: add, use, list, low, quit")

    # Keep asking for commands until the user types "quit".
    while True:
        # .strip().lower() means " ADD " works the same as "add".
        command = input("Command: ").strip().lower()

        if command == "add":
            name = input("Item: ").strip().lower()

            # float("abc") raises a ValueError. continue skips the rest
            # of "add" and goes straight back to "Command:".
            try:
                price = float(input("Price: "))
            except ValueError:
                print("Price must be a number.")
                continue

            quantity = read_whole_number("Quantity: ")

            # add_item raises a ValueError (from check_quantity) for 0 or less.
            # "as error" holds the message, so print(error) shows it.
            try:
                add_item(pantry, name, price, quantity)
            except ValueError as error:
                print(error)
            else:
                print(f"Added: {quantity} x {name.title()}")

        elif command == "use":
            name = input("Item: ").strip().lower()
            amount = read_whole_number("How many: ")

            # use_item can raise three different errors, one except for each.
            # except Exception must come LAST: every error is a kind of
            # Exception, so if it came first the other blocks would never run.
            try:
                left = use_item(pantry, name, amount)
            except KeyError:
                print(f"No {name} in the pantry.")
            except ValueError as error:
                print(error)
            except Exception as error:
                print(f"Can't do that: {error}")
            else:
                print(f"Used {amount} {name}. {left} left.")

        elif command == "list":
            # A tuple inside a tuple: .items() gives (name, (price, quantity)),
            # and enumerate() wraps that in (number, ...).
            for number, (name, (price, quantity)) in enumerate(pantry.items(), start=1):
                print(format_line(number, name, price, quantity))
            print(f"Pantry value: ${pantry_value(pantry):.2f}")

        elif command == "low":
            low = low_stock(pantry)
            if len(low) == 0:
                print("Nothing is running low.")
            else:
                # ", ".join() turns ["Rice", "Pasta"] into "Rice, Pasta".
                print("Running low: " + ", ".join(low))

        elif command == "quit":
            print(f"Goodbye! {len(pantry)} item(s) in the pantry.")
            break

        # Anything else is not a command we know.
        else:
            print(f"Unknown command: {command}")


# Run main() only when this file is run directly, not when it's imported.
if __name__ == "__main__":
    main()
