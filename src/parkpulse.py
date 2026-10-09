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
