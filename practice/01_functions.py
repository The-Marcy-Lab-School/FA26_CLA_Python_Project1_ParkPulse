"""Week 2 practice 1: define, call, and return from functions.

Practices: def; parameters vs. arguments; default and keyword arguments;
return values; print vs. return; a TypeError from a wrong argument count.
Matches the Week 2 deck slides 24, 26-27, 30 and 33. Neutral examples (not ParkPulse).

Run it:  python3 practice/01_functions.py
It runs before you change anything.

For each section: write your prediction on the "# Your prediction:" line,
then fill in every `None` marked `# TODO`, run again, and compare.
"""


# --- A. Define, call, return (slide 24) ---
# Predict: what does the print below show?
# Your prediction:
def add_tax(price, tax_rate):
    """Return total after tax."""
    return price * (1 + tax_rate)


print(add_tax(20, 0.05))

# In add_tax(20, 0.05), name the parameters and the arguments.
first_parameter = None  # TODO: replace None with the name of add_tax's first parameter, as a string
first_argument = None  # TODO: replace None with the first argument passed in add_tax(20, 0.05)
print("first parameter:", first_parameter)
print("first argument:", first_argument)


# --- B. Defaults and keyword arguments (slide 30) ---
# Predict: what do the two prints show? What changes when prefix is omitted,
# and when it is passed by keyword?
# Your prediction:
def label(name, prefix="Hello"):
    return f"{prefix}, {name}"


print(label("Kai"))
print(label("Kai", prefix="Welcome"))

my_greeting = None  # TODO: replace None with a call to label() that passes your own name and prefix="Hi" by keyword
print(my_greeting)


# --- C. Print versus return (slides 26-27) ---
# Predict: show_total(10) prints a line. What does print(result) show after it, and why?
# Your prediction:
def show_total(price):
    print(f"Total: {price}")


result = show_total(10)
print(result)


# The same idea, written to RETURN instead of print.
def get_total(price):
    """Return the price so the caller can use it."""
    return None  # TODO: replace None with price


# Predict: after you fill in get_total, what does this print?
# Your prediction:
print(get_total(10))


# --- D. Your own function ---
# Write a neutral function (not ParkPulse) that RETURNS a value.
def your_function(value):
    """TODO: replace this sentence with one sentence saying what your function returns."""
    return None  # TODO: replace None with an expression that uses value, for example value times 3


# Predict: what will the two calls below print after you fill in your_function?
# Your prediction:
print(your_function(4))
print(your_function(10))


# --- E. Wrong argument count: TypeError (slide 33) ---
# Predict: add_tax needs two arguments. What happens when it gets one?
# Which part of the last line of the error tells you the cause?
# Your prediction:
# Uncomment, predict the error, run, then re-comment.
# print(add_tax(20))
