"""
Week 4 practice 05: two names, one list (aliasing) vs a real copy.
Neutral practice (not ParkPulse). Matches deck slides 1, 30 and 34.

Run it:  python3 practice/05_aliasing.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. The title slide ---
# Predict: what does print(a) show? b = a did not copy anything.
a = ["Sky Loop"]
b = a
b.append("Drop")

print(a)


# --- B. Alias vs copy ---
# Predict both lists before you run.
park = ["Sky Loop", "Drop"]

alias = park
backup = park.copy()

alias.append("Rapids")

print(park)
print(backup)


# --- C. Your turn ---
# Predict: which names point at the same list?
x = [1, 2]
y = x
z = x.copy()
z.append(3)

same_list_y = None  # TODO: replace None with True or False: is y the same list as x?
same_list_z = None  # TODO: replace None with True or False: is z the same list as x?
print("y shares x:", same_list_y)
print("z shares x:", same_list_z)
# After you fill in both, check yourself: add print(y is x, z is x) and run again.
