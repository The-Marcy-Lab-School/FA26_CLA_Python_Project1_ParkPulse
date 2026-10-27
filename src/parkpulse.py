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

# TODO 1:
# Store the attraction data above in clearly named variables.
#
# Think about:
# - Which Python data type fits each value?
# - Which names follow snake_case?
# - Which value should be represented as a boolean?


# TODO 2:
# Calculate the attraction's utilization.
#
# Utilization means:
# current riders divided by maximum capacity
#
# Before running your code, predict the type and value
# of the expression you write.


# TODO 3:
# Use print() and an f-string to display a readable status message.
#
# Your message should include:
# - the attraction name
# - its utilization as a percentage
# - whether the attraction is open


# TODO 4:
# Review your code before you finish.
#
# Check:
# - snake_case variable names
# - spaces around operators
# - four-space indentation if you use indentation
# - no unnecessary semicolons or braces


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
# TODO: Integrate new functions into your
# existing ParkPulse application.
#
# The rule values below match the Business Rules
# table in the Week 2 README.


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

    TODO:
        1. Handle missing inputs.
        2. Identify invalid values.
        3. Apply the eligibility rule above.
        4. Return the result.
    """
    pass


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

    TODO:
        1. Validate the provided inputs.
        2. Identify the required pricing categories.
        3. Apply the pricing rules above.
        4. Return the calculated result.

    Consider:
        Would a guard clause help?
        Would if/elif/else clarify the logic?
    """
    pass


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

    TODO:
        1. Review the Week 1 capacity calculations.
        2. Decide which existing work can be reused.
        3. Protect against invalid values.
        4. Apply the capacity rules above.
        5. Return the result.

    Important:
        Preserve your working Week 1 behavior.
    """
    pass


# ---------------------------------------------------
# FEATURE 4: FUNCTION INTEGRATION
# ---------------------------------------------------

# TODO:
# Identify where the existing ParkPulse application
# should call each new function.
#
# Consider:
# - What arguments should be passed?
# - Where should returned values be stored?
# - Which code displays results?
# - Which functions can be reused?
#
# Do not duplicate your Week 1 entry point.
# Do not add Week 3 interactive menus or loops.


# ---------------------------------------------------
# WEEK 2: EDGE-CASE NOTES
# ---------------------------------------------------

# TODO:
# Predict what should happen when:
#
# 1. A required input is None.
# 2. A numeric input is negative.
# 3. A capacity value is zero.
# 4. A visitor is exactly at an eligibility boundary.
# 5. An unrecognized ticket category is supplied.
#
# Compare predictions with actual behavior.


# ===================================================
# PARKPULSE — WEEK 3: LOOPS, STRINGS & INPUT
# ===================================================
#
# Keep all Week 1 and Week 2 code above.
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


# ===================================================
# PARKPULSE — WEEK 4: LISTS, REFERENCES & DELIVERY
# ===================================================
#
# Keep all Week 1–3 code above.
#
# This week:
# - Store the whole park as a list of tuples
# - List, find, and filter attractions
# - Write queue helpers that never change the
#   caller's list (pure: copy first)
# - Add menu option 5: List attractions
#
# Move your run_menu() call below this section so it
# is still the LAST line of the file. A function must
# be defined before the menu calls it.
#
# The values below match the Business Rules table
# in the Week 4 README. No dictionaries yet (Week 5).


# ---------------------------------------------------
# FEATURE 10: PARK DATA
# ---------------------------------------------------

# TODO:
# Replace the empty list with one tuple per attraction,
# in this order: (name, max_capacity, current_riders, is_open)
#
#   Sky Loop       24 max, 20 riders, open
#   River Rapids   16 max, 16 riders, open
#   Pirate Drop    12 max,  3 riders, closed
#   Comet Coaster  30 max, 12 riders, open
#
# Sky Loop's values match your Week 1 variables.

ATTRACTIONS = []


# ---------------------------------------------------
# FEATURE 11: LIST, FIND, AND FILTER
# ---------------------------------------------------

def list_attractions(attractions):
    """
    Print one numbered line per attraction.

    Parameters:
        attractions: A list of
            (name, max_capacity, current_riders, is_open) tuples.

    Returns:
        Nothing. It only prints.

    Rules:
        - Number from 1 with enumerate(attractions, start=1).
        - Open attraction (status from check_capacity()):
          f"{number}. {name}: {riders}/{max_capacity} riders ({status})"
        - Closed attraction (no rider count):
          f"{number}. {name}: closed"

    Expected output for ATTRACTIONS:
        1. Sky Loop: 20/24 riders (near capacity)
        2. River Rapids: 16/16 riders (full)
        3. Pirate Drop: closed
        4. Comet Coaster: 12/30 riders (available)

    TODO:
        1. Loop with enumerate(attractions, start=1).
        2. Unpack each tuple into four names.
        3. Print the closed line or the open line.
    """
    pass


def find_attraction(attractions, name):
    """
    Find one attraction by name.

    Parameters:
        attractions: The list of attraction tuples.
        name: The name to look for. Ignore case and
            surrounding spaces: "  river rapids " finds
            "River Rapids".

    Returns:
        The matching tuple, or None if no name matches.

    TODO:
        1. Clean the name with .strip().lower().
        2. Loop over the attractions and compare each
           lowercased name.
        3. Return the tuple as soon as one matches.
        4. After the loop, return None.
    """
    pass


def open_attraction_names(attractions):
    """
    List the names of the attractions that are open.

    Parameters:
        attractions: The list of attraction tuples.

    Returns:
        A NEW list of names, in the original order.
        For ATTRACTIONS:
        ['Sky Loop', 'River Rapids', 'Comet Coaster']

    TODO:
        1. Start an empty list.
        2. Loop and unpack each tuple.
        3. Append the name when is_open is True.
        4. Return the new list.
    """
    pass


# ---------------------------------------------------
# FEATURE 12: PURE QUEUE HELPERS
# ---------------------------------------------------

def join_queue(queue, guest):
    """
    Add a guest to the end of a line, without changing it.

    Parameters:
        queue: A list of guest names.
        guest: The name to add.

    Returns:
        A NEW list with guest at the end.
        The caller's queue stays the same:
            line = ["Ana", "Ben"]
            new_line = join_queue(line, "Cy")
            line     -> ['Ana', 'Ben']
            new_line -> ['Ana', 'Ben', 'Cy']

    TODO:
        1. Copy the queue first.
        2. Append the guest to the copy.
        3. Return the copy.
    """
    pass


def board_riders(queue, seats):
    """
    Split a line into who boards and who keeps waiting.

    Parameters:
        queue: A list of guest names, first in line first.
        seats: How many guests can board.

    Returns:
        A tuple (boarding, still_waiting), both NEW lists.
        The caller's queue stays the same:
            board_riders(["Ana", "Ben", "Cy", "Dee", "Eli"], 3)
            -> (['Ana', 'Ben', 'Cy'], ['Dee', 'Eli'])

    TODO:
        1. Slice the first `seats` guests.
        2. Slice everyone after them.
        3. Return both slices as a tuple.
    """
    pass


# ---------------------------------------------------
# FEATURE 13: MENU OPTION 5
# ---------------------------------------------------

# TODO:
# Update your Week 3 menu functions (above):
#
# 1. get_menu_choice(): the prompt becomes
#    "Choose an option (1-6): ", valid choices are "1"
#    to "6", and the message becomes
#    "Please enter a number from 1 to 6."
# 2. run_menu(): the menu shows
#        5. List attractions
#        6. Exit
#    Choice "5" calls list_attractions(ATTRACTIONS).
#    Choice "6" does what "5" did in Week 3 (Exit + Y).


# ---------------------------------------------------
# WEEK 4: TESTING AND SHIPPING
# ---------------------------------------------------

# TODO:
# Run python3 src/parkpulse.py and test each case.
# Predict first.
#
# 1. Menu choice 5 (all four attractions print)
# 2. Menu choice 6, then Y
# 3. Menu choice 7 (invalid)
# 4. A temporary print of find_attraction(ATTRACTIONS, "  sky loop ")
# 5. A temporary print of join_queue() and board_riders(),
#    then print the original list: it must not change
#
# Before you integrate into main, follow "Ship it" in
# the README: delete every TODO and banner comment,
# keep real docstrings, and replace pass with code.
