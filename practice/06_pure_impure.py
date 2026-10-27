"""
Week 4 practice 06: pure functions (copy first) vs impure functions (change the caller's list).
Neutral practice (not ParkPulse). Matches deck slide 32.

Run it:  python3 practice/06_pure_impure.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. Same goal, different side effects ---
# Predict: what are line and new after the two calls? Which function changed line?


def add_impure(line, guest):
    line.append(guest)


def add_pure(line, guest):
    return line + [guest]


line = ["Ana"]
add_impure(line, "Ben")
new = add_pure(line, "Cy")

print(line, new)


# --- B. Your turn: make it pure ---
# remove_first() should return a NEW list without the first guest
# and leave the caller's list alone.


def remove_first(queue):
    updated = queue.copy()
    updated.pop(0)
    return None  # TODO: replace None with the list this function should return


before = ["Dee", "Eli", "Fay"]
after = remove_first(before)
print("before:", before)
print("after:", after)
