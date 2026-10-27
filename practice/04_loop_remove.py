"""
Week 4 practice 04: why removing from a list while you loop over it skips items.
Neutral practice (not ParkPulse). Matches deck slide 25.

Run it:  python3 practice/04_loop_remove.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. The bug ---
# Predict: do both "Ana"s leave the list? If not, which item was skipped, and why?
waiting = ["Ana", "Ana", "Ben"]

for guest in waiting:
    if guest == "Ana":
        waiting.remove(guest)

print(waiting)


# --- B. Fix 1: loop over a copy ---
# Predict: does looping over a copy fix it? Which list changes?
waiting = ["Ana", "Ana", "Ben"]

for guest in waiting.copy():
    if guest == "Ana":
        waiting.remove(guest)

print(waiting)


# --- C. Fix 2: build a new list ---
waiting = ["Ana", "Ana", "Ben"]
staying = []

for guest in waiting:
    if guest != "Ana":
        staying.append(None)  # TODO: replace None with the guest who stays

print(staying)
print(waiting)
