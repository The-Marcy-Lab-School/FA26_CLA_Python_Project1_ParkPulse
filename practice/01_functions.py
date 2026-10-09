"""Neutral functions lab (not ParkPulse). Matches the Week 2 deck slides 10, 13, 14."""

# PREDICT before running: write down every line this file prints.


# 1. Define, call, return (slide 10)
def add_tax(price, tax_rate):
    """Return total after tax."""
    return price * (1 + tax_rate)


print(add_tax(20, 0.05))


# 2. Defaults and keyword arguments (slide 13)
def label(name, prefix="Hello"):
    return f"{prefix}, {name}"


print(label("Kai"))
print(label("Kai", prefix="Welcome"))


# 3. Print versus return (slide 14)
def show_total(price):
    print(f"Total: {price}")


result = show_total(10)
print(result)


# A. In add_tax(20, 0.05), name the parameters and the arguments.
# B. What changes when the prefix argument is omitted? When it is passed by keyword?
# C. Why does the last line print None? What one change makes it print 10?
# D. Write your own neutral function with a docstring that RETURNS a value.
#    Call it twice with different arguments and print both results.
# E. TypeError: uncomment the next line, run, and read the last line of the error.
#    Then comment it back out.
# print(add_tax(20))
