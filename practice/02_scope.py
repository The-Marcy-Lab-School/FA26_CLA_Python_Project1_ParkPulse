"""Neutral scope and debugging lab (not ParkPulse). Matches the Week 2 deck slides 12, 16-19."""

# PREDICT before running: write down every line this file prints.


# 1. Nested calls (slide 12): which call runs first?
def double(value):
    return value * 2


def add_one(value):
    return value + 1


print(double(add_one(4)))


# 2. Local or global? (slide 16)
message = "outside"


def show_message():
    message = "inside"
    return message


print(show_message())
print(message)


# 3. NameError (slide 17)
def inspect_sample():
    observation = "ready"
    return observation


print(inspect_sample())


# 4. UnboundLocalError (slide 18)
counter = 5


def adjust():
    counter = counter + 1
    return counter


# A. Trace double(add_one(4)) from the inside out. Write the value after each call.
# B. List every local variable in this file and the function it belongs to.
# C. Explain why the two message lines print different values.
# D. NameError: uncomment the next line, predict the error, run, then comment it back out.
# print(observation)
# E. TypeError: uncomment the next line. Which part of the message tells you the cause?
# print(double(4, 5))
# F. UnboundLocalError: uncomment the next line. Why does assigning counter inside
#    adjust() make it local? Rewrite adjust() so it takes counter as a parameter
#    and returns the new value.
# print(adjust())
