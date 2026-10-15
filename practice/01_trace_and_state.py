"""Week 1 practice 1: trace a file top to bottom and inspect state.

Practices: default (top-to-bottom) control flow; comments vs. expressions vs.
statements; print() and f-strings; reading a NameError.
Matches the Week 1 deck slides 13, 15, 18. Neutral example (a bus, not ParkPulse).

Run it:  python3 practice/01_trace_and_state.py
It runs before you change anything.

For each section: write your prediction on the "# Your prediction:" line,
then fill in every `None` marked `# TODO`, run again, and compare.
"""

# --- A. Default control flow: Python runs the file top to bottom (slide 13) ---
# Predict: write every line this section prints, in order.
# Your prediction:
print("start")
seats = 40
passengers = 30
print(f"bus is {passengers / seats} full")
print("done")

# Predict: if print("done") were the very first line of this file, where in
# the output would "done" appear? Try it: move print("done") to the top of the
# file, run, then move it back.
# Your prediction:


# --- B. Three kinds of lines: comment, expression, statement (slide 15) ---
# Predict: which of the next three lines prints something? What value does
# print(passengers) show, and why not 30?
# Your prediction:

# This line is a comment. Python ignores it.
passengers + 5
passengers = passengers + 5
print(passengers)

# Label each line above with "comment", "expression", or "statement" (as a string).
comment_line_kind = None  # TODO: replace None with the kind of line `# This line is a comment...` is
plus_five_kind = None  # TODO: replace None with the kind of line `passengers + 5` is
assignment_kind = None  # TODO: replace None with the kind of line `passengers = passengers + 5` is
print("comment line:", comment_line_kind)
print("passengers + 5:", plus_five_kind)
print("passengers = passengers + 5:", assignment_kind)
# Explain: `passengers + 5` prints nothing. Why?
# Your answer:


# --- C. print() and f-strings inspect state (slide 18) ---
# Predict: write both lines this section prints.
# Your prediction:
print(f"{passengers}/{seats} seats used")
print(f"seats left: {seats - passengers}")

seats_left = None  # TODO: replace None with an expression that uses seats and passengers (no typed-in numbers)
print("seats_left variable:", seats_left)


# --- D. Your own variable in an f-string ---
# Predict: after you fill in driver_name, what will the line below print?
# Your prediction:
driver_name = None  # TODO: replace None with a driver's name as a string, in quotes
print(f"{driver_name} drives a bus with {seats} seats")


# --- E. Read a NameError ---
# Predict: what happens when Python reaches a name that was never assigned?
# Which word on the last line of the error names the problem?
# Your prediction:
# Uncomment, predict the error, run, then re-comment.
# print(drivers)
