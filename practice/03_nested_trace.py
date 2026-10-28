"""
Week 3 practice 03: count the work in a nested loop.
Neutral practice (not ParkPulse). Matches deck slide 24.

Run it:  python3 practice/03_nested_trace.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. Predict the pairs (2 x 3) ---
# Predict without running: write every (row, col) pair in the order it prints.
# How many lines print in total?
for row in range(2):
    for col in range(3):
        print(row, col)

total_prints = None  # TODO: replace None with how many times print(row, col) ran (a number)
print("total prints:", total_prints)


# --- B. Check your count with a running count ---
# Predict: what is count after both loops finish?
count = 0
for row in range(2):
    for col in range(3):
        count = None  # TODO: replace None with count plus 1
print("counted:", count)


# --- C. Change the shape ---
# Predict: what does each printed line look like? How many lines print?
rows = 3
cols = 4
for row in range(rows):
    line = ""
    for col in range(cols):
        line = line + "*"
    print(line)

stars = None  # TODO: replace None with an expression using rows and cols that gives the total number of * printed
print("stars printed:", stars)
