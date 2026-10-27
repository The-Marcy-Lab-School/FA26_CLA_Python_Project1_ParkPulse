"""
Week 4 practice 03: a list of lists (2D list): row first, then column.
Neutral practice (not ParkPulse). Matches deck slide 23.

Run it:  python3 practice/03_2d_lists.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. Row, then column ---
# Predict: which index picks the row? How many lines does the loop print?
grid = [
    ["Sky", 24],
    ["Drop", 12],
]

print(grid[1][0])

for row in grid:
    print(row[0], row[1])


# --- B. Your turn ---
sky_seats = None  # TODO: replace None with the 24 from grid, using two indexes
print("Sky seats:", sky_seats)

total_seats = 0
for row in grid:
    total_seats = None  # TODO: replace None with total_seats plus this row's seats
print("total seats:", total_seats)
