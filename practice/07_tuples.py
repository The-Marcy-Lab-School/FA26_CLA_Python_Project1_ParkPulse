"""
Week 4 practice 07: tuples, unpacking, and enumerate.
Neutral practice (not ParkPulse). Matches deck slide 37.

Run it:  python3 practice/07_tuples.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. Unpack every record ---
# Predict: what numbers print first on each line? What is rest?
rides = [
    ("Sky Loop", 24),
    ("Drop", 12),
]

for i, ride in enumerate(rides):
    name, cap = ride
    print(i + 1, name, cap)

first, *rest = rides
print(rest)


# --- B. Tuples don't change ---
# Predict the error. Uncomment, predict the error, run, then re-comment.
# rides[0][1] = 30


# --- C. Your turn ---
# Predict: with start=1, what number prints first? Why is `+ 1` gone?
for number, ride in enumerate(rides, start=1):
    name, cap = ride
    print(number, name, cap)

coaster = ("Comet Coaster", 30, 12, True)
name, max_capacity, riders, is_open = coaster
seats_left = None  # TODO: replace None with max_capacity minus riders
print(name, "seats left:", seats_left)
