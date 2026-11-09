"""
ParkPulse — Week 1

Project context:
ParkPulse helps amusement park staff quickly understand the current
status of an attraction.

Week 1 feature:
Use Python variables, expressions, and formatted output to calculate
and display one attraction's utilization.

Attraction data:
- Name: Sky Loop
- Maximum capacity: 24 riders
- Current riders: 20
- Open: yes
"""

# Step 1: store the attraction data in snake_case variables.
# str for the name, int for the rider counts, bool for open/closed.
ride_name = "Sky Loop"
max_capacity = 24
current_riders = 20
is_open = True


# Step 2: calculate utilization (current riders divided by maximum capacity).
# Week 2 Task A moved the calculation into a function that RETURNS the value.
def calculate_utilization(riders, capacity):
    """
    Return the share of seats in use, as a float.

    Parameters:
        riders: Current rider count.
        capacity: Maximum allowed riders.

    Returns:
        riders / capacity (20 / 24 -> 0.8333333333333334).
    """
    return riders / capacity


utilization = calculate_utilization(current_riders, max_capacity)

# Step 3: display a readable status message.
# :.2% multiplies the fraction by 100, rounds to 2 decimals, and adds %.
print(f"Ride: {ride_name}")
print(f"Open: {is_open}")
print(f"Capacity used: {current_riders}/{max_capacity}")
print(f"Utilization: {utilization:.2%}")

# Step 4: style review (PEP 8).
# snake_case names, spaces around operators, one statement per line,
# no semicolons or braces.


# ===================================================
# PARKPULSE — WEEK 2: FUNCTIONS, SCOPE & DECISIONS
# ===================================================
#
# Keep all completed Week 1 code above.
#
# Week 2 objectives:
# - Refactor repeated logic into functions
# - Practice parameters, arguments, and returns
# - Use conditional statements and guard clauses
# - Preserve working Week 1 functionality
#
# The rule values below match the Business Rules
# table in the Week 2 README.

sky_loop_min_height = 48
adult_base_price = 60.00


# ---------------------------------------------------
# FEATURE 1: RIDE ELIGIBILITY
# ---------------------------------------------------

def check_ride_eligibility(visitor_height, minimum_height):
    """
    Determine whether a visitor is tall enough to ride.

    Parameters:
        visitor_height: The visitor's height in inches.
        minimum_height: The ride's minimum height in inches
            (Sky Loop: 48 inches).

    Returns:
        True if eligible, False if too short,
        None if an input is missing or invalid.

    Eligibility rule:
        - visitor_height >= minimum_height -> True
          (exactly 48 inches on Sky Loop is eligible)
        - visitor_height < minimum_height -> False
        - either value is None, 0, or negative -> None
    """
    if visitor_height is None or minimum_height is None:
        return None
    if visitor_height <= 0 or minimum_height <= 0:
        return None
    if visitor_height >= minimum_height:
        return True
    return False


# ---------------------------------------------------
# FEATURE 2: TICKET PRICING
# ---------------------------------------------------

def calculate_ticket_price(ticket_type, base_price):
    """
    Determine a ticket price from its category.

    Parameters:
        ticket_type: "adult", "child", or "senior"
            (lowercase, exactly as written).
        base_price: The adult price in dollars
            (ParkPulse uses $60.00).

    Returns:
        The price as a number, or None for an
        unknown category or an invalid base price.

    Pricing rules:
        - "adult"  -> 100% of base_price  ($60.00)
        - "child"  -> 50% of base_price   ($30.00)
        - "senior" -> 75% of base_price   ($45.00)
        - any other ticket_type -> None
        - base_price is None, 0, or negative -> None
    """
    if base_price is None or base_price <= 0:
        return None

    if ticket_type == "adult":
        return base_price
    elif ticket_type == "child":
        return base_price * 0.5
    elif ticket_type == "senior":
        return base_price * 0.75
    else:
        return None


# ---------------------------------------------------
# FEATURE 3: CAPACITY RULES
# ---------------------------------------------------

def check_capacity(current_riders, max_capacity):
    """
    Evaluate capacity conditions for an attraction.

    Parameters:
        current_riders: Current rider count.
        max_capacity: Maximum allowed riders
            (Sky Loop: 24 riders).

    Returns:
        "full", "near capacity", or "available",
        or None if an input is missing or invalid.

    Capacity rules (utilization = current_riders / max_capacity):
        - max_capacity is None, 0, or negative -> None
          (check this first: dividing by 0 crashes)
        - current_riders is None, negative, or more
          than max_capacity -> None
        - current_riders == max_capacity -> "full"
        - utilization of 80% or more -> "near capacity"
          (Sky Loop at 20 of 24 riders = 83%)
        - otherwise -> "available"
    """
    if max_capacity is None or max_capacity <= 0:
        return None
    if current_riders is None or current_riders < 0:
        return None
    if current_riders > max_capacity:
        return None

    if current_riders == max_capacity:
        return "full"
    if calculate_utilization(current_riders, max_capacity) >= 0.8:
        return "near capacity"
    return "available"


# ---------------------------------------------------
# FEATURE 4: FUNCTION INTEGRATION
# ---------------------------------------------------

# Done: call each Week 2 function once for Sky Loop and
# show the results under the Week 1 message.
capacity_status = check_capacity(current_riders, max_capacity)
adult_price = calculate_ticket_price("adult", adult_base_price)
eligible_at_min = check_ride_eligibility(48, sky_loop_min_height)

print(f"Capacity status: {capacity_status}")
print(f"Adult ticket: ${adult_price:.2f}")
print(f"Eligible at 48 inches: {eligible_at_min}")


# ---------------------------------------------------
# WEEK 2: EDGE-CASE NOTES
# ---------------------------------------------------

# Done: predictions checked against the actual behavior.
#
# 1. A required input is None -> every rule function returns None.
# 2. A numeric input is negative -> None
#    (check_ride_eligibility(-3, 48), check_capacity(-1, 24)).
# 3. A capacity value is zero -> check_capacity(5, 0) returns None
#    with no ZeroDivisionError, because the guard runs before dividing.
# 4. A visitor exactly at the boundary -> check_ride_eligibility(48, 48)
#    returns True (>= includes 48).
# 5. An unrecognized ticket category -> calculate_ticket_price("vip", 60.00)
#    returns None.


# ===================================================
# PARKPULSE — WEEK 3: LOOPS, STRINGS & INPUT
# ===================================================
#
# Weeks 1 and 2 are filled in above, so this week
# you only write Week 3 code. Reuse these names:
#   ride_name, max_capacity, current_riders, is_open,
#   sky_loop_min_height, adult_base_price
#   calculate_utilization(), check_ride_eligibility(),
#   calculate_ticket_price(), check_capacity()
#
# This week:
# - Clean and validate user input
# - Build a repeating menu
# - Simulate the Sky Loop queue
# - Display a readable attraction summary
#
# Reuse your Week 1 variables and Week 2 functions.
# The values below match the Business Rules table
# in the Week 3 README.


# ---------------------------------------------------
# FEATURE 5: INPUT VALIDATION
# ---------------------------------------------------

def get_menu_choice():
    """
    Ask the user to pick a menu option.

    Prompt (exactly): "Choose an option (1-5): "

    Returns:
        The choice as a string, "1" through "5",
        or None if the choice is invalid.

    Rules:
        - Remove surrounding spaces with .strip()
          (" 3 " counts as "3").
        - Valid choices are exactly "1", "2", "3",
          "4", or "5".
        - Anything else ("", "6", "3.0", "exit"):
          print "Please enter a number from 1 to 5."
          and return None.

    TODO:
        1. Read input with the prompt above.
        2. Remove surrounding whitespace.
        3. Check whether the choice is valid.
        4. Return the choice, or print the message
           and return None.
    """
    pass


def get_yes_no(prompt):
    """
    Ask a yes/no question and return the answer.

    Parameters:
        prompt: The question to show,
            for example "Exit ParkPulse? [Y/N]: "

    Returns:
        True for yes, False for no,
        None if the answer is not recognized.

    Rules (after .strip().lower()):
        - "y" or "yes" -> True
          (" Y ", "YES", and "yes" all count)
        - "n" or "no" -> False
        - anything else ("", "maybe", "yep"):
          print "Please answer Y or N."
          and return None

    TODO:
        1. Read input using the prompt parameter.
        2. Normalize it with .strip() and .lower().
        3. Return True, False, or None using the
           rules above.
    """
    pass


def get_numeric_input(prompt):
    """
    Ask for a whole number (0 or more), with up to 3 tries.

    Parameters:
        prompt: The question to show,
            for example "Visitor height in inches: "

    Returns:
        The number as an int, or None after
        3 invalid entries.

    Rules:
        - Remove surrounding spaces with .strip().
        - Valid: the cleaned text passes .isdigit()
          ("12", " 7 ", "0"). Convert with int()
          only after it passes.
        - Invalid ("", "-3", "3.5", "twelve"):
          print "Please enter a whole number (0 or more)."
          and ask again.
        - After 3 invalid entries in a row:
          print "Too many invalid entries."
          and return None.

    TODO:
        1. Use a loop that runs at most 3 times.
        2. Read and clean the input each time.
        3. Validate BEFORE converting.
        4. Return the int as soon as one entry is valid.
        5. After the loop, print the message and
           return None.

    Think:
        How do you know this loop always ends?
    """
    pass


# ---------------------------------------------------
# FEATURE 6: INTERACTIVE MENU
# ---------------------------------------------------

def run_menu():
    """
    Run the ParkPulse menu until the user exits.

    Each time through the loop, print an empty line
    and this menu (exactly), then call get_menu_choice():

        ParkPulse — Sky Loop
        1. Show attraction summary
        2. Check ride eligibility
        3. Price a ticket
        4. Simulate the queue
        5. Exit

    What each choice does:
        "1" -> call display_attraction_summary()
        "2" -> height = get_numeric_input(
                   "Visitor height in inches: ")
               If height is None, go back to the menu.
               Otherwise call check_ride_eligibility(height, 48):
                 True  -> "Eligible to ride Sky Loop."
                 False -> "Not tall enough: Sky Loop requires 48 inches."
                 None  -> "Height must be more than 0 inches."
        "3" -> ticket_type = input(
                   "Ticket type (adult/child/senior): ")
               cleaned with .strip().lower(), then
               calculate_ticket_price(ticket_type, 60.00):
                 a price -> f"{ticket_type} ticket: ${price:.2f}"
                            (for example "child ticket: $30.00")
                 None    -> "Unknown ticket type. Choose adult, child, or senior."
        "4" -> call simulate_queue()
        "5" -> get_yes_no("Exit ParkPulse? [Y/N]: "):
                 True        -> print "Goodbye!" and end the loop
                 False/None  -> go back to the menu
        None (invalid choice) -> go back to the menu
               (get_menu_choice() already printed the message)

    TODO:
        1. Choose the loop: it must repeat until
           the user confirms Exit.
        2. Print the menu and get the choice.
        3. Use continue for an invalid choice.
        4. Handle each choice with if/elif.
        5. Use break when the user confirms Exit.
    """
    pass


# ---------------------------------------------------
# FEATURE 7: QUEUE SIMULATION
# ---------------------------------------------------

def simulate_queue():
    """
    Simulate Sky Loop ride cycles until the line is empty.

    Queue rules:
        - Ask: get_numeric_input("Guests in line: ")
          If it returns None, return without simulating.
        - If 0 guests are waiting, print
          "No one is waiting." and return.
        - Each ride cycle boards up to the Sky Loop
          max capacity (24 riders: use your Week 1
          variable, not the number 24).
          If fewer are waiting, all of them board.
        - Each ride cycle takes 5 minutes.
        - After each cycle, get the status with
          check_capacity(boarding, <your max capacity variable>)
          and print (exactly):
          f"Cycle {cycle}: {boarding} board ({status}), {waiting} still waiting"
        - Stop when 0 guests are waiting, then print:
          f"Line cleared. Ride cycles: {cycles}. Total time: {minutes} minutes."

    Example (50 guests in line):
        Cycle 1: 24 board (full), 26 still waiting
        Cycle 2: 24 board (full), 2 still waiting
        Cycle 3: 2 board (available), 0 still waiting
        Line cleared. Ride cycles: 3. Total time: 15 minutes.

    TODO:
        1. Track the state: guests waiting, cycle count.
        2. Choose the loop and its stopping condition.
        3. Each cycle: work out how many board, update
           the guests waiting, and count the cycle.
        4. Reuse check_capacity() for the status.
        5. Print each cycle, then the final line.

    Think:
        Which value gets smaller on every pass?
        What prevents an infinite loop?
    """
    pass


# ---------------------------------------------------
# FEATURE 8: ATTRACTION SUMMARY
# ---------------------------------------------------

def display_attraction_summary():
    """
    Print a readable summary of Sky Loop.

    Use your Week 1 variables (name, max capacity,
    current riders, open) and your Week 2 functions.
    Do not hard-code the numbers in the output.

    Print exactly these lines for the Week 1 data:

        Sky Loop summary
          Open: yes
          Riders: 20 of 24
          Utilization: 83.33%
          Capacity: near capacity
          Tickets: adult $60.00, child $30.00, senior $45.00

    Formatting rules:
        - Open: "yes" if the attraction is open, else "no".
        - Utilization: current riders / max capacity,
          shown with :.2% (Week 1).
        - Capacity: the string check_capacity() returns.
        - Prices: from calculate_ticket_price(..., 60.00),
          shown with :.2f (two decimal places).

    TODO:
        1. Reuse the Week 1 variables.
        2. Call your Week 2 functions for the
           capacity status and prices.
        3. Format the numbers with f-strings.
        4. Print the lines above.
    """
    pass


# ---------------------------------------------------
# FEATURE 9: APPLICATION INTEGRATION
# ---------------------------------------------------

# TODO:
# Start the menu: call run_menu() once, as the
# last line of this file (below all the functions).
#
# Your Week 1 status message and any Week 2 test
# prints will still show first. Then the menu starts.
# Choosing 5 and answering Y ends the program.


# ---------------------------------------------------
# WEEK 3: TESTING AND DEBUGGING
# ---------------------------------------------------

# TODO:
# Run python3 src/parkpulse.py and test each case.
# Predict first, then compare with the README
# "Done when" sessions.
#
# 1. A valid menu choice: 1
# 2. An invalid menu choice: 9
# 3. An empty menu choice (just press Enter)
# 4. Exit with " y " (spaces and lowercase)
# 5. A negative height: -3
# 6. A decimal height: 47.5
# 7. A queue of 50 guests (3 cycles) and of 0 guests
# 8. Exit with N, then exit with Y
