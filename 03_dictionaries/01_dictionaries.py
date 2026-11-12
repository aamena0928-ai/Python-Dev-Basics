"""
Working with dictionaries: storing, updating and looping through data.

Topics covered:
    - Creating a dictionary and reading values by key
    - Changing an existing value and adding a new key
    - Adding several keys at once with .update()
    - Looking up keys safely with .get() and a default value
    - Looping through a dictionary with .keys(), .values() and .items()
    - Finding the largest value with a "best so far" loop

Usage:
    python 01_dictionaries.py
"""


# =============================================================================
# CONCEPT: DICTIONARIES
# =============================================================================
# A dictionary stores data as KEY -> VALUE pairs, so each value can be found
# by a meaningful name instead of a position number:
#
#     book = {"title": "The Hobbit", "pages": 310}
#     book["title"]      -> "The Hobbit"
#
# Keys are case-sensitive: "pages" and "Pages" are two different keys.
#
# Part 1 works with ONE record (a single book).
# Part 2 works with a dictionary of MANY items (a whole library).


def main():
    """Run both parts of the program."""
    book_report()
    library_report()


# =============================================================================
# PART 1: ONE BOOK (create, change, add, .update(), .get())
# =============================================================================
def book_report():
    """Build one book's dictionary, update it, and print its report card."""
    # Create a dictionary with four key -> value pairs.
    book = {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "pages": 310,
    }

    # CHANGE a value: assigning to a key that already exists replaces it.
    # The original value is printed first, so the change is visible.
    print(f"Pages (original): {book['pages']}")
    book["pages"] = 320

    # ADD a key: assigning to a key that doesn't exist creates it.
    book["rating"] = "5/5"

    # .update() adds (or replaces) several keys in one call.
    book.update({"publisher": "George Allen & Unwin", "genre": "Fantasy"})

    print(format_book(book))


def format_book(book):
    """Return a formatted report card for a book dictionary.

    .get(key, "Unknown") returns the default instead of raising a KeyError
    when a key is missing, so the report never crashes on incomplete data.
    """
    return f"""
===============REPORT=================
Title:     {book.get("title", "Unknown")}
Author:    {book.get("author", "Unknown")}
Year:      {book.get("year", "Unknown")}
Pages:     {book.get("pages", "Unknown")}
Rating:    {book.get("rating", "Unknown")}
Publisher: {book.get("publisher", "Unknown")}
Genre:     {book.get("genre", "Unknown")}
======================================
"""


# =============================================================================
# PART 2: MANY BOOKS (.keys(), .values(), .items())
# =============================================================================
def library_report():
    """List the library's books, total their pages, and find the longest."""
    # Each key is a book title; each value is its number of pages.
    library = {
        "The Hobbit": 320,
        "Matilda": 240,
        "Dune": 412,
        "Wonder": 310,
    }

    # .keys() -> one title per loop.
    # The heading is printed BEFORE the loop so it appears only once.
    print("Books in my library:")
    for title in library.keys():
        print(f"  {title}")

    # .values() -> one page count per loop.
    # A running total starts at 0 before the loop and grows each round;
    # it is printed AFTER the loop, once the total is complete.
    total = 0
    for pages in library.values():
        total = total + pages
    print(f"\nTotal pages: {total}\n")

    # .items() -> the key AND the value together, unpacked into two variables.
    for title, pages in library.items():
        print(f"{title} has {pages} pages")

    # Find the longest book with .items().
    # Keep a "best so far" title and page count. Each round, if the current
    # book has more pages than the best so far, it becomes the new best.
    # If two books tie, the first one found is kept (> rather than >=).
    longest_title = ""
    most_pages = 0
    for title, pages in library.items():
        if pages > most_pages:
            longest_title = title
            most_pages = pages
    print(f"\nLongest book: {longest_title} ({most_pages} pages)")


if __name__ == "__main__":
    main()
