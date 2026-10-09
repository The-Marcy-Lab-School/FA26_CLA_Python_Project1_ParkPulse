"""Neutral user-input lab (not ParkPulse)."""
response = input("Continue studying? [Y/N]: ")
normalized = response.strip().lower()
print(f"Normalized response: {normalized!r}")

# A. Try " Y ", "n", "", and "maybe": what is acceptable?
# B. Add your own conditional handling for accepted inputs.
# C. Ask for a quantity; predict the type returned by input().
# D. Validate BEFORE calling int() or float().
# E. Test "12", "-3", "3.5", " ", and "twelve".
# F. Explain the limits of isdigit().
