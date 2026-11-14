"""
Phone Number Cleaner: practice with strings.

Topics covered:
    - looping through a string one character at a time
    - string methods (.isdigit(), .strip())
    - string slicing, including negative slices
    - f-strings
    - sorting items into two lists

People type phone numbers in many different ways. This program cleans
them all into one standard format (617-555-0123), hides all but the last
4 digits, and separates out the numbers that aren't valid.

Example output:

    Valid numbers:
      617-897-9986  (***-***-9986)
      617-555-0123  (***-***-0123)
      617-555-0199  (***-***-0199)
      617-555-0142  (***-***-0142)

    Invalid numbers:
      555-0100
      617-555-01234
      617-555-CALL
"""

# Phone numbers typed in different styles (some are not valid).
RAW_NUMBERS = [
    "617-897-9986",
    "(617) 555 0123",
    "6175550199",
    "  617.555.0142 ",
    "555-0100",       # too short
    "617-555-01234",  # too long
    "617-555-CALL",   # contains letters
]


def main():
    valid = []
    invalid = []

    # 1. Sort each number into valid or invalid.
    #    A valid phone number has exactly 10 digits.
    for num in RAW_NUMBERS:
        digits = digits_only(num)
        if len(digits) == 10:
            valid.append(format_number(digits))
        else:
            # Keep the number as the user typed it, without extra spaces.
            invalid.append(num.strip())

    # 2. Print the valid numbers, each with its masked version.
    print("Valid numbers:")
    for num in valid:
        print(f"  {num}  ({mask(num)})")

    # 3. Print the invalid numbers after a blank line.
    print()
    print("Invalid numbers:")
    for num in invalid:
        print(f"  {num}")


def digits_only(text):
    """Return only the digits in text: "(617) 555" -> "617555"."""
    # Loop through each character and keep it only if it is a digit.
    result = ""
    for char in text:
        if char.isdigit():
            result += char
    return result


def format_number(digits):
    """Return 10 digits as "XXX-XXX-XXXX": "6175550123" -> "617-555-0123"."""
    # Slice into 3 + 3 + 4 digits (the end number of a slice is not included).
    return f"{digits[0:3]}-{digits[3:6]}-{digits[6:]}"


def mask(number):
    """Hide all but the last 4 digits: "617-555-0123" -> "***-***-0123"."""
    # A negative slice counts from the end: [-4:] = the last 4 characters.
    return f"***-***-{number[-4:]}"


# Run main() only when this file is run directly, not when it's imported.
if __name__ == "__main__":
    main()
