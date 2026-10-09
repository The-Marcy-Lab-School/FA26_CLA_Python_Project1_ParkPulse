"""Neutral naming and PEP 8 lab (not ParkPulse). Matches the Week 1 deck slides 20, 21."""

# PREDICT before running: write down every line this file prints.


# 1. Variables, constants, and augmented assignment (slide 20)
MAX_SEATS = 40
current_passengers = 30
current_passengers += 1
current_passengers -= 3
print(current_passengers)
print(f"{current_passengers}/{MAX_SEATS} seats used")

MAX_SEATS = 50
print(MAX_SEATS)


# 2. PEP 8: style is readability (slide 21)
# This block runs, but it is hard to read.
TotalCost=12.5;TaxRate=0.08
x=TotalCost*TaxRate
print( x+TotalCost )


# A. What value does current_passengers hold after each line in block 1?
#    What does += do?
# B. Python let MAX_SEATS change to 50. Why is that allowed? What does the
#    ALL_CAPS name tell other developers? (JS recall: what would `const` do?)
# C. Rewrite block 2 below this comment using PEP 8: snake_case names that say
#    what each value is, spaces around operators, one statement per line, no
#    semicolons, and no extra spaces inside print( ). Run the file again. The
#    two versions must print the same total.
# D. Which habits in block 2 come from JavaScript? Name one PEP 8 rule for each.
# E. PEP 8 also requires four-space indentation. You will use it in Week 2,
#    when `if` statements and functions arrive.
