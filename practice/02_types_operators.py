"""Neutral types and operators lab (not ParkPulse). Matches the Week 1 deck slides 17, 18, 19."""

# PREDICT before running: for every print, write down the value AND its type.


# 1. Data types: predict, then verify (slide 17)
print(type("Coaster"))
print(type(24))
print(type(83.3))
print(type(True))
print(type(None))
print(type(["A", "B"]))
print(type({"ride": "A"}))


# 2. Operator drill (slide 18). Write your prediction in the comment first.
print(24 / 5)            # prediction:
print(24 // 5)           # prediction:
print(24 % 5)            # prediction:
print("3" * 5)           # prediction:
print(0.1 + 0.2 == 0.3)  # prediction:
print(0.1 + 0.2)         # prediction:


# 3. Conversions
print(int("7") + 3)
print("7" + str(3))
print(float("2.5") * 2)


# 4. Equality, identity, logic, membership (slide 19)
status = "open"
is_open = True
riders = 20
note = None
print(status == "open")
print(is_open and riders > 0)
print(not is_open or riders == 0)
print("coast" in "Coaster")
print(note is None)

first_list = ["A", "B"]
same_list = first_list
copy_list = ["A", "B"]
print(first_list == copy_list)
print(first_list is copy_list)
print(first_list is same_list)


# A. Which printed line surprised you most? Explain it in one sentence.
# B. Explain the difference between / and //. A ride car holds 5 riders and 24
#    people are waiting: which operator gives the number of full cars, and which
#    gives the riders left over?
# C. Why is 0.1 + 0.2 == 0.3 False? What does the next print show you?
# D. Why is "coast" in "Coaster" False?
# E. Explain == versus is using the last three prints. JavaScript uses === for
#    strict equality. What does Python use instead, and what does `is` check?
# F. Rewrite the block 4 prints as JavaScript in a comment
#    (and/or/not -> && || !). Then explain which version is easier to read.
# G. TypeError: uncomment the next line, predict what happens, run, and read the
#    last line of the error. Fix it two ways (with int() and with str()), then
#    comment the original line back out.
# print("3" + 5)
