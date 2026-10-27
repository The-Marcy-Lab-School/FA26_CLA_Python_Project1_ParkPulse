# ParkPulse — Week 4: Lists, References & Project Delivery

**Branch:** `Week_4` · **Project file:** `src/parkpulse.py` · **You need:** Week 3 finished on `main`

## Overview

ParkPulse helps amusement park staff check attraction capacity and status. In Weeks 1–3 you built one attraction's status, rule functions, and an interactive menu. This week ParkPulse tracks the whole park in a list, and you ship it as a portfolio project.

**This week you will:**
- Read, slice, and change a list, and predict which lines change it.
- Predict aliasing (two names, one list) and copy on purpose.
- Write pure functions that copy first, and unpack tuples with `enumerate`.
- Turn your `main` into a project you can show an employer.

## 1. Get the Week 4 starter

**1.** In your `parkpulse` folder (with `.venv` active), start from your up-to-date `main` and create your branch. Run each command by itself:
```bash
git switch main
git pull --ff-only origin main
git switch -c Week_4
```
**2.** Download the Week 4 starter:
```bash
git fetch upstream Week_4
```
**You should see:** a line ending in `Week_4 -> FETCH_HEAD` (or `upstream/Week_4`).

**3.** Copy this README and the practice files:
```bash
git restore --source upstream/Week_4 -- README.md practice/
```
**You should see:** no output, and the Week 4 files in `practice/`.

**4.** Add the new starter code (don't restore the whole file; it would erase your Week 1–3 code). Print the school's file, copy from the `# ===` line above `# PARKPULSE — WEEK 4` to the end, and paste it at the end of your `src/parkpulse.py`. Then move your `run_menu()` call below it, so it is still the last line:
```bash
git --no-pager show upstream/Week_4:src/parkpulse.py
```
**5.** Commit and push:
```bash
git add README.md practice/ src/parkpulse.py
git commit -m "Add Week 4 starter materials"
git push -u origin Week_4
```

## 2. Readings

Every reading opens with a real-world scenario in §1. Always start there.
- **Read (about 10–15 min):** [Lists, References, and Pure Functions](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/07-lists/): §1 scenario, §2 vocabulary, §3 reading a list without changing it, §4 changing a list in place.
- **Then (about 5 min, after class part 2):** §5 two names, one list, and §6 a function that changed the caller's queue.

Everything else is optional. **Think about:** (1) Which list methods return `None`? (2) When do two names share one list? (3) Why should a helper copy before it changes a list?

## 3. Practice

Open each file in `practice/`, run it (`python3 practice/<file>.py`), then fill in every `None` and complete every `# TODO`. Predict before you run.
Files: `01_list_reads.py` · `02_mutation.py` · `03_2d_lists.py` · `04_loop_remove.py` · `05_aliasing.py` · `06_pure_impure.py` · `07_tuples.py`

## 4. ParkPulse — Week 4 tasks

Complete the stubs below the Week 4 banner in `src/parkpulse.py`. Each docstring repeats the rules. **Business Rules** (Week 1–3 rules still apply):

| Rule | Value |
|---|---|
| Attractions | Sky Loop 24/20 open · River Rapids 16/16 open · Pirate Drop 12/3 closed · Comet Coaster 30/12 open (max/riders) |
| Record shape | `(name, max_capacity, current_riders, is_open)` tuple |
| Status | Week 3's `check_capacity()`: `"full"` at max, `"near capacity"` at 80% or more, else `"available"` |
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

## 5. Ship it (delivery week)

ParkPulse is finished. Make your `main` look like a real project, not a course exercise.
1. **Clean `src/`:** delete every `TODO`, banner (`# ===`), and `Think:` comment; keep real docstrings; no `pass` bodies left. This must print nothing:
```bash
grep -n "TODO" src/parkpulse.py
```
2. **Write the project README** on `main` (it replaces the template README; this weekly README never goes to `main`): one-line pitch, **Demo** (a real menu run), **How to run**, **How it's built** (one line per function), **Decisions** (for example, why queue helpers are pure), **What's next**.
3. **Test a fresh clone:** clone your repo into a new folder, run `python3 src/parkpulse.py`, and follow your own README.
4. **Pin** `parkpulse` on your GitHub profile.

## 6. AI activity

Paste one of your Week 4 functions and its rule from the Business Rules table after this prompt:
```text
Review this Python function against the rule below. Does it meet the rule? List anything that breaks it. Do not rewrite the code.
```
For each AI point: **label** it accept, reject, or investigate; **run** the case it describes; **decide** with the output or the rule as your evidence.

## 7. Interview prep

**Question:** "Tell me about a project you built." Answer in 90 seconds with STAR:
- **Situation:** who uses ParkPulse and why. **Task:** what you built in four weeks.
- **Action:** one decision, like pure queue helpers. **Result:** what it does now, with one real output.
- **Follow-up (PREP):** "Why a list of tuples?" Point → Reason → Evidence (your menu option 5) → Point.

## 8. Checklist

- [ ] I started `Week_4` from `main` and kept my Week 1–3 code.
- [ ] I did the readings and all 7 practice files.
- [ ] Tasks A–D: menu option 5 lists all four attractions, and the queue helpers don't change the caller's list.
- [ ] Ship it: no `TODO` in `src/`, a project README on `main`, a fresh clone runs, and the repo is pinned.
- [ ] My work is pushed to `Week_4` and `src/parkpulse.py` is integrated into `main`.

## 9. Commit, push, and integrate into main

Push your work, then (after your instructor signs off) bring `src/parkpulse.py` into `main` and add your project README there:
```bash
git add README.md practice/ src/parkpulse.py
git commit -m "Complete Week 4 park-wide ParkPulse"
git push origin Week_4
git switch main
git pull --ff-only origin main
git restore --source Week_4 -- src/parkpulse.py
git add src/parkpulse.py
git commit -m "Integrate Week 4 ParkPulse application"
git push origin main
```
Then write the project README on `main` (Ship it, step 2), commit it, and push. Never move this weekly `README.md` or `practice/` to `main`.
