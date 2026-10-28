"""
Week 3 practice 06: input() always returns text. Clean it, check it, then convert it.
Neutral practice (not ParkPulse). Matches deck slides 34 and 36.

Run it:  python3 practice/06_input_trace.py
It runs before you change anything. It asks you 5 questions; pressing Enter
on every question is fine (nothing loops forever).
Fill in every `None` marked `# TODO`, run again, and compare with your predictions.

Run it several times and try these answers: spaces only, 12, -3, 3.5, twelve, " Y ", "n", "maybe".
"""

# --- A. input() returns a string ---
# Predict: if you type 12, what type does type(raw) show?
raw = input("Quantity: ")
print("you typed: [" + raw + "]")
print(type(raw))


# --- B. Validate before you convert ---
# Predict for each answer (spaces, 12, -3, 3.5): which ones print an amount?
clean = raw.strip()
print("cleaned: [" + clean + "]")
if clean.isdigit():
    amount = int(clean)
    print("amount:", amount)
else:
    print("not a whole number, so int() was never called")

isdigit_limit = None  # TODO: replace None with an answer (as a string) that is a real number but makes isdigit() return False
print("isdigit() says no to:", isdigit_limit)


# --- C. Normalize a Y/N answer ---
# Predict: which of " Y ", "y", "YES", "n", "maybe" print "continuing"?
answer = input("Continue? [Y/N]: ")
normalized = None  # TODO: replace None with answer with the spaces removed and lowercased (use .strip() and .lower())
print("normalized:", normalized)
if normalized == "y":
    print("continuing")
elif normalized == "n":
    print("stopping")
else:
    print("Please answer Y or N.")


# --- D. Retry until valid, at most 3 tries ---
# Predict: if you press Enter every time, how many times does it ask?
# What prints at the end? Which line guarantees this loop ends?
minutes = 0
for attempt in range(3):
    entry = input("Minutes studied: ").strip()
    if entry.isdigit():
        minutes = int(entry)
        break
    print("Please enter a whole number like 25.")
print("minutes:", minutes)

max_questions = None  # TODO: replace None with the most times section D can ask (a number)
print("section D asks at most:", max_questions)
