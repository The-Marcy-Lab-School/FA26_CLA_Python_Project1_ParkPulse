# ParkPulse — Week 4: Lists, References & Project Delivery

**Branch:** `Week_4` · **Project file:** `src/parkpulse.py` · **You need:** your `Week_3` branch (Weeks 1–3 come filled in)

## Overview

ParkPulse helps amusement park staff check attraction capacity and status. In Weeks 1–3 you built one attraction's status, rule functions, and an interactive menu. This is the last ParkPulse week: ParkPulse tracks the whole park in a list, then you bring every week together on `main` and ship it as a portfolio project.

**This week you will:**
- Read, slice, and change a list, and predict which lines change it.
- Predict aliasing (two names, one list) and copy on purpose.
- Write pure functions, and unpack tuples with `enumerate`.
- Look back at Weeks 1–4, check the whole project with AI, and turn `main` into a project you can show an employer.

## 1. Get the Week 4 starter

The school's `src/parkpulse.py` has **Weeks 1–3 filled in**, so this week you only write Week 4 code. Start `Week_4` from your `Week_3` branch, then get the starter. This replaces your `src/parkpulse.py` with the school's file:
```bash
git switch Week_3
git switch -c Week_4
git fetch upstream Week_4
git restore --source upstream/Week_4 -- README.md src/parkpulse.py
python3 src/parkpulse.py
```
**You should see:** the Week 1–2 status lines, then the Week 3 menu (choose 5, then Y, to exit).
```bash
git add README.md src/parkpulse.py
git commit -m "Week 4 starter with Weeks 1-3 filled in"
git push -u origin Week_4
```
Only if `git remote -v` does not list `upstream`: `git remote add upstream https://github.com/The-Marcy-Lab-School/FA26_CLA_Python_Project1_ParkPulse.git`

## 2. Readings

Every reading opens with a real-world scenario in §1. Always start there.
- **Read (about 10–15 min):** [Lists, References, and Pure Functions](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/07-lists/): §1 scenario, §2 vocabulary, §3 reading a list without changing it, §4 changing a list in place.
- **Then (about 5 min, after class part 2):** §5 two names, one list, and §6 a function that changed the caller's queue.

Everything else is optional. **Think about:** (1) Which list methods return `None`? (2) When do two names share one list? (3) Why should a helper copy before it changes a list?

## 3. In class: concept, your turn, answer

There are no practice files. Every concept in the deck has a **Your turn** slide (code with a `# TODO` comment) and an **Answer** slide, with examples that use different data from ParkPulse. Then every breakout room builds all the tasks below, and each room teaches one piece.

## 4. ParkPulse — Week 4 tasks

Complete the stubs below the Week 4 banner in `src/parkpulse.py`. Each docstring repeats the rules. **Business Rules** (Week 1–3 rules still apply):

| Rule | Value |
|---|---|
| Attractions | Sky Loop 24/20 open · River Rapids 16/16 open · Pirate Drop 12/3 closed · Comet Coaster 30/12 open (max/riders) |
| Record shape | `(name, max_capacity, current_riders, is_open)` tuple |
| Status | Week 2's `check_capacity()`: `"full"` at max, `"near capacity"` at 80% or more, else `"available"` |
| Closed attraction | prints `N. Name: closed` with no rider count |
| Queue helpers | return a new list; the caller's list never changes |
| Menu | 1–4 as in Week 3, **5 = List attractions**, **6 = Exit** |

**Task A — Park data.** Fill in `ATTRACTIONS` (FEATURE 10) as a list of four tuples.
- **Done when:** `print(len(ATTRACTIONS))` prints 4 and `print(ATTRACTIONS[0])` prints the Sky Loop tuple.

**Task B — List, find, filter.** Complete `list_attractions()`, `find_attraction()`, and `open_attraction_names()` (FEATURE 11).
- **Done when:** `find_attraction(ATTRACTIONS, "  river rapids ")` returns the River Rapids tuple and `"Log Flume"` returns `None`.

**Task C — Pure queue helpers.** Complete `join_queue()` and `board_riders()` (FEATURE 12) so they copy or slice, never change the caller's list.
- **Done when:** after `join_queue(line, "Cy")`, `line` is still `['Ana', 'Ben']`.

**Task D — Menu option 5.** Update `get_menu_choice()` and `run_menu()` (FEATURE 13).
- **Done when:** menu choice 5 prints the four lines below, 6 + Y exits, and 7 shows `Please enter a number from 1 to 6.`
```text
1. Sky Loop: 20/24 riders (near capacity)
2. River Rapids: 16/16 riders (full)
3. Pirate Drop: closed
4. Comet Coaster: 12/30 riders (available)
```

## 5. Look back: Weeks 1–4

| Week | Python you learned | What it added to ParkPulse |
|---|---|---|
| 1 | variables, types, operators, f-strings, `:.2%` | Sky Loop's status line |
| 2 | functions, `return`, `if`/`elif`, guard clauses, scope | eligibility, ticket price and capacity rules |
| 3 | `for`/`while`, `break`/`continue`, string cleaning, input checks | the menu, the queue simulation and the summary |
| 4 | lists, tuples, `enumerate`, copies vs aliases, pure functions | the whole park and safe queue helpers |

**Skills you can name in an interview:** tracing code before you run it, writing small tested functions, validating input so the program never crashes, Git branches and merges, writing a project README, and using AI to review (not write) your code.

## 6. Use AI to validate the whole project

Paste your finished `src/parkpulse.py` and the Business Rules from Weeks 2–4 after this prompt:
```text
Act as a code reviewer. Here is my Python project ParkPulse and its rules. List up to 5 places where the code may not match a rule, crash on unusual input, or change a list it should not. Name the function for each. Do not rewrite the code.
```
For each point: **label** it accept, reject, or investigate; **run** the case it describes; **decide** with the output or the rule as your evidence. Fix only what your run proves.

## 7. Ship it: bring everything into `main`

ParkPulse is finished. This is the only time you merge into `main`, and it brings Weeks 1–4 together.
1. **Clean up `src/`:** remove every `TODO`, banner (`# ===`) and instruction comment, keep real docstrings, and leave no `pass` bodies. This must print nothing:
```bash
grep -n "TODO" src/parkpulse.py
```
2. **Write the project README** in place of this weekly README (same file, `README.md`): a one-line pitch, **Demo** (a real menu run), **How to run**, **How it's built** (one line per function), **Decisions** (for example, why queue helpers are pure), and **What's next**.
3. **Merge into `main`:**
```bash
git rm -r -q --ignore-unmatch practice
git add README.md src/parkpulse.py
git commit -m "ParkPulse: final version"
git push origin Week_4
git switch main
git pull --ff-only origin main
git merge --no-edit Week_4
python3 src/parkpulse.py
git push origin main
```
4. **Test a fresh clone:** clone your repo into a new folder, run `python3 src/parkpulse.py`, and follow your own README.
5. **Pin** `parkpulse` on your GitHub profile.

## 8. Interview prep

**Question:** "Tell me about a project you built." Start with **QAR** (CLA Technical Communication, Week 4): ask one clarifying **Question** ("Do you want the technical details or the big picture?"), state your **Assumption**, name a **Risk**. Then answer in 90 seconds with STAR:
- **Situation:** who uses ParkPulse and why. **Task:** what you built in four weeks.
- **Action:** one decision, like pure queue helpers. **Result:** what it does now, with one real output.
- **Follow-up (PREP):** "Why a list of tuples?" Point → Reason → Evidence (your menu option 5) → Point.

## 9. Checklist

- [ ] I started `Week_4` from `Week_3` with the school's starter (Weeks 1–3 filled in).
- [ ] Tasks A–D: menu option 5 lists all four attractions, and the queue helpers don't change the caller's list.
- [ ] I checked the whole project with AI and backed each label with a run.
- [ ] Ship it: no `TODO` in `src/`, a project README, `Week_4` merged into `main`, a fresh clone runs, and the repo is pinned.
