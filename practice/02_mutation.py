"""
Week 4 practice 02: methods that change a list in place.
Neutral practice (not ParkPulse). Matches deck slides 19 and 21.

Run it:  python3 practice/02_mutation.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. append, insert, pop, remove ---
# Predict: what is queue after each line? What does pop return?
# What does remove return?
queue = ["Ana", "Ben"]

queue.append("Cy")
queue.insert(0, "Dee")

first = queue.pop(0)
queue.remove("Ben")

print(first, queue)


# --- B. Methods that return None ---
# Predict: what does result hold? Did waits change?
waits = [15, 5, 30]

result = waits.sort()

print(result)
print(waits)


# --- C. Your turn ---
line = ["Kai", "Lux"]
removed = None  # TODO: replace None with a call that removes AND returns the last guest of line
print("removed:", removed)
print("line now:", line)

returned = None  # TODO: replace None with line.append("Mo"), then predict what returned holds
print("append returned:", returned)
print("line now:", line)
