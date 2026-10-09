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


# ---------------------------------------------------
# FEATURE 1: RIDE ELIGIBILITY
# ---------------------------------------------------

def check_ride_eligibility(visitor_height, minimum_height):
    """
    Determine whether a visitor meets the assigned
    requirements for an attraction.

    Parameters:
        visitor_height: The visitor's height.
        minimum_height: The ride's minimum height.

    Returns:
        TODO: Decide on a meaningful result.

    TODO:
        1. Handle missing inputs.
        2. Identify invalid values.
        3. Apply the assigned eligibility rule.
        4. Return the result.
    """
    pass


# ---------------------------------------------------
# FEATURE 2: TICKET PRICING
# ---------------------------------------------------

def calculate_ticket_price(ticket_type, base_price):
    """
    Determine a ticket price using assigned rules.

    Parameters:
        ticket_type: The requested ticket category.
        base_price: The starting ticket price.

    Returns:
        TODO: Decide on the appropriate value.

    TODO:
        1. Validate the provided inputs.
        2. Identify the required pricing categories.
        3. Apply the assigned pricing rules.
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
        max_capacity: Maximum allowed riders.

    Returns:
        TODO: Choose a useful result for the caller.

    TODO:
        1. Review the Week 1 capacity calculations.
        2. Decide which existing work can be reused.
        3. Protect against invalid values.
        4. Apply the assigned capacity rules.
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
# Keep all Week 1 and Week 2 starter code above.
#
# This week:
# - Build a repeating menu
# - Simulate queue activity
# - Clean and validate user input
# - Display readable attraction summaries
#
# Reuse the functions from Week 2.


# ---------------------------------------------------
# FEATURE 5: INPUT VALIDATION
# ---------------------------------------------------

def get_menu_choice():
    """
    Ask the user to select a menu option.

    TODO:
        1. Read input from the user.
        2. Remove surrounding whitespace.
        3. Normalize text when appropriate.
        4. Check whether the choice is valid.
        5. Return the accepted choice.

    Think:
        What happens if the user enters
        spaces, an empty string, or an
        unexpected option?
    """
    pass


def get_numeric_input(prompt):
    """
    Request and validate numeric user input.

    TODO:
        1. Read the input as a string.
        2. Remove extra whitespace.
        3. Decide what counts as valid input.
        4. Convert only after validation.
        5. Decide how to handle invalid input.

    Think:
        What happens with negative numbers,
        decimals, or nonnumeric characters?
    """
    pass


# ---------------------------------------------------
# FEATURE 6: INTERACTIVE MENU
# ---------------------------------------------------

def run_menu():
    """
    Run the ParkPulse interactive menu.

    TODO:
        1. Decide which options to display.
        2. Allow the user to select an action.
        3. Repeat until the user chooses to exit.
        4. Handle unexpected menu choices.
        5. Call existing ParkPulse functions.

    Think:
        Should this use for or while?
        What condition ends the loop?
        Where should break or continue go?
    """
    pass


# ---------------------------------------------------
# FEATURE 7: QUEUE SIMULATION
# ---------------------------------------------------

def simulate_queue():
    """
    Simulate queue-related activity.

    TODO:
        1. Identify the state to track.
        2. Decide what changes each iteration.
        3. Choose an appropriate loop.
        4. Establish a stopping condition.
        5. Reuse existing capacity rules.
        6. Report the result.

    Think:
        What prevents an infinite loop?
        How does capacity affect the process?
        What evidence shows that the
        simulation stops correctly?
    """
    pass


# ---------------------------------------------------
# FEATURE 8: ATTRACTION SUMMARY
# ---------------------------------------------------

def display_attraction_summary():
    """
    Display readable attraction information.

    TODO:
        1. Reuse existing attraction data.
        2. Reuse Week 1 and Week 2 logic.
        3. Format numbers appropriately.
        4. Produce a readable summary.

    Think:
        Which values should be formatted?
        Where should calculations happen?
        Where should output happen?
    """
    pass


# ---------------------------------------------------
# FEATURE 9: APPLICATION INTEGRATION
# ---------------------------------------------------

# TODO:
# Connect the new features to the existing
# ParkPulse application.
#
# Consider:
# - Which function starts the interaction?
# - Where should the menu loop run?
# - When should the queue simulation run?
# - How do you avoid repeating Week 2 logic?
# - How does the user exit safely?
#
# Preserve existing Week 1 and Week 2 behavior.


# ---------------------------------------------------
# WEEK 3: TESTING AND DEBUGGING
# ---------------------------------------------------

# TODO:
# Test the following situations:
#
# 1. A valid menu selection.
# 2. An invalid menu selection.
# 3. An empty input.
# 4. A Y/N response with extra spaces.
# 5. A negative numeric input.
# 6. A decimal numeric input.
# 7. A queue that reaches its stopping condition.
# 8. A user who chooses to exit.
#
# Predict before running.
# Record the actual results.
