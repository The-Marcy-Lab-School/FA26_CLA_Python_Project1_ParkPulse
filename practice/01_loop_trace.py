"""
Week 3 practice 01: trace for loops, range(), and a running total.
Neutral practice (not ParkPulse). Matches deck slides 1, 11, and 12.

Run it:  python3 practice/01_loop_trace.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. Count the iterations ---
# Predict: which values print? What is the first value? The last value?
for step in range(3):
    print(step)

iterations = None  # TODO: replace None with how many times the loop above ran (a number)
print("iterations:", iterations)


# --- B. Running total (accumulator) ---
# Predict: how many iterations? What are the first and last values of number?
# What is total after the loop ends?
total = 0
for number in range(1, 5):
    total += number
    print("added", number, "-> total is now", total)
print("final total:", total)


# --- C. A range with a step ---
# Predict: which numbers does range(2, 9, 3) produce? Why does 9 not print?
for number in range(2, 9, 3):
    print(number)


# --- D. Loop over a string with a running count ---
# Predict: what prints on each pass? What is letter_count at the end?
word = "loop"
letter_count = 0
for letter in word:
    print("letter:", letter)
    letter_count = None  # TODO: replace None with letter_count plus 1
print("letters counted:", letter_count)


# --- E. for or while? ---
# A for loop fits a known count. A while loop fits "repeat until a condition changes".
# Predict: how many times does the while loop below run? What changes the condition?
snacks_left = 3
while snacks_left > 0:
    print("eating a snack;", snacks_left, "left before this one")
    snacks_left = snacks_left - 1
print("no snacks left")

loop_for_menu = None  # TODO: replace None with "for" or "while": which loop fits "keep showing a menu until the user picks Exit"?
print("loop for a menu:", loop_for_menu)
