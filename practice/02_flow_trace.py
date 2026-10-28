"""
Week 3 practice 02: trace break and continue inside a loop.
Neutral practice (not ParkPulse). Matches deck slides 20 and 22.

Run it:  python3 practice/02_flow_trace.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. continue skips, break stops ---
# Predict: which numbers print? Which line ends the loop early?
for number in range(6):
    if number == 2:
        continue
    if number == 4:
        break
    print(number)
print("after the loop")


# --- B. break is not return ---
# Predict: for each call, does "loop finished" print? What value does the call return?
def first_multiple_of_three(limit):
    found = 0
    for number in range(1, limit):
        if number % 3 == 0:
            found = number
            break
    print("loop finished")
    return found


print(first_multiple_of_three(10))
print(first_multiple_of_three(3))


# --- C. Your turn: skip one value ---
# Predict: with skip_value still None, which numbers print?
skip_value = None  # TODO: replace None with the number to skip so this loop prints 0, 1, 2, 4
for number in range(5):
    if number == skip_value:
        continue
    print("C:", number)


# --- D. Your turn: stop early ---
# Predict: with stop_value still None, which numbers print?
stop_value = None  # TODO: replace None with the number that stops the loop so it prints only 0 and 1
for number in range(5):
    if number == stop_value:
        break
    print("D:", number)
