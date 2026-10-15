# ParkPulse — Week 3: Loops, Strings & Interactive Input

**Branch:** `Week_3` · **Project file:** `src/parkpulse.py` · **You need:** Week 2 finished on `main`

## Overview

ParkPulse helps amusement park staff check an attraction's capacity and status. In Weeks 1–2 you calculated utilization and wrote functions for eligibility, pricing, and capacity. This week you make ParkPulse interactive: a repeating menu, a queue simulation, validated input, and an attraction summary.

**This week you will:**
- Choose a `for` or `while` loop, and predict how many times it runs with `range()`, `break`, and `continue`.
- Clean, validate, and convert user input before you use it.
- Explain `:.2f` versus `round()`, and prove your loop ends.

## 1. Get the Week 3 starter

**1.** In your `parkpulse` folder (with `.venv` active), start from your up-to-date `main` and create your branch. Run each command by itself:
```bash
git switch main
git pull --ff-only origin main
git switch -c Week_3
```
**2.** Only if `git remote -v` does not list `upstream`, add it:
```bash
git remote add upstream https://github.com/The-Marcy-Lab-School/FA26_CLA_Python_Project1_ParkPulse.git
```
**3.** Download the Week 3 starter:
```bash
git fetch upstream Week_3
```
**You should see:** a line ending in `Week_3 -> FETCH_HEAD` (or `upstream/Week_3`).

**4.** Copy this README and the practice files:
```bash
git restore --source upstream/Week_3 -- README.md practice/
```
**You should see:** no output, and the Week 3 files in `practice/`.

**5.** Add the new starter code (don't restore the whole file; it would erase your Week 1–2 code). Print the school's file, copy from the `# ===` line above `# PARKPULSE — WEEK 3` to the end, and paste it at the end of your `src/parkpulse.py`:
```bash
git --no-pager show upstream/Week_3:src/parkpulse.py
```
**6.** Check, commit, and push:
```bash
git status
```
**You should see:** `modified: README.md`, `modified: src/parkpulse.py`, and `practice/` changes. No `.venv/`.
```bash
git add README.md practice/ src/parkpulse.py
git commit -m "Add Week 3 starter materials"
git push -u origin Week_3
```

## 2. Readings

Every reading opens with a real-world scenario in §1 — always start there.
- **Read:** [Loops](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/05-loops/) — §1 scenario, §2 vocabulary, §4 known vs unknown count, §5 `break`/`continue`, §6 running count.
- **Skim:** [Inputs and Outputs](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/06-inputs-and-outputs/) — §1 scenario, §2 vocabulary, glance at §6 turning input into the right type.

Everything else is optional. **Think about:** (1) When should a program use a `for` loop instead of a `while` loop? (2) What stops a loop, and what makes one run forever? (3) Why does user input need validation before conversion?

## 3. Practice

Open each file in `practice/`, run it (`python3 practice/<file>.py`), then fill in every `None` and complete every `# TODO`. Predict before you run. (`06_input_trace.py` asks for input; pressing Enter is fine.)
Files: `practice/01_loop_trace.py` · `practice/02_flow_trace.py` · `practice/03_nested_trace.py` · `practice/04_termination.py` · `practice/05_string_trace.py` · `practice/06_input_trace.py` · `practice/07_format_trace.py`

## 4. ParkPulse — Week 3 tasks

Complete the stubs below the Week 3 banner in `src/parkpulse.py`. **Business Rules** (each docstring repeats them and gives the exact messages to print; Week 2 rules still apply: 48 inches, $60/$30/$45, `"full"` at 24 of 24):

| Function | Rule |
|---|---|
| `run_menu()` | Options 1–5: summary, eligibility, ticket price, queue, exit. Repeats until Exit is confirmed with Y. |
| `get_menu_choice()` | After `.strip()`, only `"1"` to `"5"` are valid; anything else prints a message and returns `None`. |
| `get_yes_no(prompt)` | After `.strip().lower()`: `y`/`yes` → `True`, `n`/`no` → `False`, anything else → `None`. |
| `get_numeric_input(prompt)` | Whole numbers 0 or more (`.isdigit()`). Asks again on invalid input; after 3 invalid tries returns `None`. |
| `simulate_queue()` | Each 5-minute cycle boards up to 24 guests (fewer if fewer wait). Repeat until 0 are waiting. |
| `display_attraction_summary()` | Utilization with `:.2%`, prices with `:.2f`, status from `check_capacity()`. |

**Task A — Clean and validate input.** Complete `get_menu_choice()`, `get_yes_no()`, and `get_numeric_input()` (FEATURE 5).
- **Done when:** temporary `print(...)` calls handle valid, messy (spaces, capitals), and invalid input as the rules say, with no crash.

**Task B — Interactive menu.** Complete `run_menu()` (FEATURE 6), reusing `check_ride_eligibility()` and `calculate_ticket_price()`. Add `run_menu()` as the last line of the file (FEATURE 9).
- **Done when:** every choice works, an invalid choice shows the menu again, and Exit only ends on Y.

**Task C — Queue simulation.** Complete `simulate_queue()` (FEATURE 7) with a loop that stops when no one is waiting, reusing `check_capacity()` for each cycle.
- **Done when:** menu choice 4 with 50 guests prints:
```text
Cycle 1: 24 board (full), 26 still waiting
Cycle 2: 24 board (full), 2 still waiting
Cycle 3: 2 board (available), 0 still waiting
Line cleared. Ride cycles: 3. Total time: 15 minutes.
```
**Task D — Attraction summary.** Complete `display_attraction_summary()` (FEATURE 8) from your Week 1 variables and Week 2 functions; don't type the numbers by hand.
- **Done when:** menu choice 1 prints the six lines shown in the docstring.

**Task E — Test.** Run the 8 cases in the `WEEK 3: TESTING AND DEBUGGING` comment, predicting each first.
- **Done when:** no input (empty, spaces, letters, negatives, decimals) crashes the program, and your Week 1–2 output is unchanged.

## 5. AI activity

Copy this prompt, then for each suggestion **predict** what your program will do, **run** it, and **decide** whether the AI was right (if your program broke, fix it and note which assumption failed):
```text
I'm testing a Python command-line menu. It accepts a menu choice from 1 to 5, a Y/N answer, and a whole number of guests (0 or more). Suggest 8 unusual or hostile things a user might type that could break input validation or make a loop run forever. For each one, say what you think could go wrong. Do not write any code.
```

## 6. Interview prep

**Question:** "How do you know your loop will terminate?" Answer in 60–90 seconds:
- **Point:** which loop you used in `simulate_queue()` or `run_menu()`, and why. **Reason:** what changes each pass and which condition (or `break`) ends it.
- **Evidence:** your 50-guest run went 50 → 26 → 2 → 0 in 3 cycles.
- **Point:** restate why it ends, then what would make it infinite (boarding 0 per cycle) and how your code prevents it.

## 7. Checklist

- [ ] I started `Week_3` from `main` and kept my Week 1–2 code.
- [ ] I did the readings and all 7 practice files.
- [ ] Tasks A–D: input is validated, the menu repeats until Exit + Y, and the queue run and summary match.
- [ ] Task E: no input crashes the program, and I tested the AI's hostile inputs.
- [ ] My work is pushed to `Week_3` and `src/parkpulse.py` is integrated into `main`.

## 8. Commit, push, and integrate into main

Push your work, then (after your instructor signs off) bring **only** `src/parkpulse.py` into `main`. Never move `README.md` or `practice/` to `main`.
```bash
git add README.md practice/ src/parkpulse.py
git commit -m "Complete Week 3 interactive ParkPulse"
git push origin Week_3
git switch main
git pull --ff-only origin main
git restore --source Week_3 -- src/parkpulse.py
git add src/parkpulse.py
git commit -m "Integrate Week 3 ParkPulse application"
git push origin main
```
