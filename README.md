# ParkPulse — Week 3: Loops, Strings & Interactive Input

**Branch:** `Week_3` · **Project file:** `src/parkpulse.py` · **You need:** Week 2 finished on `main`

## Overview

ParkPulse helps amusement park staff check the status of an attraction. In Weeks 1–2 you calculated Sky Loop's utilization and wrote functions for ride eligibility, ticket pricing, and capacity. This week you make ParkPulse interactive: a menu that repeats until the user exits, a queue simulation, cleaned and validated input, and a readable attraction summary.

**By the end of this week you can:**

- Choose a `for` or `while` loop for a task and explain why it fits.
- Trace `range()`, loops over strings, `break`, and `continue`, and predict how many times a loop runs.
- Clean, validate, and convert user input before you use it.
- Explain the difference between `:.2f` and `round()`, and prove your loop ends.

---

## 1. Get your Week 3 starter

Do these steps in the VS Code terminal, inside your personal ParkPulse repository.

1. Check that your work is saved:

   ```bash
   git status
   ```

   **You should see:** `nothing to commit, working tree clean`. If you see changed files, commit them on the branch you're on before you continue.

2. Check your remotes:

   ```bash
   git remote -v
   ```

   **You should see:** `origin` pointing to your personal repository. If `upstream` is also listed, skip step 3.

3. Connect the school repository as `upstream` (only if step 2 didn't list it):

   ```bash
   git remote add upstream https://github.com/The-Marcy-Lab-School/FA26_CLA_Python_Project1_ParkPulse.git
   ```

   **You should see:** no output. Run `git remote -v` again and `upstream` is listed.

4. Download the instructor's Week 3 branch:

   ```bash
   git fetch upstream Week_3
   ```

   **You should see:** a line ending in `Week_3 -> upstream/Week_3`.

5. Switch to `main` and get your latest work:

   ```bash
   git switch main
   ```

   ```bash
   git pull --ff-only origin main
   ```

   **You should see:** `Already up to date.` (or a list of updated files). You are on `main`.

6. Create your Week 3 branch from `main`:

   ```bash
   git switch -c Week_3
   ```

   **You should see:** `Switched to a new branch 'Week_3'`. You are on `Week_3` from here until section 8.

7. Bring in this README and the Week 3 practice files:

   ```bash
   git restore --source upstream/Week_3 -- README.md practice/
   ```

   **You should see:** no output. `git status` shows `modified: README.md` and a new `practice/` folder.

8. Print the instructor's Week 3 starter code:

   ```bash
   git --no-pager show upstream/Week_3:src/parkpulse.py
   ```

   Don't restore the whole file: it would replace your finished Week 1–2 code.

   1. In the output, find the `# ===` line just above `# PARKPULSE — WEEK 3: LOOPS, STRINGS & INPUT`.
   2. Copy from that line to the end of the output.
   3. Paste it at the bottom of your own `src/parkpulse.py`, below your Week 2 code.
   4. Run `python3 src/parkpulse.py`. **You should see:** your Week 1 status message and Week 2 output, exactly as before. The Week 3 functions don't run yet.

9. Commit and push your starter:

   ```bash
   git add README.md practice/ src/parkpulse.py
   ```

   ```bash
   git commit -m "Add Week 3 starter materials"
   ```

   ```bash
   git push -u origin Week_3
   ```

   **You should see:** `branch 'Week_3' set up to track 'origin/Week_3'`.

Keep using the `.gitignore` from `main`. Never commit `.venv/`.

---

## 2. Readings

Each reading opens with a short real-world scenario in **§1**. **Always read §1 first**: it's the "why" for everything after it. Then read the sections below. Everything else (including **Go further**) is optional.

| Reading | Read | Skip for now |
|---|---|---|
| [Loops](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/05-loops/) | §1 scenario · §4 known count or unknown count · §5 `break`, `continue`, and loops with no way out · §6 running counts | §2–3, §7–9 (optional) |
| [Inputs and Outputs](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/06-inputs-and-outputs/) | §1 scenario · §3 strings, one character at a time · §5 `input()` · §6 turning input into the right type | §2, §4, §7–8 (optional) |

**Think about:**

1. When should a program use a `for` loop instead of a `while` loop?
2. What stops a loop? What makes one run forever?
3. Why does user input need validation before conversion?

---

## 3. Practice

Each file holds the code from this week's slides. The files are neutral (not ParkPulse).

| File | Skills | Deck slides |
|---|---|---|
| `practice/01_loop_trace.py` | `for`, `range()`, running totals, `for` vs `while` | 1, 11, 12 |
| `practice/02_flow_trace.py` | `break`, `continue`, `break` vs `return` | 13, 16 |
| `practice/03_nested_trace.py` | Nested loops, counting iterations | 14 |
| `practice/04_termination.py` | Why a `while` loop ends, stopping a runaway loop with Ctrl+C | 15, 16 |
| `practice/05_string_trace.py` | `strip`/`lower`, indexing, slicing, immutability, string methods | 20, 22 |
| `practice/06_input_trace.py` | `input()`, `isdigit()`, Y/N answers, retry up to 3 times | 21 |
| `practice/07_format_trace.py` | `:.2f` vs `round()`, `sep`, `end` | 22, 23 |

For every file:

1. Run it first: `python3 practice/<file>.py`. It runs before you change anything. (`06_input_trace.py` asks you questions; pressing Enter is fine.)
2. Read each section's **Predict** comment and write your prediction as a comment.
3. Replace every `None` marked `# TODO` with your answer, run again, and compare.

These files stay on this week's branch. They never go to `main`.

---

## 4. ParkPulse — Week 3 tasks

Work in `src/parkpulse.py`, below your Week 2 code. Each function's docstring repeats the rules below.

### Business Rules

The Week 2 rules still apply: Sky Loop minimum height 48 inches; tickets $60.00 adult, $30.00 child, $45.00 senior; capacity `"full"` at 24 of 24 riders and `"near capacity"` at 80% or more.

| Rule | Function | Value |
|---|---|---|
| Menu options | `run_menu()` | `1. Show attraction summary` · `2. Check ride eligibility` · `3. Price a ticket` · `4. Simulate the queue` · `5. Exit` |
| Menu choice | `get_menu_choice()` | After `.strip()`, only `"1"` to `"5"` are valid. Anything else prints `Please enter a number from 1 to 5.` and returns `None`, and the menu shows again. |
| Yes/No answer | `get_yes_no(prompt)` | After `.strip().lower()`: `"y"` or `"yes"` → `True`; `"n"` or `"no"` → `False`; anything else prints `Please answer Y or N.` and returns `None`. |
| Whole number | `get_numeric_input(prompt)` | After `.strip()`, valid if `.isdigit()` is `True` (0 or more). Invalid entries print `Please enter a whole number (0 or more).` and ask again. After 3 invalid entries: print `Too many invalid entries.` and return `None`. |
| Exit | `run_menu()` | Choice 5 asks `Exit ParkPulse? [Y/N]: `. Yes prints `Goodbye!` and ends the loop. No or an unrecognized answer goes back to the menu. |
| Queue: boarding | `simulate_queue()` | Each ride cycle boards up to 24 guests (Sky Loop's max capacity). If fewer are waiting, all of them board. |
| Queue: time | `simulate_queue()` | Each ride cycle takes 5 minutes. |
| Queue: stop | `simulate_queue()` | Stop when 0 guests are waiting. 0 guests at the start prints `No one is waiting.` |
| Summary | `display_attraction_summary()` | Utilization with `:.2%`; prices with `:.2f`; capacity status from `check_capacity()`. |

### Task A — Clean and validate input

Complete `get_menu_choice()`, `get_yes_no(prompt)`, and `get_numeric_input(prompt)` (FEATURE 5).

**Done when:** you add each test line below to the bottom of the file, run `python3 src/parkpulse.py`, type the answer, and see the expected output. Delete the test lines afterward.

| Test line | You type | You should see |
|---|---|---|
| `print(get_menu_choice())` | ` 3 ` | `3` |
| `print(get_menu_choice())` | `6` | `Please enter a number from 1 to 5.` then `None` |
| `print(get_yes_no("Exit ParkPulse? [Y/N]: "))` | ` Y ` | `True` |
| `print(get_yes_no("Exit ParkPulse? [Y/N]: "))` | `no` | `False` |
| `print(get_yes_no("Exit ParkPulse? [Y/N]: "))` | `maybe` | `Please answer Y or N.` then `None` |
| `print(get_numeric_input("Guests in line: "))` | ` 7 ` | `7` |
| `print(get_numeric_input("Guests in line: "))` | `-3`, then `50` | the error message once, then `50` |
| `print(get_numeric_input("Guests in line: "))` | `-3`, `3.5`, `abc` | the error message 3 times, `Too many invalid entries.`, then `None` |

### Task B — Interactive menu

Complete `run_menu()` (FEATURE 6). It repeats until the user confirms Exit, and it reuses your Week 2 functions: `check_ride_eligibility()` for choice 2 and `calculate_ticket_price()` for choice 3. The docstring lists the exact message for each result.

**Done when:** you add `run_menu()` as the last line of the file, run `python3 src/parkpulse.py`, and this session matches (your Week 1–2 output prints first; what you type is after each `:`):

```text
ParkPulse — Sky Loop
1. Show attraction summary
2. Check ride eligibility
3. Price a ticket
4. Simulate the queue
5. Exit
Choose an option (1-5): 9
Please enter a number from 1 to 5.

ParkPulse — Sky Loop
...menu...
Choose an option (1-5): 2
Visitor height in inches: 47.5
Please enter a whole number (0 or more).
Visitor height in inches: 47
Not tall enough: Sky Loop requires 48 inches.

ParkPulse — Sky Loop
...menu...
Choose an option (1-5): 2
Visitor height in inches: 48
Eligible to ride Sky Loop.

ParkPulse — Sky Loop
...menu...
Choose an option (1-5): 3
Ticket type (adult/child/senior):  Child
child ticket: $30.00

ParkPulse — Sky Loop
...menu...
Choose an option (1-5): 3
Ticket type (adult/child/senior): vip
Unknown ticket type. Choose adult, child, or senior.

ParkPulse — Sky Loop
...menu...
Choose an option (1-5): 5
Exit ParkPulse? [Y/N]: n

ParkPulse — Sky Loop
...menu...
Choose an option (1-5): 5
Exit ParkPulse? [Y/N]:  y
Goodbye!
```

(`...menu...` stands for the five menu lines, which print every time.) Keep the `run_menu()` line: it is how the app starts from now on.

### Task C — Queue simulation

Complete `simulate_queue()` (FEATURE 7) using the queue rules. Use a loop that stops when no one is waiting, and reuse `check_capacity()` for each cycle's status.

**Done when:** menu choice 4 gives these results:

```text
Choose an option (1-5): 4
Guests in line: 50
Cycle 1: 24 board (full), 26 still waiting
Cycle 2: 24 board (full), 2 still waiting
Cycle 3: 2 board (available), 0 still waiting
Line cleared. Ride cycles: 3. Total time: 15 minutes.
```

```text
Choose an option (1-5): 4
Guests in line: 20
Cycle 1: 20 board (near capacity), 0 still waiting
Line cleared. Ride cycles: 1. Total time: 5 minutes.
```

```text
Choose an option (1-5): 4
Guests in line: 0
No one is waiting.
```

### Task D — Attraction summary

Complete `display_attraction_summary()` (FEATURE 8). Use your Week 1 variables and your Week 2 functions; don't type the numbers into the output by hand.

**Done when:** menu choice 1 prints exactly:

```text
Sky Loop summary
  Open: yes
  Riders: 20 of 24
  Utilization: 83.33%
  Capacity: near capacity
  Tickets: adult $60.00, child $30.00, senior $45.00
```

### Task E — Integrate and test

`run_menu()` is the last line of `src/parkpulse.py` (FEATURE 9). Then run the 8 cases in the "WEEK 3: TESTING AND DEBUGGING" comment at the bottom of the starter code. Predict each result first.

**Done when:**

- Every session in Tasks A–D matches.
- Your Week 1 status message still prints first, and your Week 2 functions still give the same results: `check_ride_eligibility(48, 48)` → `True`, `calculate_ticket_price("child", 60.00)` → `30.0`, `check_capacity(24, 24)` → `"full"`, `check_capacity(5, 0)` → `None`.
- No input you type (empty, spaces, letters, negative numbers, decimals) crashes the program.

Don't add Week 4 list features yet.

---

## 5. AI activity: hostile inputs

Ask an AI assistant for inputs that might break your program. Don't ask it for code.

Copy this prompt:

```text
I'm testing a Python command-line menu. It accepts a menu choice from 1 to 5, a Y/N answer, and a whole number of guests (0 or more). Suggest 8 unusual or hostile things a user might type that could break input validation or make a loop run forever. For each one, say what you think could go wrong. Do not write any code.
```

Then, for each suggestion:

1. **Predict** what your program will do. Write it down.
2. **Run** your program and type the input.
3. **Compare** what happened with your prediction.
4. **Decide:** was the AI right? If your program broke, fix it and write down which assumption failed.

You are responsible for the expected behavior. AI can only suggest test cases.

---

## 6. Interview prep

**Question:** "How do you know your loop will terminate?"

Answer in 60–90 seconds with Point → Reason → Evidence → Takeaway:

- **Point:** Which loop did you use in `simulate_queue()` or `run_menu()`, and why that kind (`for` or `while`)?
- **Reason:** What state changes on every pass, and which condition becomes `False` (or which `break` runs)?
- **Evidence:** Your 50-guest run: guests waiting went 50 → 26 → 2 → 0 in 3 cycles. Or: `get_numeric_input()` asks at most 3 times.
- **Takeaway:** What would make the loop infinite (for example, boarding 0 guests per cycle), and how your code prevents it.

---

## 7. Checklist

- [ ] Task A: `get_menu_choice()`, `get_yes_no()`, and `get_numeric_input()` match the Task A table.
- [ ] Task B: the menu session matches and Exit needs a Y.
- [ ] Task C: the queue runs for 50, 20, and 0 guests exactly as shown.
- [ ] Task D: the summary matches line for line.
- [ ] Task E: Week 1–2 output is unchanged, and no input crashes the program.
- [ ] I finished all 7 practice files.
- [ ] I tested the AI's hostile inputs and wrote down what failed.
- [ ] I committed and pushed `Week_3`.
- [ ] I integrated `src/parkpulse.py` into `main`.

---

## 8. Commit, push, and integrate into main

1. Check that you are on `Week_3`:

   ```bash
   git branch --show-current
   ```

   **You should see:** `Week_3`

2. Commit and push your Week 3 work:

   ```bash
   git add README.md practice/ src/parkpulse.py
   ```

   ```bash
   git commit -m "Complete Week 3 interactive ParkPulse"
   ```

   ```bash
   git push origin Week_3
   ```

   **You should see:** a line ending in `Week_3 -> Week_3`.

3. When your instructor signs off on Week 3, bring **only** the application file into `main`. The README and `practice/` stay on `Week_3`.

   ```bash
   git switch main
   ```

   ```bash
   git pull --ff-only origin main
   ```

   ```bash
   git restore --source Week_3 -- src/parkpulse.py
   ```

   ```bash
   git status
   ```

   **You should see:** `modified: src/parkpulse.py` and nothing else.

4. Commit and push `main`:

   ```bash
   git add src/parkpulse.py
   ```

   ```bash
   git commit -m "Integrate Week 3 ParkPulse application"
   ```

   ```bash
   git push origin main
   ```

   **You should see:** a line ending in `main -> main`. Run `python3 src/parkpulse.py` on `main`: the menu starts.

---

## Optional practice

- Predict the output of `range(2, 9, 3)` and of a 3 x 4 nested loop, then run them.
- Build a neutral retry-until-valid example (like section D of `practice/06_input_trace.py`) that asks for a Y/N answer.
- In your own words, explain why `:.2f` and `round()` are different.
- Timed-screen practice:
  - HackerRank · [Loops](https://www.hackerrank.com/challenges/python-loops/problem) (for + range warm-up)
  - HackerRank · [Find a string](https://www.hackerrank.com/challenges/find-a-string/problem) (slicing + running count)
  - LeetCode · [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) (print each value for now; the list version is Week 4)
  - LeetCode · [Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) (explain why the while loop ends)
  - CodingBat · [String-1](https://codingbat.com/python/String-1) (slicing reps)
  - [Python Tutor](https://pythontutor.com/visualize.html): paste your `simulate_queue()` loop, predict, then step through it.

**Next week:** lists, references, and finishing ParkPulse.
