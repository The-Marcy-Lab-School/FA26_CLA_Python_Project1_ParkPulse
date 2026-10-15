# ParkPulse — Week 2: Functions, Scope & Decisions

**Branch:** `Week_2` · **Project file:** `src/parkpulse.py` · **You need:** Week 1 finished on `main`

## Overview

ParkPulse helps amusement park staff check an attraction's capacity and status. Last week you displayed Sky Loop's utilization. This week you refactor that code into functions and add decisions: ride eligibility, ticket pricing, and capacity rules.

**This week you will:**
- Turn repeated code into functions with parameters, docstrings, and return values.
- Explain local versus global scope, and read `NameError`, `TypeError`, and `UnboundLocalError`.
- Write decisions with `if`/`elif`/`else`, guard clauses, and `is None`, and test their edge cases.

## 1. Get the Week 2 starter

**1.** In your `parkpulse` folder (with `.venv` active), start from your up-to-date `main` and create your branch. Run each command by itself:
```bash
git switch main
git pull --ff-only origin main
git switch -c Week_2
```
**2.** Only if `git remote -v` does not list `upstream`, add it:
```bash
git remote add upstream https://github.com/The-Marcy-Lab-School/FA26_CLA_Python_Project1_ParkPulse.git
```
**3.** Download the Week 2 starter:
```bash
git fetch upstream Week_2
```
**You should see:** a line ending in `Week_2 -> FETCH_HEAD` (or `upstream/Week_2`).

**4.** Copy this README and the practice files:
```bash
git restore --source upstream/Week_2 -- README.md practice/
```
**You should see:** no output, and `practice/` in the Explorer.

**5.** Add the new starter code (don't restore the whole file; it would erase your Week 1 code). Print the school's file, copy from the `# ===` line above `# PARKPULSE — WEEK 2` to the end, and paste it at the end of your `src/parkpulse.py`:
```bash
git --no-pager show upstream/Week_2:src/parkpulse.py
```
**6.** Check, commit, and push:
```bash
git status
```
**You should see:** `modified: README.md`, `modified: src/parkpulse.py`, and `practice/` untracked. No `.venv/`.
```bash
git add README.md practice/ src/parkpulse.py
git commit -m "Add Week 2 starter materials"
git push -u origin Week_2
```

## 2. Readings

Every reading opens with a real-world scenario in §1 — always start there.
- **Read:** [Functions](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/03-functions/) — §1 scenario, §2 vocabulary, §5 repeated code into a function, §6 `return`, §7 scope.
- **Skim:** [Conditional Statements](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/04-conditional-statements/) — §1 scenario, §2 vocabulary, glance at §5 guard clauses.

Everything else is optional. **Think about:** (1) What is the difference between `print()` and `return`? (2) Why might a variable be visible inside one function but not another? (3) Why check for `None` before comparing a value to a number?

## 3. Practice

Open each file in `practice/`, run it (`python3 practice/<file>.py`), then fill in every `None` and complete every `# TODO`. Predict before you run.
Files: `practice/01_functions.py` · `practice/02_scope.py` · `practice/03_decisions.py`

## 4. ParkPulse — Week 2 tasks

Complete the stubs below the Week 2 banner in `src/parkpulse.py`. **Business Rules** (each docstring repeats them):

| Function | Rule |
|---|---|
| `check_ride_eligibility(visitor_height, minimum_height)` | Sky Loop minimum height 48 inches. `True` if height ≥ minimum (exactly 48 is eligible), `False` if shorter, `None` if either value is `None`, 0, or negative. |
| `calculate_ticket_price(ticket_type, base_price)` | Base price $60.00: adult $60.00, child $30.00, senior $45.00. `None` for any other type or a base price that is `None`, 0, or negative. |
| `check_capacity(current_riders, max_capacity)` | Sky Loop max 24 riders. `"full"` at max; `"near capacity"` at 80% or more; otherwise `"available"`. `None` for a missing, 0, or negative max, or riders that are `None`, negative, or over max. |

**Task A — Refactor into a function.** Move your Week 1 utilization calculation into a function (above the Week 2 banner) that takes riders and capacity as parameters, has a docstring, and **returns** the value.
- **Done when:** your Week 1 message still prints `83.33%`, using the function's return value.

**Task B — Ride eligibility.** Complete `check_ride_eligibility()`: guard clauses for invalid values first, then the height rule.
- **Done when:** `print(check_ride_eligibility(48, 48))` prints `True` and a `None` height returns `None`.

**Task C — Ticket pricing.** Complete `calculate_ticket_price()` with a guard clause and `if`/`elif`/`else`. Return the price; don't print it.
- **Done when:** each ticket type returns its price from the table, and `"vip"` returns `None`.

**Task D — Capacity rules.** Complete `check_capacity()`, reusing your Task A function. Guard against a zero or missing max **before** you divide.
- **Done when:** `check_capacity(20, 24)` returns `"near capacity"` and `check_capacity(5, 0)` returns `None` without crashing.

**Task E — Integrate and test.** Under `FEATURE 4: FUNCTION INTEGRATION`, call your functions for Sky Loop and print the results with your Week 1 message. Then predict and test the edge cases at the bottom of the file.
- **Done when:** `python3 src/parkpulse.py` runs with no error and every edge case matches the Business Rules. (No menus or loops yet.)

## 5. AI activity

Copy this prompt, then **predict** each result from the Business Rules, **run** it inside `print()`, and **decide** whether the test was worth keeping:
```text
Suggest five unusual or boundary-case inputs that could test a Python ride eligibility function. Do not write the function or provide implementation code.
```

## 6. Interview prep

**Question:** "Why did you refactor that ParkPulse logic into a function?" Answer in 60–90 seconds:
- **Point:** what you extracted. **Reason:** reuse, testing one rule at a time, clearer names.
- **Evidence:** one function, one input, one result, e.g. `check_capacity(5, 0)` returning `None` instead of crashing.
- **Point:** restate what you extracted and how that structure improves correctness (PREP).

## 7. Checklist

- [ ] I started `Week_2` from `main` and kept my Week 1 code.
- [ ] I did the readings and every practice file.
- [ ] Task A: utilization is a function that returns a value.
- [ ] Tasks B–D: all three functions match the Business Rules, including edge cases.
- [ ] Task E: the program runs with no error and my Week 1 message still prints.
- [ ] My work is pushed to `Week_2` and `src/parkpulse.py` is integrated into `main`.

## 8. Commit, push, and integrate into main

Push your work, then (after your instructor signs off) bring **only** `src/parkpulse.py` into `main`. Never move `README.md` or `practice/` to `main`.
```bash
git add README.md practice/ src/parkpulse.py
git commit -m "Complete Week 2 ParkPulse functions"
git push origin Week_2
git switch main
git pull --ff-only origin main
git restore --source Week_2 -- src/parkpulse.py
git add src/parkpulse.py
git commit -m "Integrate Week 2 ParkPulse features"
git push origin main
```
