# ParkPulse — Week 3: Loops, Strings & Interactive Input

**Branch:** `Week_3` · **Project file:** `src/parkpulse.py` · **You need:** a `Week_3` branch (Weeks 1–2 come filled in)

## Overview

ParkPulse helps amusement park staff check an attraction's capacity and status. In Weeks 1–2 you calculated utilization and wrote functions for eligibility, pricing, and capacity. This week you make ParkPulse interactive: a repeating menu, a queue simulation, validated input, and an attraction summary.

**This week you will:**
- Choose a `for` or `while` loop, and predict how many times it runs with `range()`, `break`, and `continue`.
- Clean, validate, and convert user input before you use it.
- Explain `:.2f` versus `round()`, and prove your loop ends.

## 1. Get the Week 3 starter

The school's `src/parkpulse.py` has **Weeks 1–2 filled in**, so this week you only write Week 3 code.

**Already on `Week_3` from the end of the Week 2 deck?** Get the updated starter, then skip to Section 2. This replaces your `src/parkpulse.py` with the school's file (do it before you start Week 3):
```bash
git switch Week_3
git fetch upstream Week_3
git restore --source upstream/Week_3 -- README.md src/parkpulse.py
python3 src/parkpulse.py
git add README.md src/parkpulse.py
git commit -m "Week 3 starter with Weeks 1-2 filled in"
git push origin Week_3
```
**You should see:** the Week 1–2 status lines (`Utilization: 83.33%`, `Capacity status: near capacity`) when you run it.

**Starting fresh?** Follow steps 1–5.

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

**4.** Copy this README and the starter file (Weeks 1–2 filled in, Week 3 started for you):
```bash
git restore --source upstream/Week_3 -- README.md src/parkpulse.py
```
**You should see:** no output. `python3 src/parkpulse.py` prints the Week 1–2 status lines.

**5.** Check, commit, and push:
```bash
git status
```
**You should see:** `modified: README.md` and `modified: src/parkpulse.py`. No `.venv/`.
```bash
git add README.md src/parkpulse.py
git commit -m "Add Week 3 starter materials"
git push -u origin Week_3
```

## 2. Readings

Every reading opens with a real-world scenario in §1 — always start there.
- **Read:** [Loops](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/06-loops/) — §1 scenario, §2 vocabulary, §4 known vs unknown count, §5 `break`/`continue`, §6 running count.
- **Skim:** [Strings, Inputs and Outputs](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/05-strings-inputs-and-outputs/) — §1 scenario, §2 vocabulary, glance at §6 turning input into the right type.

Everything else is optional. **Think about:** (1) When should a program use a `for` loop instead of a `while` loop? (2) What stops a loop, and what makes one run forever? (3) Why does user input need validation before conversion?

## 3. In class: concept, your turn, answer

There are no practice files this week. Every concept in the deck has a **Your turn** slide (code with a `# TODO` comment) and an **Answer** slide. Then you build the tasks below in breakout rooms and teach the class what to type.
If you restored `practice/` last class, you can delete it: `git rm -r practice` (it never goes to `main`).

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

## 5. Use AI while you build

AI is a partner, not the author. **Ask AI to:** explain an error message in plain words, list unusual inputs to test, or check one of your functions against a README rule (point to the line, don't rewrite it). **You still:** write each line yourself, predict before you run every suggestion, and explain any line you keep.

Try it on Task E. Copy this prompt, then for each suggestion **predict** what your program will do, **run** it, and **decide** whether the AI was right (if your program broke, fix it and note which assumption failed):
```text
I'm testing a Python command-line menu. It accepts a menu choice from 1 to 5, a Y/N answer, and a whole number of guests (0 or more). Suggest 8 unusual or hostile things a user might type that could break input validation or make a loop run forever. For each one, say what you think could go wrong. Do not write any code.
```

## 6. Interview prep

**Question:** "How do you know your loop will terminate?" Answer in 60–90 seconds:
- **Point:** which loop you used in `simulate_queue()` or `run_menu()`, and why. **Reason:** what changes each pass and which condition (or `break`) ends it.
- **Evidence:** proof, not a claim (CLA Technical Communication, Week 3): your 50-guest run went 50 → 26 → 2 → 0 in 3 cycles.
- **Point:** restate why it ends, then what would make it infinite (boarding 0 per cycle) and how your code prevents it.

## 7. Checklist

- [ ] I'm on `Week_3` with the school's starter (Weeks 1–2 filled in).
- [ ] I did the readings and each Your turn slide in class.
- [ ] Tasks A–D: input is validated, the menu repeats until Exit + Y, and the queue run and summary match.
- [ ] Task E: no input crashes the program, and I tested the AI's hostile inputs.
- [ ] My work is pushed to `Week_3`.

## 8. Commit and push

Push your work to `Week_3`. Don't merge into `main` this week: Week 4 starts from this branch, and the last ParkPulse session brings everything into `main`.
```bash
git add README.md src/parkpulse.py
git commit -m "Complete Week 3 interactive ParkPulse"
git push origin Week_3
```
