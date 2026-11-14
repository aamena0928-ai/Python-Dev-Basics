"""
Grade Report: practice with lists and for loops.

Topics covered:
    - for loops
    - lists and list methods (.append(), sorted())
    - len() and a running total
    - finding the highest / lowest value with a "best so far" loop
    - list comprehensions
    - if / elif / else inside a function

The program prints each test score with its letter grade, adds a late
score, then prints a summary of the class.

Example output:

    Score 85: B
    Score 92: A
    Score 67: D
    Score 74: C
    Score 58: F
    Score 99: A

    Number of scores: 7
    Average: 79.3
    Highest: 99
    Lowest: 58
    Sorted: [58, 67, 74, 80, 85, 92, 99]
    Passed (70+): [85, 92, 74, 99, 80]
"""

# Constants are written in CAPITALS so it's clear they are fixed settings.
SCORES = [85, 92, 67, 74, 58, 99]
PASS_MARK = 70


def main():
    # 1. Print every score with its letter grade.
    for score in SCORES:
        print(f"Score {score}: {letter_grade(score)}")

    # 2. A late test came in: .append() adds it to the end of the list.
    SCORES.append(80)

    # 3. Count the scores and work out the average.
    #    "\n" prints a blank line first, to separate the summary.
    print(f"\nNumber of scores: {len(SCORES)}")

    total = 0  # running total: start at 0 BEFORE the loop
    for score in SCORES:
        total += score

    average = total / len(SCORES)
    print(f"Average: {round(average, 1)}")

    # 4. Find the highest and lowest score with a "best so far" loop.
    #    Start with the first score, then replace it whenever a
    #    bigger (or smaller) one turns up.
    #    (Python's built-in max() and min() do the same thing.)
    highest = SCORES[0]
    lowest = SCORES[0]

    for score in SCORES:
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score

    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")

    # 5. Print the scores from lowest to highest.
    #    sorted() returns a NEW sorted list and leaves SCORES unchanged.
    #    (SCORES.sort() would change the list itself and return None.)
    print(f"Sorted: {sorted(SCORES)}")

    # 6. List comprehension: keep only the scores that passed.
    passed = [score for score in SCORES if score >= PASS_MARK]
    print(f"Passed ({PASS_MARK}+): {passed}")


def letter_grade(score):
    """Return "A", "B", "C", "D" or "F" for a score from 0 to 100."""
    # Check the highest grade first: the first condition that is True wins.
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Run main() only when this file is run directly, not when it's imported.
if __name__ == "__main__":
    main()
