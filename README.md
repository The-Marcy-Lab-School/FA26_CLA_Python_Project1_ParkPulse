# ParkPulse — Week 2: Functions, Scope & Decisions

**Project:** ParkPulse  
**Branch:** `Week_2`

## Overview

Last week, you built the foundation of ParkPulse using variables, data types, expressions, and operators to calculate ride capacity/utilization and display formatted attraction status.

Your completed Week 1 Python application should already be integrated into your personal repository's `main` branch.

**This week, you will refactor and extend ParkPulse using functions and conditional logic.**

### Week 2 Goals

By the end of this week, you will:

- Create reusable functions with parameters, arguments, docstrings, and return values.
- Trace function calls and explain local versus global scope.
- Use `if`, `elif`, `else`, and guard clauses to make decisions.
- Apply eligibility, ticket pricing, and capacity rules to ParkPulse.
- Predict and test edge cases.

---

## 1. Get Your Week 2 Starter From GitHub

Your instructor has published the Week 2 starter code and practice activities on the school repository's `Week_2` branch.

You will fetch the starter into your **existing personal ParkPulse repository**.

### Step 1 — Open Your Existing Repository

In VS Code, open your ParkPulse project and terminal.

Check your current branch and remotes:

```bash
git status
git remote -v
```

Your `origin` should point to your personal GitHub repository.

### Step 2 — Add the School Repository as a Remote

If you have not already added the school repository:

```bash
git remote add upstream https://github.com/The-Marcy-Lab-School/FA26_CLA_Python_Project1_ParkPulse.git
```

If `upstream` already exists, skip this command.

### Step 3 — Fetch the Week 2 Branch

```bash
git fetch upstream Week_2
```

This downloads your instructor's Week 2 starter without modifying your `main` branch.

### Step 4 — Create Your Week 2 Branch

First, make sure your Week 1 work is committed and your working tree is clean.

```bash
git switch main
git pull --ff-only origin main
git switch -c Week_2
```

Your new branch now starts with your completed Week 1 application.

### Step 5 — Add the Week 2 Starter Materials

Retrieve your instructor's Week 2 README and practice files:

```bash
git restore --source upstream/Week_2 -- README.md practice/
```

Your instructor has also added new Week 2 function starter code to `src/parkpulse.py`.

**Important:** Do not restore the instructor's whole Python file. It would overwrite your completed Week 1 code.

Instead, print the instructor's version in your terminal:

```bash
git --no-pager show upstream/Week_2:src/parkpulse.py
```

1. Find the `PARKPULSE — WEEK 2: FUNCTIONS, SCOPE & DECISIONS` banner.
2. Copy everything from that banner to the end of the output.
3. Paste it at the bottom of your own `src/parkpulse.py`, below your Week 1 code.
4. Run `python3 src/parkpulse.py` and confirm your Week 1 status message still prints.

You now have your Week 1 work plus the Week 2 starter.

### Step 6 — Commit Your Starter

```bash
git add README.md practice/ src/parkpulse.py
git commit -m "Add Week 2 starter materials"
git push -u origin Week_2
```

You are ready to begin Week 2 development.

**Continue using your existing `.gitignore`. Do not commit `.venv/`.**

---

## 2. Interactive Reading — Functions

**Required:** Instructor-assigned sections of the Functions interactive GitBook reading.

Focus on:

- Defining and calling functions with `def`
- Parameters and arguments
- Return values
- Local versus global scope

### Think About

1. How does a function help eliminate repeated code?
2. What is the difference between `print()` and `return`?
3. What happens when a function is called with the wrong number of arguments?
4. Why might a variable be accessible inside one function but not another?

Be prepared to discuss one example during our whole-class debrief.

**Optional reading:** Conditional Statements.

---

## 3. Python Practice Activities

The `practice/` folder contains short exercises separate from the ParkPulse application. Each file holds the code examples from this week's slides.

| File | Skills | Slides |
|---|---|---|
| `01_functions.py` | Functions, parameters, defaults, keyword arguments, returns, print vs. return | 10, 13, 14 |
| `02_scope.py` | Nested calls, local vs. global scope, `NameError`, `TypeError`, `UnboundLocalError` | 12, 16–19 |
| `03_decisions.py` | `if`/`elif`/`else`, truthiness, `is None`, guard clauses, conditional expressions | 23–26 |

For each file:

1. Predict every printed line before running it, and write your predictions down.
2. Run the file and compare.
3. Answer the lettered prompts at the bottom of the file. Some prompts ask you to uncomment a line that raises an error: run it, read the last line of the error, then comment it back out.

```bash
python3 practice/01_functions.py
python3 practice/02_scope.py
python3 practice/03_decisions.py
```

**Remember:** These practice files are for learning. They are not part of the finished ParkPulse application.

---

## 4. ParkPulse — Week 2 Development

**File:** `src/parkpulse.py`

Your instructor has provided Week 2 starter function definitions and TODOs. Complete them using the Business Rules below. The same values are repeated in each function's docstring.

### Business Rules

| Rule | Function | Inputs | Result |
|---|---|---|---|
| Ride eligibility | `check_ride_eligibility(visitor_height, minimum_height)` | Heights in inches. Sky Loop minimum height: 48 inches. | `True` if `visitor_height >= minimum_height` (exactly 48 is eligible); `False` if shorter; `None` if either value is `None`, 0, or negative |
| Ticket pricing | `calculate_ticket_price(ticket_type, base_price)` | `ticket_type` is `"adult"`, `"child"`, or `"senior"` (lowercase). Base price: $60.00 | adult = 100% ($60.00); child = 50% ($30.00); senior = 75% ($45.00); `None` for any other ticket type or a base price that is `None`, 0, or negative |
| Capacity rules | `check_capacity(current_riders, max_capacity)` | Sky Loop max capacity: 24 riders. Utilization = `current_riders / max_capacity` | `"full"` if `current_riders == max_capacity`; `"near capacity"` if utilization is 80% or more (20 of 24 = 83%); otherwise `"available"`; `None` if `max_capacity` is `None`, 0, or negative, or `current_riders` is `None`, negative, or more than `max_capacity` |

### Task A — Refactor Into Functions

Move your Week 1 utilization calculation into a function, for example `calculate_utilization(current_riders, max_capacity)`, that **returns** the utilization instead of printing it.

Your functions should:

- Have descriptive names.
- Accept appropriate parameters.
- Include docstrings. Write real ones: they become the "How it's built" section of your portfolio README in Week 4.
- Return values that other code can use.
- Avoid unnecessary reliance on global variables.

**Done when:** `python3 src/parkpulse.py` prints the same Week 1 status message as before.

### Task B — Ride Eligibility

Complete `check_ride_eligibility()` using the eligibility rule in the table.

- Handle missing (`None`) and invalid values first, with guard clauses.
- Then apply the height rule and return the result.

Consider which conditions should be checked first. What happens if you compare `None` to a number?

### Task C — Ticket Pricing

Complete `calculate_ticket_price()` using the pricing rules in the table.

- Validate `base_price` with a guard clause.
- Use `if`/`elif`/`else` for the ticket categories.
- Return the price; do not print inside the function.

Consider why returning a value is more flexible than printing it inside the function.

### Task D — Capacity Rules

Complete `check_capacity()` using the capacity rules in the table.

- Reuse your Task A utilization function.
- Guard against a zero or missing `max_capacity` **before** dividing.
- Return one of the status strings.
- Preserve correct Week 1 behavior.

### Task E — Integrate and Test

Call your functions from the existing ParkPulse application, store their return values, and print the results with your Week 1 status message.

Then test each function: add these calls inside `print()` at the bottom of `src/parkpulse.py`, predict each result, and run the file. Your results must match:

| Call | Expected |
|---|---|
| `check_ride_eligibility(48, 48)` | `True` (boundary) |
| `check_ride_eligibility(40, 48)` | `False` |
| `check_ride_eligibility(None, 48)` | `None` |
| `calculate_ticket_price("child", 60.00)` | `30.0` |
| `calculate_ticket_price("vip", 60.00)` | `None` |
| `calculate_ticket_price("adult", -5)` | `None` |
| `check_capacity(20, 24)` | `"near capacity"` |
| `check_capacity(24, 24)` | `"full"` |
| `check_capacity(5, 0)` | `None` (no crash) |

The edge-case notes at the bottom of the starter code list more cases to predict.

Do not add interactive menus or loop-based features yet. Those are part of Week 3.

---

## 5. AI Edge-Case Activity

Use AI to suggest additional inputs that might reveal problems in your code.

Example prompt:

"Suggest five unusual or boundary-case inputs that could test a Python ride eligibility function. Do not write the function or provide implementation code."

For each input:

1. Predict the expected behavior.
2. Run your function.
3. Compare your prediction with the actual behavior.
4. Explain unexpected results.
5. Decide whether the AI suggestion was useful.

**AI can suggest test cases, but you are responsible for the expected behavior and implementation.**

---

## 6. Interview Connection

Imagine an interviewer asks:

**"Why did you refactor that ParkPulse logic into a function?"**

Prepare a 60–90-second explanation using:

- **Point:** What did you change?
- **Reason:** Why does that structure help?
- **Evidence:** Which function, input, and observed result support your decision?
- **Final Point:** What is the takeaway?

Be prepared to explain how you verified an edge case.

---

## 7. Week 2 Completion Checklist

- [ ] My completed Week 1 application is already on `main`.
- [ ] I fetched the instructor's `Week_2` starter.
- [ ] I preserved my Week 1 application code.
- [ ] I completed the required Functions reading activity.
- [ ] I practiced function calls, scope, and conditional statements.
- [ ] I refactored ParkPulse into reusable functions.
- [ ] I completed ride eligibility, ticket pricing, and capacity rules.
- [ ] I added appropriate guard clauses.
- [ ] Week 1 functionality still works.
- [ ] I tested normal and edge-case inputs, and every call in the Task E table matches its expected result.
- [ ] I can explain one design decision using evidence.

---

## 8. Commit and Push Week 2

Confirm your branch:

```bash
git branch --show-current
git status
```

Commit your completed work:

```bash
git add src/parkpulse.py practice/ README.md
git commit -m "Complete Week 2 ParkPulse functions"
git push origin Week_2
```

Your completed work is now saved on your personal repository's `Week_2` branch.

### Integrate Your Completed Application Into Main

**Do not merge the Week 2 README or `practice/` files into `main`.**

Those are instructional materials for `Week_2` only.

Once your Week 2 application is complete and approved, transfer only the finished Python application file:

```bash
git switch main
git pull --ff-only origin main
git restore --source Week_2 -- src/parkpulse.py
git add src/parkpulse.py
git commit -m "Integrate Week 2 ParkPulse features"
git push origin main
```

Your `main` branch should contain the cumulative working application, existing project documentation, and configuration files—not the weekly instructional README or practice exercises.

---

## Optional Practice

- Complete the Conditional Statements interactive reading.
- Trace additional functions involving default arguments, keyword arguments, and scope.
- Test additional edge cases.
- Complete any remaining Week 2 function work.

**Next week:** Loops, strings, and interactive input.