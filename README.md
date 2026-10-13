# ParkPulse — Week 1: Python Launch — Syntax, State & Operators

**Branch:** `Week_1` · **Project file:** `src/parkpulse.py` · **You need:** a GitHub account, VS Code with the Python extension, and Python 3 from the Miniconda setup in class

> This README is for Week 1 only. Do **not** copy it into `main`.
> By Week 4, your `main` branch gets one ParkPulse README that covers the whole project.

## Overview

ParkPulse is a command-line tool for monitoring amusement park attraction capacity and status. A park operations team needs a quick summary of ride capacity and utilization so staff can decide whether an attraction's status looks healthy. Across Weeks 1–4 you build it in one file, `src/parkpulse.py`; this week you set up your repository and Python environment, then calculate and display one attraction's status using variables, expressions, and operators.

**By the end of this week you can:**

- Create your own ParkPulse repository and a `.venv`, select the interpreter in VS Code, and run a file with `python3`.
- Explain what the interpreter does, and tell comments, expressions, and statements apart.
- Predict the value and type of arithmetic, comparison, logical, membership, and identity expressions before you run them.
- Use variables, `print()`, and f-strings (including `:.2%`) to display one attraction's status.
- Write code that follows PEP 8: snake_case names and spaces around operators.

---

## 1. Get the Week 1 starter

Do these steps in order. Run each command by itself and check the **You should see** line before you go on.

### Create your repository

**Step 1.** On the school's ParkPulse repository page on GitHub, click **Use this template**, then **Create a new repository**. Name it `parkpulse`, make sure the owner is your GitHub account, and click **Create repository**. Do **not** fork the school repository.

**You should see:** your new repository page, `github.com/<your-username>/parkpulse`, with `README.md`, `.gitignore`, and `src/`.

**Step 2.** On your new repository page, click **Code** and copy the HTTPS URL. In a terminal, clone it (paste your URL in place of `<your-repository-url>`):

```bash
git clone <your-repository-url>
```

**You should see:** `Cloning into 'parkpulse'...` and no error.

**Step 3.** In VS Code, choose **File → Open Folder…**, open the `parkpulse` folder you just cloned, then open a terminal with **Terminal → New Terminal**. Every command from here on runs in this VS Code terminal.

**Step 4.** Check which branch you are on:

```bash
git branch --show-current
```

**You should see:** `main`

### Fetch the Week 1 starter

**Step 5.** Connect the school repository under the name `upstream`:

```bash
git remote add upstream https://github.com/The-Marcy-Lab-School/FA26_CLA_Python_Project1_ParkPulse.git
```

**You should see:** no output. (If you see `error: remote upstream already exists`, it was added earlier; go on to Step 6.)

**Step 6.** Check your remotes:

```bash
git remote -v
```

**You should see:** four lines: two for `origin` (your `parkpulse` repository) and two for `upstream` (the school's `FA26_CLA_Python_Project1_ParkPulse` repository).

**Step 7.** Download the school's Week 1 branch:

```bash
git fetch upstream Week_1
```

**You should see:** a line ending in `Week_1 -> FETCH_HEAD`. Your files do not change yet.

**Step 8.** Create your own Week 1 branch:

```bash
git switch -c Week_1
```

**You should see:** `Switched to a new branch 'Week_1'`. You are now on `Week_1`. Stay on this branch for all Week 1 work.

**Step 9.** Copy the Week 1 starter files (this README, `src/parkpulse.py`, and `practice/`) onto your branch. Week 1 has no earlier code, so you take the whole starter file:

```bash
git restore --source upstream/Week_1 -- README.md src/parkpulse.py practice/
```

**You should see:** no output. In the VS Code Explorer, `README.md` now shows these Week 1 instructions, and `src/parkpulse.py` and the `practice/` folder appear.

### Set up Python

**Step 10.** Confirm Python 3 is installed:

```bash
python3 --version
```

**You should see:** `Python 3.` followed by a version number, for example `Python 3.12.4`. If you see `command not found`, finish the Miniconda setup from class first, then come back to this step.

**Step 11.** Create a virtual environment inside your repository:

```bash
python3 -m venv .venv
```

**You should see:** no output, and a `.venv` folder in the Explorer. `.venv/` is a private Python environment for this project only. It is **not** project code, and `.gitignore` already keeps it out of Git.

**Step 12.** Activate the environment. On Mac:

```bash
source .venv/bin/activate
```

On Windows, run this instead:

```bash
.venv\Scripts\activate
```

**You should see:** your terminal prompt now starts with `(.venv)`.

**Step 13.** Select the interpreter in VS Code: open the Command Palette (**Cmd+Shift+P** on Mac, **Ctrl+Shift+P** on Windows), run **Python: Select Interpreter**, and choose the one inside `.venv` (it shows `('.venv': venv)`).

**You should see:** `('.venv': venv)` in the bottom-right corner of VS Code when `src/parkpulse.py` is open.

**Step 14.** Check that the terminal uses that interpreter:

```bash
which python3
```

**You should see:** a path ending in `parkpulse/.venv/bin/python3`. (On Windows, `which` may not exist; check that the prompt starts with `(.venv)` instead.)

**Step 15.** Run the starter:

```bash
python3 src/parkpulse.py
```

**You should see:** nothing printed and no error. That is expected: the starter is only a docstring and TODO comments. No error means Python, your interpreter, and the file path all work.

### Commit the starter

**Step 16.** Check what Git sees:

```bash
git status
```

**You should see:** `On branch Week_1`, then `modified: README.md` under "Changes not staged for commit", and `practice/` and `src/parkpulse.py` under "Untracked files". `.venv/` must **not** be listed. If it is, stop and ask your instructor before committing.

**Step 17.** Stage the starter files:

```bash
git add README.md src/parkpulse.py practice/
```

**You should see:** no output.

**Step 18.** Commit them:

```bash
git commit -m "Add Week 1 starter materials"
```

**You should see:** `[Week_1 <commit id>] Add Week 1 starter materials` and `5 files changed`.

**Step 19.** Push your branch to your GitHub repository:

```bash
git push -u origin Week_1
```

**You should see:** `* [new branch] Week_1 -> Week_1` and a line saying the branch is set up to track `origin`.

You are on `Week_1` and ready to begin Week 1.

---

## 2. Readings

Each reading opens with a short real-world scenario in **§1**. **Always read §1 first**: it's the "why" for everything after it. Then read the sections below. Everything else (including **Go further**) is optional.

| Reading | Read | Skip for now |
|---|---|---|
| [Intro to Programming](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/01-intro-to-programming/) | §1 scenario · §3 three kinds of line · §4 running the file with the interpreter · §6 control flow | §2, §5, §7–9 (optional) |
| [Data Types, Variables, and Operators](https://the-marcy-lab-school.github.io/SWE_Interactive_Readings/Mod1/02-data-types-variables-operators/) | §1 scenario · §3 every value has a type · §4 the six families of operators · §6 variables | §2, §5, §7–8 (optional) |

### Think about

1. What is the difference between an expression and a statement?
2. Why does `24 / 5` give a different type than `24 // 5`?
3. What is the difference between `==` and `is`?
4. Which JavaScript habits (`console.log`, `===`, `&&`, braces, semicolons) have a different form in Python?

Be ready to discuss one example in the whole-class debrief.

---

## 3. Practice

The `practice/` folder holds short exercises that are separate from the ParkPulse application. Each file uses the code examples from this week's slides, with neutral values.

| File | Skills | Deck slides |
|---|---|---|
| `practice/01_trace_and_state.py` | Top-to-bottom control flow, comments vs. expressions vs. statements, `print()` and f-strings, `NameError` | 12, 14, 15 |
| `practice/02_types_operators.py` | `type()`, `/` vs. `//` vs. `%`, `"3" * 5`, floating-point surprises, conversions, `==` vs. `is`, `and`/`or`/`not`, `in`, `TypeError` | 17, 18, 19 |
| `practice/03_names_style.py` | Variables, ALL_CAPS constants, `+=`, snake_case, PEP 8 rewrite | 20, 21 |

For every file:

1. Run it first (it runs before you change anything). Use the command for that file:

```bash
python3 practice/01_trace_and_state.py
```

```bash
python3 practice/02_types_operators.py
```

```bash
python3 practice/03_names_style.py
```

2. Read each section's **Predict** comment and write your prediction as a comment on the `# Your prediction:` line, before you look at the output.
3. Replace every `None` marked `# TODO` with your answer, run the file again, and compare with your prediction.

A line marked `# Uncomment, predict the error, run, then re-comment.` is an error demo: remove the `#` at the start of the line below it, predict the error, run the file, read the last line of the error, then put the `#` back.

These files stay on this week's branch; they never go to `main`.

---

## 4. ParkPulse — Week 1 tasks

**File:** `src/parkpulse.py` · **Branch:** `Week_1`

Complete TODO 1–4 in the starter using the attraction data below. The same data is in the file's docstring.

### Business Rules

| Data | Value | Python type |
|---|---|---|
| Attraction name | Sky Loop | `str` |
| Maximum capacity | 24 riders | `int` |
| Current riders | 20 | `int` |
| Open | yes | `bool` (`True`) |
| Utilization | current riders ÷ maximum capacity (20 / 24) | `float` (`0.8333333333333334`) |
| Utilization shown as a percentage | format the fraction with `:.2%` in an f-string | printed as `83.33%` |

### Task A — Store the attraction data (TODO 1)

Store each value from the table in its own variable, below the TODO 1 comment. Use snake_case names (or ALL_CAPS for a value you treat as a constant) and the Python type from the table.

**Done when:** `python3 src/parkpulse.py` runs with no error (it still prints nothing).

### Task B — Calculate utilization (TODO 2)

Below the TODO 2 comment, write the utilization expression using your variables, not the numbers `20` and `24`, and store it in a variable.

Before you run it, write down the type and value you expect. Then add two temporary lines, `print(type(...))` and `print(...)`, with your variable inside the parentheses.

**Done when:** those two lines print `<class 'float'>` and `0.8333333333333334`. Then delete the two temporary lines.

### Task C — Display the status (TODO 3)

Below the TODO 3 comment, use `print()` and f-strings to display a readable status message with the attraction name, its utilization as a percentage, and whether it is open.

**Formatting a percentage:** inside an f-string, `{value:.2%}` multiplies by 100, rounds to 2 decimal places, and adds `%`. Use it on the fraction, not on a value you already multiplied by 100:

```python
utilization = 20 / 24
print(f"Utilization: {utilization:.2%}")        # Utilization: 83.33%
print(f"Utilization: {utilization * 100:.2%}")  # Utilization: 8333.33%  <- multiplied twice
```

**Done when:** `python3 src/parkpulse.py` prints the name, the utilization percentage, and the open status. Your wording can differ, but the values must match. For example:

```
Ride: Sky Loop
Open: True
Capacity used: 20/24
Utilization: 83.33%
```

If you see `83.33333333333334%`, you printed the raw value; add the `:.2%` format spec. Week 3 adds more format specs (`:.2f`) and compares them with `round()`.

### Task D — Style review (TODO 4)

Check your code against PEP 8: snake_case names, spaces around operators, one statement per line, no semicolons or braces.

**Done when:** every line passes those four checks and `python3 src/parkpulse.py` prints exactly the same output as in Task C.

Do not add `if` statements or functions yet. Those are part of Week 2.

---

## 5. AI activity

Use AI as a tutor, not an autopilot. Copy this prompt exactly, then paste one expression from your practice files or `src/parkpulse.py` after it:

```
Act as a tutor. Do not give me the answer yet. Ask me what this Python expression will evaluate to, then give me a hint if my prediction is wrong.
```

For each expression:

1. Write your prediction (value and type) before you send it.
2. Answer the AI's question.
3. Run the code and compare the terminal output with your prediction and the AI's explanation.
4. Decide: if the AI suggests a line of code, run it and verify it before you keep it.

**Terminal output is your evidence. AI can explain, but you are responsible for every line in your code.**

---

## 6. Interview prep

An interviewer asks:

**"What is the difference between an expression and a statement in Python?"**

Prepare a 60–90-second answer using Point → Reason → Evidence → Takeaway:

- **Point:** Answer in one sentence.
- **Reason:** Why does the difference matter?
- **Evidence:** Point to one line in `src/parkpulse.py` and say what it did: produced a value (your utilization expression) or changed state (an assignment).
- **Takeaway:** How does this distinction help you debug?

Be ready to explain one way Python differs from JavaScript, for example `==` versus `===`, or indentation versus braces.

---

## 7. Checklist

- [ ] I created my own `parkpulse` repository from the template (not a fork).
- [ ] I created and activated `.venv`, selected it in VS Code, and `.venv/` is not committed.
- [ ] I fetched the school's `Week_1` starter onto my own `Week_1` branch.
- [ ] I completed the Intro to Programming and Data Types, Variables, and Operators readings.
- [ ] I ran all three practice files, wrote my predictions, and replaced every `None` marked `# TODO`.
- [ ] Task A: my attraction data uses clearly named variables of the correct types.
- [ ] Task B: my utilization is calculated from variables, not typed-in numbers.
- [ ] Task C: `python3 src/parkpulse.py` prints the name, utilization percentage (`83.33%`), and open status.
- [ ] Task D: my code follows PEP 8.
- [ ] I can explain an expression versus a statement using a line of my code.
- [ ] My Week 1 work is committed and pushed to `Week_1`.
- [ ] My finished `src/parkpulse.py` is integrated into `main`.

---

## 8. Commit, push, and integrate into main

### Commit and push your Week 1 work

**Step 1.** Check your branch:

```bash
git branch --show-current
```

**You should see:** `Week_1`. If you see anything else, run `git switch Week_1` first.

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
git commit -m "Complete Week 1 ParkPulse status"
```

**You should see:** `[Week_1 <commit id>] Complete Week 1 ParkPulse status`.

**Step 5.** Push it:

```bash
git push origin Week_1
```

**You should see:** a line ending in `Week_1 -> Week_1`. Your work is saved on your GitHub repository's `Week_1` branch.

### Integrate your finished application into main

Do this once your Week 1 application is complete and your instructor has reviewed it. Copy only `src/parkpulse.py` into `main`. Do **not** bring this README or `practice/` into `main`: they are Week 1 instructions only.

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

**Step 8.** Copy only your finished application file from your Week 1 branch:

```bash
git restore --source Week_1 -- src/parkpulse.py
```

**You should see:** no output.

**Step 9.** Check that only the application file changed:

```bash
git status
```

**You should see:** `On branch main` and `src/parkpulse.py` under "Untracked files" (it is new on `main`). `README.md` and `practice/` must not be listed.

**Step 10.** Stage it:

```bash
git add src/parkpulse.py
```

**You should see:** no output.

**Step 11.** Commit it:

```bash
git commit -m "Integrate Week 1 ParkPulse status"
```

**You should see:** `[main <commit id>] Integrate Week 1 ParkPulse status` and `1 file changed`.

**Step 12.** Push `main`:

```bash
git push origin main
```

**You should see:** a line ending in `main -> main`.

Your `main` branch now has the working application and `.gitignore`, not the weekly README or practice files. Week 2 starts from this `main`.

---

## Optional practice

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
