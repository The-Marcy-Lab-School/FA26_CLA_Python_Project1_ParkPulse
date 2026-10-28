"""Week 2 practice 3: choose branches for the right reasons.

Practices: if / elif / else; guard clauses; truthiness and `is None`;
conditional expressions; rewriting nested ifs with guard clauses.
Matches the Week 2 deck slides 33-34, 36 and 38. Neutral examples (not ParkPulse).

Run it:  python3 practice/03_decisions.py
It runs before you change anything.

For each section: write your prediction on the "# Your prediction:" line,
then fill in every `None` marked `# TODO`, run again, and compare.
"""

# --- A. Which branch runs? (slide 33) ---
# Predict: which word prints when temperature is 18?
# Your prediction:
temperature = 18

if temperature > 30:
    print("hot")
elif temperature >= 15:
    print("mild")
else:
    print("cold")

# Predict: which word prints if you change temperature to 30? To 15? To 14?
# Try each one, run, then set it back to 18.
# Your prediction:
# Explain: would three separate `if` statements (no elif/else) print the same
# thing for every temperature? Why or why not?
# Your answer:


# --- B. Guard clause: less nesting (slide 36) ---
# Predict: what do the two prints show?
# Your prediction:
def reciprocal(value):
    if value == 0:
        return None
    return 1 / value


print(reciprocal(4))
print(reciprocal(0))
# Explain: why does the final return need no else?
# Your answer:


# --- C. Falsy versus missing (slide 38) ---
# Predict: True or False for each print?
# Your prediction:
reading = 0

print(reading is None)
print(not reading)

reading_is_missing = None  # TODO: replace None with the check that is True ONLY when reading is None (not when it is 0)
print("reading is missing:", reading_is_missing)
# Explain: why do the two checks disagree? When would `if not reading:` hide a
# real 0 reading?
# Your answer:


# --- D. Conditional expression (slide 34) ---
# Predict: which label prints?
# Your prediction:
score = 82
label = "pass" if score >= 70 else "retry"
print(label)

seats_left = 3
seat_label = None  # TODO: replace None with a conditional expression: "open" when seats_left is more than 0, otherwise "full"
print("seat label:", seat_label)


# --- E. Rewrite a nested conditional with guard clauses ---
# Predict: what do the three prints show?
# Your prediction:
def describe_order(quantity):
    if quantity is not None:
        if quantity > 0:
            return "ready"
        else:
            return "empty"
    else:
        return "missing"


print(describe_order(3))
print(describe_order(0))
print(describe_order(None))


def describe_order_guarded(quantity):
    """Same results as describe_order(), with guard clauses and no nesting."""
    # TODO: on the line above the return, add a guard clause for the "missing" case.
    # TODO: below that, add a second guard clause for the "empty" case.
    return None  # TODO: replace None with the value for a positive quantity


# These three prints must match the three describe_order() prints above.
print(describe_order_guarded(3))
print(describe_order_guarded(0))
print(describe_order_guarded(None))
