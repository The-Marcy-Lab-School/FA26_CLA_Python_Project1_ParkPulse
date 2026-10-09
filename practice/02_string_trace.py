"""Neutral strings lab (not ParkPulse)."""
message = "  Blue Notebook  "
clean = message.strip().lower()
print(clean)
print(clean[0])
print(clean[-1])
print(clean[:4])
print("note" in clean)
print(len(clean))

# A. Predict all outputs.
# B. Try an out-of-range index, explain IndexError.
# C. Try changing one character in place; explain immutability.
# D. Use startswith, endswith, find, upper, replace, split.
