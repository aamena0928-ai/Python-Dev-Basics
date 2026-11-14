"""
To-Do List: practice with tuples and while loops.

Topics covered:
    - while True loops with break
    - if / elif / else to handle commands
    - tuples: grouping related values into one item
    - a list of tuples
    - tuple unpacking in a for loop, with enumerate()
    - cleaning input with .strip().lower()

A small to-do list that keeps asking for commands until the user quits.
Each task is stored as a tuple: (task, priority).

Commands:
    add    add a new task
    list   show all tasks
    quit   exit the program

Example run:

    Commands: add, list, quit
    Command: add
    Task: Buy milk
    Priority (high/low): high
    Added: Buy milk
    Command: add
    Task: Finish CS50 problem set
    Priority (high/low): low
    Added: Finish CS50 problem set
    Command: list
    1. Buy milk [high]
    2. Finish CS50 problem set [low]
    Command: fly
    Unknown command: fly
    Command: quit
    Goodbye! You have 2 tasks.
"""


def main():
    tasks = []  # a list of tuples, e.g. [("Buy milk", "high"), ...]

    print("Commands: add, list, quit")

    # Keep asking for commands until the user types "quit".
    while True:
        # .strip().lower() means " ADD " works the same as "add".
        command = input("Command: ").strip().lower()

        # "add": group the task and its priority into ONE tuple.
        if command == "add":
            task = input("Task: ")
            priority = input("Priority (high/low): ")
            tasks.append((task, priority))
            print(f"Added: {task}")

        # "list": show every task, numbered from 1.
        elif command == "list":
            if len(tasks) == 0:
                print("No tasks yet.")
            else:
                # enumerate() gives a number for each item, and
                # (task, priority) unpacks each tuple into two variables.
                for number, (task, priority) in enumerate(tasks, start=1):
                    print(f"{number}. {task} [{priority}]")

        # "quit": say goodbye, then break out of the while loop.
        elif command == "quit":
            print(f"Goodbye! You have {len(tasks)} tasks.")
            break

        # Anything else is not a command we know.
        else:
            print(f"Unknown command: {command}")


# Run main() only when this file is run directly, not when it's imported.
if __name__ == "__main__":
    main()
