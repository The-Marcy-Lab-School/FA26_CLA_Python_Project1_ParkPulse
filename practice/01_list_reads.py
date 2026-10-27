"""
Week 4 practice 01: read a list with an index, a slice, in, and len().
Neutral practice (not ParkPulse). Matches deck slides 15 and 17.

Run it:  python3 practice/01_list_reads.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. Index, slice, in, len ---
# Predict: what does each print show? Which index ends the slice?
# Does any of these lines change the list?
rides = ["Sky Loop", "Drop",
         "Rapids", "Coaster"]

print(rides[1])

print(rides[1:3])

print("Drop" in rides)

print(len(rides))


# --- B. Zero-based indexing ---
# Predict: what do queue[3] and queue[-1] print? Why is the last index len(queue) - 1?
queue = ["Skyline", "Paper",
         "Neon", "Better"]

print(queue[3])

print(queue[-1])

print(len(queue) - 1)


# --- C. Your turn ---
# Use an index or a slice, not a loop, for each blank.
first_ride = None  # TODO: replace None with the first item of rides
last_two = None  # TODO: replace None with a slice of the last two items of rides
print("first:", first_ride)
print("last two:", last_two)

# Predict: what happens with rides[4]? (There are 4 items.)
# Uncomment, predict the error, run, then re-comment.
# print(rides[4])
