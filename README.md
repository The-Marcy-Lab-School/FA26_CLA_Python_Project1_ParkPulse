# ParkPulse — Week 1: Python Launch — Syntax, State & Operators

**Branch:** `Week_1` · **Project file:** `src/parkpulse.py` · **You need:** a GitHub account, VS Code with the Python extension, and Python 3 from the Miniconda setup in class

> This README is for Week 1 only. Do **not** copy it into `main`.

## Overview

ParkPulse is a command-line tool that helps amusement park staff check an attraction's capacity and status. Across Weeks 1–4 you build it in one file, `src/parkpulse.py`. This week you set up your repository and Python, then calculate and display one attraction's utilization.

**This week you will:**

- Create your own ParkPulse repository and a `.venv`, and run a file with `python3`.
- Tell comments, expressions, and statements apart.
- Predict the value and type of an expression before you run it.
- Use variables, `print()`, and f-strings (including `:.2%`) to display a status message.
- Write code that follows PEP 8.

## 1. Get the Week 1 starter

You do this setup once. Run each command by itself, in order.

### Create your repository

**Step 1.** On the school's ParkPulse repository page on GitHub, click **Use this template → Create a new repository**. Name it `parkpulse`, owned by your GitHub account. Do **not** fork it.

**Step 2.** On your new repository page, click **Code** and copy the HTTPS URL. Clone it (paste your URL in place of `<your-repository-url>`):

```bash
git clone <your-repository-url>
```

**Step 3.** In VS Code, choose **File → Open Folder…** and open `parkpulse`. Open **Terminal → New Terminal**. Every command from here on runs in this terminal.

### Fetch the Week 1 starter

**Step 4.** Connect the school repository under the name `upstream` (you do this once; later weeks reuse it):

```bash
git remote add upstream https://github.com/The-Marcy-Lab-School/FA26_CLA_Python_Project1_ParkPulse.git
```

**Step 5.** Download the school's Week 1 branch:

```bash
git fetch upstream Week_1
```

**You should see:** a line ending in `Week_1 -> FETCH_HEAD` (or `upstream/Week_1`). Your files do not change yet.

**Step 6.** Create your own Week 1 branch:

```bash
git switch -c Week_1
```

**Step 7.** Copy the Week 1 starter files onto your branch:

```bash
git restore --source upstream/Week_1 -- README.md src/parkpulse.py practice/
```

**You should see:** no output. `README.md` now shows these instructions, and `src/parkpulse.py` and `practice/` appear in the Explorer.

### Set up Python

**Step 8.** Confirm Python 3 is installed (you should get `Python 3.x.x`; if not, finish the Miniconda setup first):

```bash
python3 --version
```

**Step 9.** Create a virtual environment. `.gitignore` already keeps `.venv/` out of Git.

```bash
python3 -m venv .venv
```

**Step 10.** Activate it. Your prompt then starts with `(.venv)`. On Mac:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

**Step 11.** In VS Code, open the Command Palette (**Cmd+Shift+P** / **Ctrl+Shift+P**), run **Python: Select Interpreter**, and choose the one marked `('.venv': venv)`.

**Step 12.** Run the starter. It prints nothing and shows no error: the starter is only a docstring and TODO comments.

```bash
python3 src/parkpulse.py
```

### Commit the starter

**Step 13.** Check what Git sees:

```bash
git status
```

**You should see:** `On branch Week_1`, `modified: README.md`, and `practice/` and `src/parkpulse.py` as untracked. `.venv/` must **not** be listed; if it is, ask your instructor before you commit.

**Step 14.** Stage, commit, and push:

```bash
git add README.md src/parkpulse.py practice/
git commit -m "Add Week 1 starter materials"
git push -u origin Week_1
```

## 2. Readings

Every reading opens with a real-world scenario in §1 — always start there.

- **Read (about 10–15 min):** [Intro to Programming](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/01-intro-to-programming/) — §1 scenario, §2 technical vocabulary, §3 three kinds of line, §4 running the file, §6 control flow.
- **Skim (about 5 min):** [Data Types, Variables, and Operators](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/02-data-types-variables-operators/) — §1 scenario, §2 vocabulary, glance at §4 the operators.

Everything else, including **Go further**, is optional.

**Think about:**

1. What is the difference between an expression and a statement?
2. Why does `24 / 5` give a different type than `24 // 5`?
3. Which JavaScript habits (`console.log`, `===`, `&&`, braces) look different in Python?

## 3. Practice

Open each file in `practice/` and run it (`python3 practice/<file>.py`). Predict before you run, then fill in every `None` and complete every `# TODO`.

Files: `practice/01_trace_and_state.py` · `practice/02_types_operators.py` · `practice/03_names_style.py`

## 4. ParkPulse — Week 1 tasks

Complete TODO 1–4 in `src/parkpulse.py`. The same data is in the file's docstring.

### Business Rules

| Data | Value | Python type |
|---|---|---|
| Attraction name | Sky Loop | `str` |
| Maximum capacity | 24 riders | `int` |
| Current riders | 20 | `int` |
| Open | yes | `bool` |
| Utilization | current riders ÷ maximum capacity | `float` |

### Task A — Store the attraction data (TODO 1)

Store each value from the table in its own snake_case variable, with the type from the table.

**Done when:** `python3 src/parkpulse.py` runs with no error.

### Task B — Calculate utilization (TODO 2)

Write the utilization expression from your variables (not the numbers `20` and `24`) and store it. Predict its type and value, then check with temporary `print(type(...))` and `print(...)` lines.

**Done when:** they print `<class 'float'>` and `0.8333333333333334`, and you have deleted the temporary lines.

### Task C — Display the status (TODO 3)

Use `print()` and f-strings to show the attraction name, utilization as a percentage, and whether it is open.

**Formatting a percentage:** `{value:.2%}` multiplies by 100, rounds to 2 decimals, and adds `%`. Use it on the fraction, not on a value you already multiplied by 100:

```python
utilization = 20 / 24
print(f"Utilization: {utilization:.2%}")        # Utilization: 83.33%
print(f"Utilization: {utilization * 100:.2%}")  # Utilization: 8333.33%  <- multiplied twice
```

**Done when:** the program prints something like this (your wording can differ, the values must match):

```text
Ride: Sky Loop
Open: True
Capacity used: 20/24
Utilization: 83.33%
```

### Task D — Style review (TODO 4)

Check your code against PEP 8: snake_case names, spaces around operators, one statement per line, no semicolons or braces.

**Done when:** every line passes and the output is unchanged. (No `if` statements or functions yet; those are Week 2.)

## 5. AI activity

Copy this prompt, then paste one expression from your practice files or `src/parkpulse.py` after it:

```text
Act as a tutor. Do not give me the answer yet. Ask me what this Python expression will evaluate to, then give me a hint if my prediction is wrong.
```

1. **Predict** the value and type, and write it down.
2. **Run** the code and compare the output with your prediction.
3. **Decide:** if the AI suggests code, run and verify it before you keep it.

## 6. Interview prep

**Question:** "What is the difference between an expression and a statement in Python?"

Answer in 60–90 seconds with PREP: Point → Reason → Evidence → Point:

- **Point:** one-sentence answer. **Reason:** why the difference matters.
- **Evidence:** one line in `src/parkpulse.py` that produced a value (your utilization) or changed state (an assignment).
- **Point:** restate your answer, then say how the distinction helps you debug.

## 7. Checklist

- [ ] I created `parkpulse` from the template (not a fork) and added `upstream`.
- [ ] `.venv` is active and selected in VS Code, and `.venv/` is not committed.
- [ ] I did the readings and every practice file.
- [ ] Tasks A–D: the program prints the name, `83.33%`, and the open status, in PEP 8 style.
- [ ] I can explain an expression versus a statement using a line of my code.
- [ ] My work is pushed to `Week_1` and `src/parkpulse.py` is integrated into `main`.

## 8. Commit, push, and integrate into main

Commit and push your Week 1 work:

```bash
git add README.md practice/ src/parkpulse.py
git commit -m "Complete Week 1 ParkPulse status"
git push origin Week_1
```

When your instructor signs off, bring **only** the application file into `main`:

```bash
git switch main
git pull --ff-only origin main
git restore --source Week_1 -- src/parkpulse.py
git add src/parkpulse.py
git commit -m "Integrate Week 1 ParkPulse status"
git push origin main
```

Never move `README.md` or `practice/` to `main`; they stay on `Week_1`. Week 2 starts from this `main`.
