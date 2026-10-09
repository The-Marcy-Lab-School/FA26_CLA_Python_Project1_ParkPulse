# ParkPulse — Week 1: Python Launch — Syntax, State & Operators

**Project:** ParkPulse  
**Branch:** `week-1-python-launch`

> This README is for Week 1 instructions only.
>
> Do **not** merge this README into `main`.
>
> Your final `main` branch will eventually contain one complete ParkPulse
> README covering the entire Weeks 1–4 project.

## Overview

ParkPulse is a command-line tool for monitoring amusement park attraction capacity and status. A park operations team needs a quick summary of ride capacity and utilization so staff can decide whether an attraction's status looks healthy.

Across Weeks 1–4, you will build the project incrementally. Each week adds to the same application file, `src/parkpulse.py`.

**This week, you will set up your repository and Python environment, then calculate and display one attraction's status using variables, expressions, and operators.**

The repository structure has already been created for you:

```
README.md
.gitignore      (already ignores .venv/ and __pycache__/)
src/
```

### Week 1 Goals

By the end of this week, you will:

- Create your own ParkPulse repository, a `.venv`, and select the Python interpreter in VS Code.
- Run a Python file with `python3` and explain what the interpreter does.
- Tell comments, expressions, and statements apart.
- Predict and verify types and results for arithmetic, comparison, logical, membership, and identity operators.
- Use variables, `print()`, and f-strings to calculate and display attraction status.
- Write code that follows PEP 8: snake_case names and spaces around operators.

---

## 1. Get Your Week 1 Starter

### Step 1 — Create Your Own Repository From the Template

On the school's ParkPulse repository page on GitHub:

1. Click **Use this template**.
2. Choose **Create a new repository**.
3. Name your repository `parkpulse`.
4. Make sure the repository is owned by your GitHub account.
5. Create the repository.

**Do not fork the school repository.**

### Step 2 — Clone Your New Repository

Copy the URL of the repository you just created, then run:

```bash
git clone <your-repository-url>
cd parkpulse
```

Open the `parkpulse` folder in VS Code and open a terminal (**Terminal → New Terminal**).

### Step 3 — Add the School Repository and Fetch Week 1

Your new repository only has `main`. The Week 1 starter lives on the school repository's `week-1-python-launch` branch.

```bash
git remote add upstream https://github.com/The-Marcy-Lab-School/FA26_CLA_Python_Project1_ParkPulse.git
git fetch upstream week-1-python-launch
```

If `upstream` already exists, skip the `git remote add` command.

### Step 4 — Create Your Week 1 Branch and Add the Starter

```bash
git switch -c week-1-python-launch
git restore --source upstream/week-1-python-launch -- README.md src/parkpulse.py practice/
```

You now have this README, the starter file `src/parkpulse.py`, and the `practice/` folder.

### Step 5 — Create and Activate a Virtual Environment

Confirm Python 3 is installed (use the Miniconda setup from class if it isn't):

```bash
python3 --version
```

Create the environment inside your repository and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate with `.venv\Scripts\activate` instead. Your terminal prompt should now start with `(.venv)`.

`.venv/` is a private Python environment for this project only. It is **not** project code: `.gitignore` already keeps it out of Git.

### Step 6 — Select the Interpreter in VS Code

1. Open the Command Palette (**Cmd+Shift+P** on Mac, **Ctrl+Shift+P** on Windows).
2. Run **Python: Select Interpreter**.
3. Choose the interpreter inside `.venv` (it shows `('.venv': venv)`).

Check the terminal is using it:

```bash
which python3
```

The path should end in `parkpulse/.venv/bin/python3`.

### Step 7 — Run the Starter

```bash
python3 src/parkpulse.py
```

Nothing prints yet. That is expected: the starter is only a docstring and TODO comments. No error means Python, your interpreter, and the file path all work.

### Step 8 — Commit Your Starter

```bash
git status
git add README.md src/parkpulse.py practice/
git commit -m "Add Week 1 starter materials"
git push -u origin week-1-python-launch
```

`git status` must **not** list `.venv/`. If it does, stop and ask your instructor before committing.

You are ready to begin Week 1 development.

---

## 2. Interactive Readings — Intro to Programming; Data Types, Variables & Operators

**Required:** Instructor-assigned sections of the Intro to Programming and Data Types, Variables, and Operators GitBook readings.

Focus on:

- What a program, the interpreter, and default (top-to-bottom) control flow are
- Comments, expressions, and statements
- `str`, `int`, `float`, `bool`, and `None`
- Arithmetic (`/`, `//`, `%`), comparison, logical, membership, and identity operators
- Variables, constants, and snake_case naming

### Think About

1. What is the difference between an expression and a statement?
2. Why does `24 / 5` give a different type than `24 // 5`?
3. What is the difference between `==` and `is`?
4. Which JavaScript habits (`console.log`, `===`, `&&`, braces, semicolons) have a different form in Python?

Be prepared to discuss one example during our whole-class debrief.

---

## 3. Python Practice Activities

The `practice/` folder contains short exercises separate from the ParkPulse application. Each file holds the code examples from this week's slides, with neutral values.

| File | Skills | Slides |
|---|---|---|
| `01_trace_and_state.py` | Top-to-bottom control flow, comments vs. expressions vs. statements, `print()` and f-strings, `NameError` | 12, 14, 15 |
| `02_types_operators.py` | `type()`, `/` vs. `//` vs. `%`, `"3" * 5`, floating-point surprises, conversions, `==` vs. `is`, `and`/`or`/`not`, `in`, `TypeError` | 17, 18, 19 |
| `03_names_style.py` | Variables, ALL_CAPS constants, `+=`, snake_case, PEP 8 rewrite | 20, 21 |

For each file:

1. Predict every printed line before running it, and write your predictions down.
2. Run the file and compare.
3. Answer the lettered prompts at the bottom of the file. Some prompts ask you to uncomment a line that raises an error: run it, read the last line of the error, then comment it back out.

```bash
python3 practice/01_trace_and_state.py
python3 practice/02_types_operators.py
python3 practice/03_names_style.py
```

**Remember:** These practice files are for learning. They are not part of the finished ParkPulse application.

---

## 4. ParkPulse — Week 1 Development

**File:** `src/parkpulse.py`

Complete TODO 1–4 in the starter using the attraction data below. The same data is in the file's docstring.

### Business Rules

| Data | Value | Python type |
|---|---|---|
| Attraction name | Sky Loop | `str` |
| Maximum capacity | 24 riders | `int` |
| Current riders | 20 | `int` |
| Open | yes | `bool` (`True`) |
| Utilization | current riders ÷ maximum capacity (20 / 24) | `float` (`0.8333333333333334`) |
| Utilization as a percentage | utilization × 100 | `float` (`83.33333333333334`) |

### Task A — Store the Attraction Data (TODO 1)

Store each value in a clearly named variable. Use snake_case names (or ALL_CAPS for a value you treat as a constant) and the type from the table.

### Task B — Calculate Utilization (TODO 2)

Write the utilization expression using your variables, not the numbers `20` and `24`.

Before running it, write down the type and value you expect. Then check with `print(type(...))` and `print(...)`, and remove those checks when you are done.

### Task C — Display the Status (TODO 3)

Use `print()` and f-strings to display a readable status message with the attraction name, its utilization as a percentage, and whether it is open.

**Done when:** `python3 src/parkpulse.py` prints all three values. Your wording can differ, but the values must match. For example:

```
Ride: Sky Loop
Open: True
Capacity used: 20/24
Utilization: 83.33333333333334%
```

The long decimal is expected this week. You will learn to format it properly in Week 3.
Optional preview (it's on the slides): `print(f"Utilization: {20 / 24:.2%}")` prints `Utilization: 83.33%` — `:.2%` multiplies by 100 for you, so use it on the fraction, not on a value you already multiplied.

### Task D — Style Review (TODO 4)

Check your code against PEP 8: snake_case names, spaces around operators, one statement per line, no semicolons or braces. Run the file again to confirm the output did not change.

Do not add `if` statements or functions yet. Those are part of Week 2.

---

## 5. AI Tutor Activity

Use AI as a tutor, not an autopilot. Paste one expression from your practice files or `src/parkpulse.py` and use this prompt:

"Act as a tutor. Do not give me the answer yet. Ask me what this Python expression will evaluate to, then give me a hint if my prediction is wrong."

For each expression:

1. Write your prediction (value and type) before you send it.
2. Answer the AI's question.
3. Run the code and compare the terminal output with both your prediction and the AI's explanation.
4. If the AI suggests a line of code, run it and verify it before you keep it.

**Terminal output is your evidence. AI can explain, but you are responsible for every line in your code.**

---

## 6. Interview Connection

Imagine an interviewer asks:

**"What is the difference between an expression and a statement in Python?"**

Prepare a 60–90-second explanation using:

- **Point:** Answer in one sentence.
- **Reason:** Why does the difference matter?
- **Evidence:** Point to one line in `src/parkpulse.py` and say what it did (produced a value, or changed state).
- **Final Point:** How does this distinction help you debug?

Be prepared to explain one way Python differs from JavaScript, for example `==` versus `===`, or indentation versus braces.

---

## 7. Week 1 Completion Checklist

- [ ] I created my own `parkpulse` repository from the template (not a fork).
- [ ] I created and activated `.venv`, selected it in VS Code, and `.venv/` is not committed.
- [ ] I fetched the instructor's `week-1-python-launch` starter.
- [ ] I completed the required Intro to Programming and Data Types, Variables, and Operators readings.
- [ ] I predicted and ran all three practice files and answered their prompts.
- [ ] My attraction data uses clearly named variables of the correct types.
- [ ] My utilization is calculated from variables, not typed-in numbers.
- [ ] `python3 src/parkpulse.py` prints the name, utilization percentage, and open status.
- [ ] My code follows PEP 8.
- [ ] I can explain an expression versus a statement using a line of my code.

---

## 8. Commit and Push Week 1

Confirm your branch:

```bash
git branch --show-current
git status
```

Commit your completed work:

```bash
git add src/parkpulse.py practice/ README.md
git commit -m "Complete Week 1 ParkPulse status"
git push origin week-1-python-launch
```

Your completed work is now saved on your personal repository's `week-1-python-launch` branch.

### Integrate Your Completed Application Into Main

**Do not merge the Week 1 README or `practice/` files into `main`.**

Those are instructional materials for Week 1 only.

Once your Week 1 application is complete and approved, transfer only the finished Python application file:

```bash
git switch main
git pull --ff-only origin main
git restore --source week-1-python-launch -- src/parkpulse.py
git add src/parkpulse.py
git commit -m "Integrate Week 1 ParkPulse status"
git push origin main
```

Your `main` branch should contain the working application and the `.gitignore`, not the weekly instructional README or practice exercises. Week 2 starts from this `main`.

---

## Optional Practice

- Translate these JavaScript lines into Python. Predict each result, then run your version.

```javascript
console.log("Riders: " + 20);
let isFull = 20 === 24;
const canBoard = true && 20 < 24;
console.log(!true);
console.log(24 % 5);
```

- Re-run `practice/02_types_operators.py` with different numbers and predict each result before running.
- Rewrite another small piece of code you wrote in JavaScript using PEP 8 style.

**Next week:** Functions, scope, and decisions.
