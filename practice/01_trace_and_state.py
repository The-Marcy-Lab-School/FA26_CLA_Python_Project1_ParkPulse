"""Neutral tracing lab (not ParkPulse). Matches the Week 1 deck slides 12, 14, 15."""

# PREDICT before running: write down every line this file prints, in order.


# 1. Default control flow: Python runs the file top to bottom (slide 12)
print("start")
seats = 40
passengers = 30
print(f"bus is {passengers / seats} full")
print("done")


# 2. Three kinds of lines (slide 14)
# This line is a comment. Python ignores it.
passengers + 5
passengers = passengers + 5
print(passengers)


# 3. print() and f-strings inspect state (slide 15)
print(f"{passengers}/{seats} seats used")
print(f"seats left: {seats - passengers}")


# A. Label every line in block 2 as a comment, an expression, or a statement.
# B. The line `passengers + 5` prints nothing. Why? Then explain why
#    print(passengers) shows 35 and not 30.
# C. Move print("done") to the very top of the file. Predict, run, then move it
#    back. What does this tell you about default control flow?
# D. Add one variable of your own (for example, a driver's name) and print it
#    inside an f-string together with `seats`.
# E. NameError: uncomment the next line, predict what happens, run, and read the
#    last line of the error. Then comment it back out.
# print(drivers)
