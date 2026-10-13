"""
Week 3 practice 05: normalize a string, then index, slice, and inspect it.
Neutral practice (not ParkPulse). Matches deck slides 20 and 22.

Run it:  python3 practice/05_string_trace.py
It runs before you change anything.
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.
"""

# --- A. Normalize, then index and slice ---
# Predict: every printed line. The brackets show exactly where the string starts and ends.
label = "  East Gate  "
clean = label.strip().lower()
print("[" + clean + "]")
print(clean[0])
print(clean[0:4])
print(clean[-1])
print(len(clean))

raw_length = None  # TODO: replace None with len() of label (the original string, spaces included)
print("raw length:", raw_length)


# --- B. Your slice ---
# Predict: which index does the second word start at? (Count from 0.)
second_word = None  # TODO: replace None with a slice of clean that gives "gate"
print("second word:", second_word)


# --- C. Index errors and immutability ---
# Predict: what error does each commented line raise?
# Uncomment ONE line at a time, predict the error, run, then re-comment it.
# print(clean[20])
# clean[0] = "W"

# Strings can't change in place, so string methods return a NEW string.
renamed = None  # TODO: replace None with clean.replace(...) so the new string says "west" where clean says "east"
print("renamed:", renamed)
print("clean is still:", clean)


# --- D. String methods ---
# Predict: True/False, a number, or the new string for each line.
print("gate" in clean)
print(clean.startswith("east"))
print(clean.endswith("east"))
print(clean.find("gate"))
print(clean.upper())
print(clean.split())  # the [ ] brackets are a list; you'll learn lists in Week 4

has_space = None  # TODO: replace None with an expression using `in` that checks whether clean contains a space
print("has a space:", has_space)
