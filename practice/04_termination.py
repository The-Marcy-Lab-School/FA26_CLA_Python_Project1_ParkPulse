"""
Week 3 practice 04: why a while loop ends (or doesn't).
Neutral practice (not ParkPulse). Matches deck slides 26-27.

Run it:  python3 practice/04_termination.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.

If a loop never stops, press Ctrl+C in the terminal to end the program.
"""

# --- A. The runaway loop from the slide ---
# Predict: what is missing? What happens if this loop runs?
# Uncomment the three lines below, predict, run, then press Ctrl+C to stop it.
# Re-comment them before you go on.
# attempts = 0
# while attempts < 3:
#     print("checking")


# --- B. Make the loop end ---
# Predict: once step is filled in, how many times does "checking" print?
# What is attempts after the loop?
step = None  # TODO: replace None with how much attempts should grow on each pass (a whole number)
attempts = 0
while attempts < 3:
    print("checking, attempts =", attempts)
    if step is None:
        print("step is still None, so attempts never changes. Stopping early with break.")
        break
    attempts = attempts + step
print("attempts after the loop:", attempts)
# Then: set step to 0. Predict first, run, and press Ctrl+C when it doesn't stop.
# Put your working value back before you go on.


# --- C. A stopping point you can't see in advance ---
# Predict: how many times does value get cut in half before the loop stops?
value = 20
halvings = 0
while value >= 1:
    value = value / 2
    halvings = halvings + 1
print("halvings:", halvings)

ending_line = None  # TODO: replace None with the line from section C (as a string) that makes `value >= 1` eventually False
print("the line that ends loop C:", ending_line)
