"""Neutral formatting lab (not ParkPulse)."""
measurement = 7 / 3
print(f"Shown with two places: {measurement:.2f}")
print("Stored value:", measurement)
print("A", "B", "C", sep=" | ")
print("First", end=" ")
print("second")

# A. Predict every line.
# B. Explain :.2f versus round(measurement, 2).
# C. Change sep and end to alter output.
# D. Write your own neutral f-string.
