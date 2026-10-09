# ParkPulse — Week 3: Loops, Strings & Interactive Input

**Branch:** `Week_3`  
**Project:** ParkPulse

## Overview

In Weeks 1–2, you built the foundation of ParkPulse, calculated ride capacity/utilization, and introduced reusable functions for eligibility, pricing, and capacity rules.

Your completed Week 2 application file should already be integrated into your personal repository's `main` branch.

**This week:** Make ParkPulse interactive by adding loops, user input, validation, and readable attraction summaries.

## 1. Get Your Week 3 Starter

Your instructor has published the `Week_3` starter branch in the school repository.

Open your existing personal ParkPulse repository in VS Code.

First, ensure your Week 2 work is committed and your working tree is clean.

### Check your remotes

```bash
git remote -v
```

Your `origin` should point to your personal repository.

If you have not already connected the school repository:

```bash
git remote add upstream https://github.com/The-Marcy-Lab-School/FA26_CLA_Python_Project1_ParkPulse.git
```

If `upstream` already exists, skip that command.

### Fetch the instructor's Week 3 branch

```bash
git fetch upstream Week_3
```

### Create your Week 3 branch from your completed work

```bash
git switch main
git pull --ff-only origin main
git switch -c Week_3
```

If you already have a local `Week_3` branch, switch to it instead.

### Bring in the Week 3 instructional files

```bash
git restore --source upstream/Week_3 -- README.md practice/
```

Your instructor also added Week 3 function stubs to `src/parkpulse.py`.

Review those additions in the school repository's `Week_3` branch and copy the new function stubs into your existing application.

**Do not overwrite your completed Week 1–2 code.**

Continue using the `.gitignore` inherited from `main`. Do not commit `.venv/`.

## 2. Interactive Readings

### Required: Loops

Read the instructor-assigned sections covering:

- `for` loops and `range()`
- `while` loops
- `break` and `continue`
- Loop termination and running counts

**Think:** When should a program use a `for` loop instead of a `while` loop?

### Required: Inputs and Outputs

Read the instructor-assigned sections covering:

- String indexing and slicing
- String methods
- `input()` and type conversion
- Input validation and formatting

**Think:** Why does user input need validation before conversion?

The classroom reading activities cover selected excerpts, not the complete chapters.

## 3. Python Practice

Complete the exercises in `practice/`.

| File | Focus |
|---|---|
| `01_loop_trace.py` | `for`, `range()`, running counts, and loop tracing |
| `02_string_trace.py` | Indexing, slicing, and string methods |
| `03_input_trace.py` | Input normalization, validation, and conversion |
| `04_formatting.py` | f-strings, decimal formatting, and output |

For each file:

1. Predict the output before running it.
2. Run the code.
3. Explain what happened.
4. Complete the TODOs or extension prompts.

Run the files using:

```bash
python3 practice/01_loop_trace.py
python3 practice/02_string_trace.py
python3 practice/03_input_trace.py
python3 practice/04_formatting.py
```

**These files are for practice only and should not become part of the final ParkPulse application.**

## 4. ParkPulse — Week 3 Development

**File:** `src/parkpulse.py`

Continue working from your completed Week 2 application.

Your instructor has provided starter function definitions and TODOs for this week's features.

### Task A — Input Validation

Complete the starter functions for menu choices and numeric input.

Your implementation should:

- Read input using `input()`.
- Remove unnecessary whitespace with `.strip()`.
- Normalize Y/N responses with `.lower()`.
- Validate numeric input before converting it.
- Handle invalid responses appropriately.

**Consider:** What should happen if someone enters an empty string, a negative number, or an unexpected menu choice?

### Task B — Interactive Menu

Complete the menu functionality.

Your menu should:

- Display available actions.
- Allow users to select an action.
- Repeat until the user chooses to exit.
- Handle invalid selections.
- Reuse existing ParkPulse functions.

**Consider:** Why is a `while` loop appropriate for a menu?

### Task C — Queue Simulation

Complete the queue simulation starter function.

Your implementation should:

- Track the necessary queue-related state.
- Use a loop to simulate repeated activity.
- Update state appropriately.
- Stop when the required condition is met.
- Reuse your existing capacity rules.

**Consider:** What prevents your simulation from running forever?

### Task D — Attraction Summary

Complete the attraction summary functionality.

Your implementation should:

- Reuse existing attraction information.
- Use your Week 1 and Week 2 calculations/functions.
- Format values clearly using f-strings.
- Display readable attraction information.

### Task E — Integrate and Test

Connect the new functions to your existing ParkPulse application.

Verify that:

1. The menu repeats and exits correctly.
2. Invalid menu selections are handled.
3. Y/N inputs work with different capitalization and surrounding spaces.
4. Invalid numeric inputs are handled before conversion.
5. The queue simulation terminates.
6. Attraction summaries display correctly.
7. Week 1 and Week 2 functionality still works.

Do not add Week 4 list-based collection features yet.

## 5. AI Edge-Case Activity

Ask AI to suggest unusual inputs that might break your menu, queue simulation, or input validation.

For each suggested input:

1. Predict the expected behavior.
2. Test your code.
3. Compare the expected and actual results.
4. Explain any differences.

Do not ask AI to complete your ParkPulse implementation.

## 6. Interview Connection

Prepare a brief answer to:

**"How do you know your loop will terminate?"**

Explain:

- Why you chose that loop.
- What state changes during each iteration.
- What causes the loop to stop.
- What test or observed output verifies your explanation.

## 7. Week 3 Completion Checklist

- [ ] My completed Week 2 application file was already integrated into `main`.
- [ ] I fetched the instructor's `Week_3` branch.
- [ ] I preserved my previous ParkPulse work.
- [ ] I practiced loops, strings, input, and formatting.
- [ ] My interactive menu repeats and exits.
- [ ] My queue simulation terminates correctly.
- [ ] User input is cleaned and validated.
- [ ] Attraction summaries are readable.
- [ ] Previous functionality still works.
- [ ] I tested normal and edge-case inputs.
- [ ] I can explain loop termination with evidence.

## 8. Commit and Push Week 3

Confirm your branch:

```bash
git branch --show-current
git status
```

Commit your Week 3 work:

```bash
git add README.md practice/ src/parkpulse.py
git commit -m "Complete Week 3 interactive ParkPulse"
git push -u origin Week_3
```

Use your actual application filename if it differs.

### Important: Keep Instructional Files Out of Main

**Do not merge the Week 3 README or `practice/` folder into `main`.**

These files belong only on the instructional `Week_3` branch.

After completing Week 3 and receiving instructor approval, integrate **only the finished application Python file** into your cumulative `main` branch.

```bash
git switch main
git pull --ff-only origin main
git restore --source Week_3 -- src/parkpulse.py
git status
git add src/parkpulse.py
git commit -m "Integrate Week 3 ParkPulse application"
git push origin main
```

Your `main` branch should retain its existing portfolio README and `.gitignore`, alongside your completed application code.

## Optional Practice

- Finish the Loops and Inputs and Outputs interactive readings.
- Practice tracing nested loops and predicting iteration counts.
- Test additional unusual input scenarios.
- Explain the difference between `:.2f` formatting and `round()`.

**Next week:** Lists, references, and final ParkPulse integration.