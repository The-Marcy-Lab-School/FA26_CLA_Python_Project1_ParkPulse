"""
Week 3 practice 07: what you display vs what you store (:.2f vs round()), plus print's sep and end.
Neutral practice (not ParkPulse). Matches deck slides 30 and 31.

Run it:  python3 practice/07_format_trace.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. Display vs stored value ---
# Predict: what does each line show? Which lines change the value, and which only change the display?
rate = 7 / 3
print(f"{rate:.2f}")
print(round(rate, 2))
print(rate)
print(type(f"{rate:.2f}"))
print(type(round(rate, 2)))


# --- B. Why it matters when you keep calculating ---
# Predict: do these two lines show the same number? Why or why not?
rounded = round(rate, 2)
print(rounded * 3)
print(f"{rate * 3:.2f}")

three_places = None  # TODO: replace None with an f-string that displays rate with 3 decimal places
print("three places:", three_places)

# Recall from Week 1: :.2% shows a fraction as a percentage.
print(f"{5 / 8:.2%}")


# --- C. sep and end ---
# Predict: every printed line, including where each line break happens.
print("A", "B", "C", sep=" | ")
print("First", end=" ")
print("second")
for step in range(3):
    print(step, end=" ")
print()

separator = None  # TODO: replace None with the string that makes the next line print 9:30:00
print("9", "30", "00", sep=separator)

ending = None  # TODO: replace None with the string that makes the next two prints show Loading...done on one line
print("Loading...", end=ending)
print("done")
