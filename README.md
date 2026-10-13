# ParkPulse — Week 2: Functions, Scope & Decisions

**Branch:** `Week_2` · **Project file:** `src/parkpulse.py` · **You need:** Week 1 finished on `main`

> This README is for Week 2 only. Do **not** copy it into `main`.
> By Week 4, your `main` branch gets one ParkPulse README that covers the whole project.

## Overview

ParkPulse is a command-line tool that helps amusement park staff check attraction capacity and status. Last week you calculated and displayed Sky Loop's utilization with variables, operators, and f-strings. This week you refactor that code into functions and add decisions: ride eligibility, ticket pricing, and capacity rules.

**By the end of this week you can:**

- Refactor repeated behavior into named functions with parameters, docstrings, and return values.
- Trace function calls and explain local versus global scope, and read `NameError`, `TypeError`, and `UnboundLocalError`.
- Design clear decisions with `if`/`elif`/`else`, guard clauses, and truthiness (`is None` versus a falsy `0`).
- Apply eligibility, ticket pricing, and capacity rules to ParkPulse, and test their edge cases.

---

## 1. Get the Week 2 starter

You fetch the Week 2 starter into your **existing** `parkpulse` repository. Do these steps in order. Run each command by itself and check the **You should see** line before you go on.

### Start from your Week 1 work on main

**Step 1.** In VS Code, open your `parkpulse` folder (**File → Open Folder…**) and open a terminal (**Terminal → New Terminal**).

**Step 2.** Activate your virtual environment. On Mac:

```bash
source .venv/bin/activate
```

On Windows, run this instead:

```bash
.venv\Scripts\activate
```

**You should see:** your terminal prompt starts with `(.venv)`.

**Step 3.** Switch to `main`:

```bash
git switch main
```

**You should see:** `Switched to branch 'main'` (or `Already on 'main'`). You are now on `main`.

**Step 4.** Check that your work is all committed:

```bash
git status
```

**You should see:** `nothing to commit, working tree clean`. If files are listed, finish Section 8 of the Week 1 README (commit and integrate) before you go on.

**Step 5.** Get the latest `main` from GitHub:

```bash
git pull --ff-only origin main
```

**You should see:** `Already up to date.` (or a short list of updated files).

### Fetch the Week 2 starter

**Step 6.** Check your remotes:

```bash
git remote -v
```

**You should see:** two `origin` lines (your `parkpulse` repository). If two `upstream` lines (the school's `FA26_CLA_Python_Project1_ParkPulse` repository) are also listed, skip Step 7.

**Step 7.** Only if `upstream` was not listed in Step 6, connect the school repository:

```bash
git remote add upstream https://github.com/The-Marcy-Lab-School/FA26_CLA_Python_Project1_ParkPulse.git
```

**You should see:** no output.

**Step 8.** Download the school's Week 2 branch:

```bash
git fetch upstream Week_2
```

**You should see:** a line ending in `Week_2 -> FETCH_HEAD`. Your files do not change yet.

**Step 9.** Create your own Week 2 branch from `main`:

```bash
git switch -c Week_2
```

**You should see:** `Switched to a new branch 'Week_2'`. You are now on `Week_2`, and it starts with your completed Week 1 application. Stay on this branch for all Week 2 work.

**Step 10.** Copy the Week 2 README and practice files onto your branch:

```bash
git restore --source upstream/Week_2 -- README.md practice/
```

**You should see:** no output. `README.md` now shows these Week 2 instructions, and `practice/` holds `01_functions.py`, `02_scope.py`, and `03_decisions.py`.

### Add the Week 2 code to src/parkpulse.py

The school's `src/parkpulse.py` has new Week 2 function stubs at the bottom. **Do not restore the whole file:** it would replace your finished Week 1 code with the empty Week 1 starter. Copy only the Week 2 part.

**Step 11.** Print the school's version of the file in your terminal:

```bash
git --no-pager show upstream/Week_2:src/parkpulse.py
```

**You should see:** the whole starter file. It begins with the Week 1 docstring and TODOs, and further down has the banner `# PARKPULSE — WEEK 2: FUNCTIONS, SCOPE & DECISIONS`.

**Step 12.** In that output, select and copy from the `# ===================================================` line directly **above** `# PARKPULSE — WEEK 2: FUNCTIONS, SCOPE & DECISIONS` down to the last line of the file, `# Compare predictions with actual behavior.` Do not copy anything above that `# ===` line.

**Step 13.** Open your `src/parkpulse.py`, click at the very end of your Week 1 code, add one blank line, paste, and save the file.

**You should see:** your Week 1 code unchanged at the top, then the Week 2 banner, then the three stubs `check_ride_eligibility`, `calculate_ticket_price`, and `check_capacity`.

**Step 14.** Run the file:

```bash
python3 src/parkpulse.py
```

**You should see:** exactly the Week 1 status message you printed last week, and no error. The Week 2 functions are defined but not called yet, so they print nothing.

### Commit the starter

**Step 15.** Check what Git sees:

```bash
git status
```

**You should see:** `On branch Week_2`, `modified: README.md` and `modified: src/parkpulse.py`, and `practice/` under "Untracked files". `.venv/` must **not** be listed.

**Step 16.** Stage the starter files:

```bash
git add README.md practice/ src/parkpulse.py
```

**You should see:** no output.

**Step 17.** Commit them:

```bash
git commit -m "Add Week 2 starter materials"
```

**You should see:** `[Week_2 <commit id>] Add Week 2 starter materials` and `5 files changed`.

**Step 18.** Push your branch to your GitHub repository:

```bash
git push -u origin Week_2
```

**You should see:** `* [new branch] Week_2 -> Week_2` and a line saying the branch is set up to track `origin`.

You are on `Week_2` and ready to begin Week 2.

---

## 2. Readings

Each reading opens with a short real-world scenario in **§1**. **Always read §1 first**: it's the "why" for everything after it. Then read the sections below. Everything else (including **Go further**) is optional.

| Reading | Read | Skip for now |
|---|---|---|
| [Functions](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/03-functions/) | §1 scenario · §5 turning repeated code into a function · §6 what `return` does · §7 scope | §2–4, §8–9 (optional) |
| [Conditional Statements](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/04-conditional-statements/) | §1 scenario · §3 why condition order matters · §4 boolean context (truthy/falsy) · §5 guard clauses | §2, §6–8 (optional) |

### Think about

1. How does a function help eliminate repeated code?
2. What is the difference between `print()` and `return`?
3. What happens when a function is called with the wrong number of arguments?
4. Why might a variable be accessible inside one function but not another?

Be ready to discuss one example in the whole-class debrief.

---

## 3. Practice

The `practice/` folder holds short exercises that are separate from the ParkPulse application. Each file uses the code examples from this week's slides.

| File | Skills | Deck slides |
|---|---|---|
| `practice/01_functions.py` | Functions, parameters, defaults, keyword arguments, returns, print vs. return | 10, 13, 14 |
| `practice/02_scope.py` | Nested calls, local vs. global scope, `NameError`, `TypeError`, `UnboundLocalError` | 12, 16–19 |
| `practice/03_decisions.py` | `if`/`elif`/`else`, truthiness, `is None`, guard clauses, conditional expressions | 23–26 |

For every file:

1. Run it first (it runs before you change anything). Use the command for that file:

```bash
python3 practice/01_functions.py
```

```bash
python3 practice/02_scope.py
```

```bash
python3 practice/03_decisions.py
```

2. Read each section's **Predict** comment and write your prediction as a comment on the `# Your prediction:` line, before you look at the output.
3. Replace every `None` marked `# TODO` with your answer, run the file again, and compare with your prediction.

A line marked `# Uncomment, predict the error, run, then re-comment.` is an error demo: remove the `#` at the start of the line below it, predict the error, run the file, read the last line of the error, then put the `#` back.

These files stay on this week's branch; they never go to `main`.

---

## 4. ParkPulse — Week 2 tasks

**File:** `src/parkpulse.py` · **Branch:** `Week_2`

Complete the Week 2 function stubs using the Business Rules below. The same values are repeated in each function's docstring.

### Business Rules

| Rule | Function | Inputs | Result |
|---|---|---|---|
| Ride eligibility | `check_ride_eligibility(visitor_height, minimum_height)` | Heights in inches. Sky Loop minimum height: 48 inches. | `True` if `visitor_height >= minimum_height` (exactly 48 is eligible); `False` if shorter; `None` if either value is `None`, 0, or negative |
| Ticket pricing | `calculate_ticket_price(ticket_type, base_price)` | `ticket_type` is `"adult"`, `"child"`, or `"senior"` (lowercase). Base price: $60.00 | adult = 100% ($60.00); child = 50% ($30.00); senior = 75% ($45.00); `None` for any other ticket type or a base price that is `None`, 0, or negative |
| Capacity rules | `check_capacity(current_riders, max_capacity)` | Sky Loop max capacity: 24 riders. Utilization = `current_riders / max_capacity` | `"full"` if `current_riders == max_capacity`; `"near capacity"` if utilization is 80% or more (20 of 24 = 83%); otherwise `"available"`; `None` if `max_capacity` is `None`, 0, or negative, or `current_riders` is `None`, negative, or more than `max_capacity` |

### Task A — Refactor into functions

Move your Week 1 utilization calculation into a function, for example `calculate_utilization(current_riders, max_capacity)`, that **returns** the utilization instead of printing it. Put it in your Week 1 code, above the Week 2 banner, and use its return value in your Week 1 status message.

Your functions should:

- Have descriptive snake_case names.
- Take the values they need as parameters (for example `current_riders` and `max_capacity`), not read global variables.
- Include docstrings. Write real ones: they become the "How it's built" section of your portfolio README in Week 4.
- Return values that other code can use.

**Done when:** `python3 src/parkpulse.py` prints the same Week 1 status message as before, including `83.33%`.

### Task B — Ride eligibility

Complete `check_ride_eligibility()` using the eligibility rule in the table.

- Handle missing (`None`) and invalid values first, with guard clauses.
- Then apply the height rule and return the result.

Consider which conditions should be checked first. What happens if you compare `None` to a number?

**Done when:** the three `check_ride_eligibility` rows in the Task E table match.

### Task C — Ticket pricing

Complete `calculate_ticket_price()` using the pricing rules in the table.

- Validate `base_price` with a guard clause.
- Use `if`/`elif`/`else` for the ticket categories.
- Return the price; do not print inside the function.

Consider why returning a value is more flexible than printing it inside the function.

**Done when:** the three `calculate_ticket_price` rows in the Task E table match.

### Task D — Capacity rules

Complete `check_capacity()` using the capacity rules in the table.

- Reuse your Task A utilization function.
- Guard against a zero or missing `max_capacity` **before** dividing.
- Return one of the status strings.
- Keep your Week 1 status message working.

**Done when:** the three `check_capacity` rows in the Task E table match, and your Week 1 status message still prints.

### Task E — Integrate and test

Under the `FEATURE 4: FUNCTION INTEGRATION` comment, call your functions for Sky Loop (for example `check_capacity(20, 24)`), store their return values in variables, and print the results with your Week 1 status message.

Then test each function: at the bottom of `src/parkpulse.py`, add each call below inside `print()`, for example `print(check_ride_eligibility(48, 48))`. Predict each result, then run the file.

**Done when:** `python3 src/parkpulse.py` prints these results, in this order:

| Call | Expected |
|---|---|
| `check_ride_eligibility(48, 48)` | `True` (boundary) |
| `check_ride_eligibility(40, 48)` | `False` |
| `check_ride_eligibility(None, 48)` | `None` |
| `calculate_ticket_price("child", 60.00)` | `30.0` |
| `calculate_ticket_price("vip", 60.00)` | `None` |
| `calculate_ticket_price("adult", -5)` | `None` |
| `check_capacity(20, 24)` | `near capacity` |
| `check_capacity(24, 24)` | `full` |
| `check_capacity(5, 0)` | `None` (no crash) |

The edge-case notes at the bottom of the starter code list more cases to predict.

Do not add interactive menus or loops yet. Those are part of Week 3.

---

## 5. AI activity

Use AI to suggest extra inputs that might reveal problems in your code. Copy this prompt exactly:

```
Suggest five unusual or boundary-case inputs that could test a Python ride eligibility function. Do not write the function or provide implementation code.
```

For each input the AI suggests:

1. Predict the expected behavior using the Business Rules table, and write it down.
2. Run your function with that input inside `print()`.
3. Compare your prediction with the actual result, and explain any difference.
4. Decide whether the AI suggestion was useful, and keep the test if it was.

**AI can suggest test cases, but you are responsible for the expected behavior and implementation.**

---

## 6. Interview prep

An interviewer asks:

**"Why did you refactor that ParkPulse logic into a function?"**

Prepare a 60–90-second answer using Point → Reason → Evidence → Takeaway:

- **Point:** What behavior did you extract into a function?
- **Reason:** Why does that structure help (reuse, testing one rule at a time, clearer names)?
- **Evidence:** Name one function, one input, and the result you observed, for example `check_capacity(5, 0)` returning `None` instead of crashing.
- **Takeaway:** How does that structure improve correctness?

Be ready to explain how you verified one edge case.

---

## 7. Checklist

- [ ] My completed Week 1 application was on `main` before I started.
- [ ] I fetched the school's `Week_2` starter onto my own `Week_2` branch and kept my Week 1 code.
- [ ] I completed the Functions reading.
- [ ] I ran all three practice files, wrote my predictions, and replaced every `None` marked `# TODO`.
- [ ] Task A: my utilization calculation is a function that returns a value, and the Week 1 status message still prints.
- [ ] Task B: `check_ride_eligibility()` is complete, with guard clauses for `None`, 0, and negative heights.
- [ ] Task C: `calculate_ticket_price()` is complete and returns $60.00 / $30.00 / $45.00 prices.
- [ ] Task D: `check_capacity()` is complete and never divides by 0.
- [ ] Task E: every call in the Task E table prints its expected result.
- [ ] I can explain one design decision using a function, an input, and an observed result.
- [ ] My Week 2 work is committed and pushed to `Week_2`.
- [ ] My finished `src/parkpulse.py` is integrated into `main`.

---

## 8. Commit, push, and integrate into main

### Commit and push your Week 2 work

**Step 1.** Check your branch:

```bash
git branch --show-current
```

**You should see:** `Week_2`. If you see anything else, run `git switch Week_2` first.

**Step 2.** Check what changed:

```bash
git status
```

**You should see:** `modified: src/parkpulse.py`, plus any practice files you edited. `.venv/` must not be listed.

**Step 3.** Stage your work:

```bash
git add src/parkpulse.py practice/ README.md
```

**You should see:** no output.

**Step 4.** Commit it:

```bash
git commit -m "Complete Week 2 ParkPulse functions"
```

**You should see:** `[Week_2 <commit id>] Complete Week 2 ParkPulse functions`.

**Step 5.** Push it:

```bash
git push origin Week_2
```

**You should see:** a line ending in `Week_2 -> Week_2`. Your work is saved on your GitHub repository's `Week_2` branch.

### Integrate your finished application into main

Do this once your Week 2 application is complete and your instructor has reviewed it. Copy only `src/parkpulse.py` into `main`. Do **not** bring this README or `practice/` into `main`: they are Week 2 instructions only.

**Step 6.** Switch to `main`:

```bash
git switch main
```

**You should see:** `Switched to branch 'main'`. You are now on `main`.

**Step 7.** Get the latest `main` from GitHub:

```bash
git pull --ff-only origin main
```

**You should see:** `Already up to date.` (or a short list of updated files).

**Step 8.** Copy only your finished application file from your Week 2 branch:

```bash
git restore --source Week_2 -- src/parkpulse.py
```

**You should see:** no output.

**Step 9.** Check that only the application file changed:

```bash
git status
```

**You should see:** `On branch main` and `modified: src/parkpulse.py`, and nothing else. `README.md` and `practice/` must not be listed.

**Step 10.** Stage it:

```bash
git add src/parkpulse.py
```

**You should see:** no output.

**Step 11.** Commit it:

```bash
git commit -m "Integrate Week 2 ParkPulse features"
```

**You should see:** `[main <commit id>] Integrate Week 2 ParkPulse features` and `1 file changed`.

**Step 12.** Push `main`:

```bash
git push origin main
```

**You should see:** a line ending in `main -> main`.

Your `main` branch now has the cumulative working application and `.gitignore`, not the weekly README or practice files. Week 3 starts from this `main`.

---

## Optional practice

- Complete the Conditional Statements interactive reading.
- Trace more functions that use default arguments, keyword arguments, and scope.
- Test more edge cases from the edge-case notes at the bottom of `src/parkpulse.py`.
- Finish any remaining Week 2 function work.

**Next week:** Loops, strings, and interactive input.
