"""Neutral decisions lab (not ParkPulse). Matches the Week 2 deck slides 23-26."""

# PREDICT before running: write down every line this file prints.


# 1. Which branch runs? (slide 23)
temperature = 18

if temperature > 30:
    print("hot")
elif temperature >= 15:
    print("mild")
else:
    print("cold")


# 2. Guard clause (slide 24)
def reciprocal(value):
    if value == 0:
        return None
    return 1 / value


print(reciprocal(4))
print(reciprocal(0))


# 3. Falsy versus missing (slide 25)
reading = 0

print(reading is None)
print(not reading)


# 4. Conditional expression (slide 26)
score = 82
label = "pass" if score >= 70 else "retry"
print(label)


# 5. A nested conditional to rewrite
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


# A. Change temperature to 30, then 15, then 14. Predict the branch each time.
#    Would three separate if statements print the same thing? Why or why not?
# B. Why does reciprocal() need no else after its guard?
# C. reading is 0. Why do the two checks disagree? When would `if not reading:`
#    hide a real 0 reading?
# D. Rewrite describe_order() with guard clauses (early returns) and no nesting.
#    The three printed results must not change.
# E. Write your own conditional expression that picks between two labels.
