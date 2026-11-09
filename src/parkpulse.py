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

minutes_per_cycle = 5


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
    """
    choice = input("Choose an option (1-5): ").strip()

    # One character long AND one of the digits 1-5.
    # The length check stops "12" or "" from matching.
    if len(choice) == 1 and choice in "12345":
        return choice

    print("Please enter a number from 1 to 5.")
    return None


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
    """
    answer = input(prompt).strip().lower()

    if answer == "y" or answer == "yes":
        return True
    if answer == "n" or answer == "no":
        return False

    print("Please answer Y or N.")
    return None


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

    Why this loop always ends:
        range(3) gives it at most 3 passes, and a valid
        entry returns early.
    """
    for attempt in range(3):
        entry = input(prompt).strip()
        if entry.isdigit():
            return int(entry)
        print("Please enter a whole number (0 or more).")

    print("Too many invalid entries.")
    return None


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
    """
    # while True: we can't know in advance how many times the user
    # will pick an option. The loop ends only at the break (Exit + Y).
    while True:
        print()
        print("ParkPulse — Sky Loop")
        print("1. Show attraction summary")
        print("2. Check ride eligibility")
        print("3. Price a ticket")
        print("4. Simulate the queue")
        print("5. Exit")

        choice = get_menu_choice()
        if choice is None:
            continue

        if choice == "1":
            display_attraction_summary()
        elif choice == "2":
            height = get_numeric_input("Visitor height in inches: ")
            if height is None:
                continue
            eligible = check_ride_eligibility(height, sky_loop_min_height)
            if eligible is None:
                print("Height must be more than 0 inches.")
            elif eligible:
                print("Eligible to ride Sky Loop.")
            else:
                print("Not tall enough: Sky Loop requires 48 inches.")
        elif choice == "3":
            ticket_type = input("Ticket type (adult/child/senior): ")
            ticket_type = ticket_type.strip().lower()
            price = calculate_ticket_price(ticket_type, adult_base_price)
            if price is None:
                print("Unknown ticket type. Choose adult, child, or senior.")
            else:
                print(f"{ticket_type} ticket: ${price:.2f}")
        elif choice == "4":
            simulate_queue()
        elif choice == "5":
            if get_yes_no("Exit ParkPulse? [Y/N]: "):
                print("Goodbye!")
                break


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

    Why this loop always ends:
        waiting gets smaller on every pass, because at least
        1 guest boards (waiting > 0 and max_capacity is 24).
    """
    waiting = get_numeric_input("Guests in line: ")
    if waiting is None:
        return
    if waiting == 0:
        print("No one is waiting.")
        return

    cycles = 0
    while waiting > 0:
        if waiting >= max_capacity:
            boarding = max_capacity
        else:
            boarding = waiting
        waiting = waiting - boarding
        cycles = cycles + 1

        status = check_capacity(boarding, max_capacity)
        print(
            f"Cycle {cycles}: {boarding} board ({status}), "
            f"{waiting} still waiting"
        )

    minutes = cycles * minutes_per_cycle
    print(
        f"Line cleared. Ride cycles: {cycles}. "
        f"Total time: {minutes} minutes."
    )


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
    """
    if is_open:
        open_text = "yes"
    else:
        open_text = "no"

    utilization = calculate_utilization(current_riders, max_capacity)
    status = check_capacity(current_riders, max_capacity)
    adult = calculate_ticket_price("adult", adult_base_price)
    child = calculate_ticket_price("child", adult_base_price)
    senior = calculate_ticket_price("senior", adult_base_price)

    print(f"{ride_name} summary")
    print(f"  Open: {open_text}")
    print(f"  Riders: {current_riders} of {max_capacity}")
    print(f"  Utilization: {utilization:.2%}")
    print(f"  Capacity: {status}")
    print(
        f"  Tickets: adult ${adult:.2f}, child ${child:.2f}, "
        f"senior ${senior:.2f}"
    )


# ---------------------------------------------------
# WEEK 3: TESTING AND DEBUGGING
# ---------------------------------------------------

# Done: each case tested with python3 src/parkpulse.py.
#
# 1. 1        -> the six-line Sky Loop summary.
# 2. 9        -> "Please enter a number from 1 to 5.", menu again.
# 3. Enter    -> same message, menu again.
# 4. 5 then " y " -> "Goodbye!" (strip + lower make it "y").
# 5. 2 then -3     -> "Please enter a whole number (0 or more)."
#    ("-" is not a digit), asks again.
# 6. 2 then 47.5   -> same message ("." is not a digit), asks again.
# 7. 4 then 50 -> 3 cycles, 15 minutes. 4 then 0 -> "No one is waiting."
# 8. 5 then N -> menu again; 5 then Y -> "Goodbye!"


# ===================================================
# PARKPULSE — WEEK 4: LISTS, REFERENCES & DELIVERY
# ===================================================
#
# Weeks 1–3 are filled in above, so this week you
# only write Week 4 code. Reuse these names:
#   check_capacity(), get_menu_choice(), run_menu(),
#   simulate_queue(), display_attraction_summary()
#
# This week:
# - Store the whole park as a list of tuples
# - List, find, and filter attractions
# - Write queue helpers that never change the
#   caller's list (pure: copy first)
# - Add menu option 5: List attractions
#
# run_menu() is called once, as the LAST line of the
# file (below this section), so every function is
# defined before the menu calls it.
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


# ---------------------------------------------------
# START THE APP (keep this as the last line)
# ---------------------------------------------------

run_menu()
