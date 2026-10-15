"""Week 1 practice 3: names, constants, and PEP 8 style.

Practices: variables; ALL_CAPS constants; += and -=; snake_case; a PEP 8 rewrite.
Matches the Week 1 deck slides 30, 31, 32. Neutral example (a bus, not ParkPulse).

Run it:  python3 practice/03_names_style.py
It runs before you change anything.

For each section: write your prediction on the "# Your prediction:" line,
then fill in every `None` marked `# TODO`, run again, and compare.
"""

# --- A. Variables and augmented assignment (slide 30) ---
# Predict: the value current_passengers holds after EACH of the next three
# lines, and the two lines this section prints.
# Your prediction:
MAX_SEATS = 40
current_passengers = 30
current_passengers += 1
current_passengers -= 3
print(current_passengers)
print(f"{current_passengers}/{MAX_SEATS} seats used")

boarding = None  # TODO: replace None with how many passengers board at the next stop (any whole number)
print("boarding:", boarding)
# Uncomment the next two lines after you fill in boarding (adding None crashes).
# Predict the new value of current_passengers first.
# current_passengers += boarding
# print("after the next stop:", current_passengers)


# --- B. Constants are a naming convention (slide 30) ---
# Predict: does Python allow MAX_SEATS to change? What does the next print show?
# Your prediction:
MAX_SEATS = 50
print(MAX_SEATS)
# Explain: why does Python allow this? What does the ALL_CAPS name tell other
# developers? (JS recall: what would `const` do?)
# Your answer:


# --- C. PEP 8: style is readability (slides 31, 32) ---
# This block runs, but it is hard to read.
# Predict: the number it prints.
# Your prediction:
TotalCost=12.5;TaxRate=0.08
x=TotalCost*TaxRate
print( x+TotalCost )

# Your PEP 8 rewrite: snake_case names that say what each value is, spaces
# around operators, one statement per line, no semicolons.
total_cost = None  # TODO: replace None with the value TotalCost holds
tax_rate = None  # TODO: replace None with the value TaxRate holds
tax_amount = None  # TODO: replace None with total_cost times tax_rate, with a space on each side of *
print("total cost:", total_cost)
print("tax rate:", tax_rate)
print("tax amount:", tax_amount)
# Uncomment after you fill in tax_amount and total_cost (None + None crashes).
# It must print the same total as the hard-to-read block above:
# print(tax_amount + total_cost)

# Explain: which habits in the hard-to-read block come from JavaScript?
# Name one PEP 8 rule for each.
# Your answer:

# PEP 8 also requires four-space indentation. You will use it in Week 2,
# when `if` statements and functions arrive.
