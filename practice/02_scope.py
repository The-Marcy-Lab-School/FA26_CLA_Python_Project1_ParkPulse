"""Week 2 practice 2: trace nested calls and follow names across scope.

Practices: nested calls; local vs. global scope; reading NameError, TypeError,
and UnboundLocalError.
Matches the Week 2 deck slides 29, 33, 39 and 42-44. Neutral examples (not ParkPulse).

Run it:  python3 practice/02_scope.py
It runs before you change anything.

For each section: write your prediction on the "# Your prediction:" line,
then fill in every `None` marked `# TODO`, run again, and compare.
"""


# --- A. Nested calls: which call runs first? (slide 29) ---
# Predict: the value after each call in double(add_one(4)), from the inside
# out, and what the print shows.
# Your prediction:
def double(value):
    return value * 2


def add_one(value):
    return value + 1


print(double(add_one(4)))

# Trace it one call at a time.
inner_result = None  # TODO: replace None with the INNER call from the print above (just that call)
print("inner call:", inner_result)
# Uncomment after you fill in inner_result (double(None) crashes):
# print("outer call:", double(inner_result))


# --- B. Local or global? (slide 39) ---
# Predict: what do the two prints show? Why are they different?
# Your prediction:
message = "outside"


def show_message():
    message = "inside"
    return message


print(show_message())
print(message)

# Name the scope of each `message`, as a string: "local" or "global".
message_inside_function_scope = None  # TODO: replace None with the scope of message inside show_message()
message_at_top_scope = None  # TODO: replace None with the scope of message = "outside"
print("message in show_message():", message_inside_function_scope)
print('message = "outside":', message_at_top_scope)


# --- C. NameError: where is the name created, and where is it used? (slide 42) ---
def inspect_sample():
    observation = "ready"
    return observation


# Predict: what does this print?
# Your prediction:
print(inspect_sample())

# Predict: observation was created inside inspect_sample(). What happens if
# you use it out here?
# Your prediction:
# Uncomment, predict the error, run, then re-comment.
# print(observation)

observation_value = None  # TODO: replace None with a call that gets observation's value without a NameError
print("observation:", observation_value)


# --- D. TypeError: wrong argument count (slide 33) ---
# Predict: double takes one argument. What happens with two? Which part of
# the error message tells you the cause?
# Your prediction:
# Uncomment, predict the error, run, then re-comment.
# print(double(4, 5))


# --- E. UnboundLocalError (slides 43-44) ---
counter = 5


def adjust():
    counter = counter + 1
    return counter


# Predict: counter is 5 out here. What happens when adjust() runs, and why
# does assigning counter inside adjust() make it local?
# Your prediction:
# Uncomment, predict the error, run, then re-comment.
# print(adjust())


# The fix: take counter as a parameter and return the new value.
def adjust_counter(counter):
    """Return counter plus 1."""
    return None  # TODO: replace None with the new value: counter plus 1


# Predict: what do these two lines print after you fill in adjust_counter?
# Does the global counter change?
# Your prediction:
print(adjust_counter(counter))
print(counter)

# Explain: list every local variable in this file and the function it belongs to.
# Your answer:
