"""
Shopping Cart: practice combining lists, tuples, for loops and while loops.

Topics covered:
    - while True loops with break
    - if / elif / else to handle commands
    - tuples: storing (name, price, quantity) as one item
    - a list of tuples, with .append() and .pop()
    - tuple unpacking in a for loop, with enumerate()
    - converting input with float() and int()
    - a helper function that returns a value
    - formatting money with f"{amount:.2f}"

A shopping cart that keeps asking for commands until the user checks out.
Each item in the cart is stored as a tuple: (name, price, quantity).

Commands:
    add       add an item to the cart
    remove    remove an item by its number
    view      show the cart and the total
    checkout  show the final total and exit

Example run:

    Commands: add, remove, view, checkout
    Command: add
    Item: Apple
    Price: 0.50
    Quantity: 6
    Added: 6 x Apple
    Command: add
    Item: Bread
    Price: 2.25
    Quantity: 1
    Added: 1 x Bread
    Command: view
    1. Apple   6 x $0.50 = $3.00
    2. Bread   1 x $2.25 = $2.25
    Total: $5.25
    Command: remove
    Number to remove: 1
    Removed: Apple
    Command: remove
    Number to remove: 9
    No item number 9.
    Command: fly
    Unknown command: fly
    Command: checkout
    You bought 1 item(s). Total: $2.25. Thanks!
"""


def main():
    cart = []  # a list of tuples, e.g. [("Apple", 0.5, 6), ...]

    print("Commands: add, remove, view, checkout")

    # Keep asking for commands until the user types "checkout".
    while True:
        # .strip().lower() means " ADD " works the same as "add".
        command = input("Command: ").strip().lower()

        # "add": convert price and quantity to numbers, then group
        # all three values into ONE tuple and add it to the cart.
        if command == "add":
            name = input("Item: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            cart.append((name, price, quantity))
            print(f"Added: {quantity} x {name}")

        # "view": show every item, numbered from 1, then the total.
        elif command == "view":
            if len(cart) == 0:
                print("Your cart is empty.")
            else:
                # enumerate() gives a number for each item, and
                # (name, price, quantity) unpacks each tuple.
                for number, (name, price, quantity) in enumerate(cart, start=1):
                    print(f"{number}. {name}   {quantity} x ${price:.2f} = ${price * quantity:.2f}")
                print(f"Total: ${cart_total(cart):.2f}")

        # "remove": people count from 1, but list positions start at 0,
        # so item number 1 is cart[0].
        elif command == "remove":
            choice = int(input("Number to remove: "))
            if 1 <= choice <= len(cart):
                # .pop() removes the tuple and gives it back,
                # so removed[0] is the item's name.
                removed = cart.pop(choice - 1)
                print(f"Removed: {removed[0]}")
            else:
                print(f"No item number {choice}.")

        # "checkout": show the final total, then break out of the while loop.
        elif command == "checkout":
            print(f"You bought {len(cart)} item(s). Total: ${cart_total(cart):.2f}. Thanks!")
            break

        # Anything else is not a command we know.
        else:
            print(f"Unknown command: {command}")


def cart_total(cart):
    """Return the total price of every (name, price, quantity) tuple in cart."""
    total = 0
    for name, price, quantity in cart:
        total += price * quantity
    return total


# Run main() only when this file is run directly, not when it's imported.
if __name__ == "__main__":
    main()
