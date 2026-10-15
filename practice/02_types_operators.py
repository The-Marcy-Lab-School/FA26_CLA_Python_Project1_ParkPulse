"""Week 1 practice 2: predict types and operator results before you run them.

Practices: type(); / vs. // vs. %; "3" * 5; floating-point surprises;
conversions with int(), str(), float(); == vs. is; and / or / not; in; TypeError.
Matches the Week 1 deck slides 20, 21, 24, 27. Neutral values (not ParkPulse).

Run it:  python3 practice/02_types_operators.py
It runs before you change anything.

For each section: write your prediction (value AND type) on the
"# Your prediction:" line or after "# prediction:", then fill in every `None`
marked `# TODO`, run again, and compare.
"""

# --- A. Data types: predict, then verify (slide 20) ---
# Predict: the type each line prints, for example <class 'str'>.
# Your prediction:
print(type("Coaster"))
print(type(24))
print(type(83.3))
print(type(True))
print(type(None))
print(type(["A", "B"]))
print(type({"ride": "A"}))


# --- B. Operator drill (slide 21) ---
# Predict: write the value and type after "prediction:" on each line.
print(24 / 5)            # prediction:
print(24 // 5)           # prediction:
print(24 % 5)            # prediction:
print("3" * 5)           # prediction:

# A ride car holds 5 riders and 24 people are waiting.
waiting = 24
car_size = 5
full_cars = None  # TODO: replace None with the expression that gives the number of FULL cars (use waiting and car_size)
riders_left_over = None  # TODO: replace None with the expression that gives the riders left over (use waiting and car_size)
print("full cars:", full_cars)
print("riders left over:", riders_left_over)


# --- C. Floating-point surprise (slide 21) ---
# Predict: True or False? Then predict what 0.1 + 0.2 really prints.
print(0.1 + 0.2 == 0.3)  # prediction:
print(0.1 + 0.2)         # prediction:
# Explain: why is the first line not what you might expect?
# Your answer:


# --- D. Conversions (slide 24) ---
# Predict: the value and type of each line.
print(int("7") + 3)       # prediction:
print("7" + str(3))       # prediction:
print(float("2.5") * 2)   # prediction:

# Predict: what error does "3" + 5 raise, and what does its last line say?
# Your prediction:
# Uncomment, predict the error, run, then re-comment.
# print("3" + 5)

# Fix "3" + 5 two ways:
number_sum = None  # TODO: replace None with "3" + 5 rewritten using int() so Python adds two numbers
text_join = None  # TODO: replace None with "3" + 5 rewritten using str() so Python joins two strings
print("with int():", number_sum)
print("with str():", text_join)


# --- E. Equality, identity, logic, membership (slide 27) ---
# Predict: True or False for each print in this section.
# Your prediction:
status = "open"
is_open = True
riders = 20
note = None
print(status == "open")
print(is_open and riders > 0)
print(not is_open or riders == 0)
print("coast" in "Coaster")
print(note is None)

# Predict: True or False for each of the last three prints.
# Your prediction:
first_list = ["A", "B"]
same_list = first_list
copy_list = ["A", "B"]
print(first_list == copy_list)
print(first_list is copy_list)
print(first_list is same_list)

has_riders = None  # TODO: replace None with an expression that is True when is_open is True AND riders is more than 0
print("open with riders:", has_riders)

# Explain: why is "coast" in "Coaster" False?
# Your answer:
# Explain: == versus is, using the last three list prints. JavaScript uses ===
# for strict equality. What does Python use instead, and what does `is` check?
# Your answer:
# JavaScript: rewrite the five status/riders prints above as JavaScript
# (and / or / not -> && || !). Which version is easier to read?
# Your answer:
