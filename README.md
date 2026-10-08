# ParkPulse — Week 2: Functions, Scope & Decisions

**Project:** ParkPulse  
**Branch:** `Week_2`

## Overview

Last week, you built the foundation of ParkPulse using variables, data types, expressions, and operators to calculate ride capacity/utilization and display formatted attraction status.

Your completed Week 1 Python application should already be integrated into your personal repository's `main` branch.

**This week, you will refactor and extend ParkPulse using functions and conditional logic.**

### Week 2 Goals

By the end of this week, you will:

- Create reusable functions with parameters, arguments, docstrings, and return values.
- Trace function calls and explain local versus global scope.
- Use `if`, `elif`, `else`, and guard clauses to make decisions.
- Apply eligibility, ticket pricing, and capacity rules to ParkPulse.
- Predict and test edge cases.

---

## 1. Get Your Week 2 Starter From GitHub

Your instructor has published the Week 2 starter code and practice activities on the school repository's `Week_2` branch.

You will fetch the starter into your **existing personal ParkPulse repository**.

### Step 1 — Open Your Existing Repository

In VS Code, open your ParkPulse project and terminal.

Check your current branch and remotes:

```bash
git status
git remote -v
```

Your `origin` should point to your personal GitHub repository.

### Step 2 — Add the School Repository as a Remote

If you have not already added the school repository:

```bash
git remote add upstream https://github.com/The-Marcy-Lab-School/FA26_CLA_Python_Project1_ParkPulse.git
```

If `upstream` already exists, skip this command.

### Step 3 — Fetch the Week 2 Branch

```bash
git fetch upstream Week_2
```

This downloads your instructor's Week 2 starter without modifying your `main` branch.

### Step 4 — Create Your Week 2 Branch

First, make sure your Week 1 work is committed and your working tree is clean.

```bash
git switch main
git pull --ff-only origin main
git switch -c Week_2
```

Your new branch now starts with your completed Week 1 application.

### Step 5 — Add the Week 2 Starter Materials

Retrieve your instructor's Week 2 README and practice files:

```bash
git restore --source upstream/Week_2 -- README.md practice/
```

Your instructor has also added new Week 2 function starter code to `src/parkpulse.py`.

**Important:** Do not overwrite your completed Week 1 application with the instructor's entire Python file.

Instead:

1. Open the instructor's Week 2 version of `src/parkpulse.py` on GitHub.
2. Identify the newly added Week 2 function definitions and TODOs.
3. Add those new sections to your existing `src/parkpulse.py`.
4. Preserve your completed Week 1 code.

You now have your Week 1 work plus the Week 2 starter.

### Step 6 — Commit Your Starter

```bash
git add README.md practice/ src/parkpulse.py
git commit -m "Add Week 2 starter materials"
git push -u origin Week_2
```

You are ready to begin Week 2 development.

**Continue using your existing `.gitignore`. Do not commit `.venv/`.**

---

## 2. Interactive Reading — Functions

**Required:** Instructor-assigned sections of the Functions interactive GitBook reading.

Focus on:

- Defining and calling functions with `def`
- Parameters and arguments
- Return values
- Local versus global scope

### Think About

1. How does a function help eliminate repeated code?
2. What is the difference between `print()` and `return`?
3. What happens when a function is called with the wrong number of arguments?
4. Why might a variable be accessible inside one function but not another?

Be prepared to discuss one example during our whole-class debrief.

**Optional reading:** Conditional Statements.

---

## 3. Python Practice Activities

The `practice/` folder contains short exercises separate from the ParkPulse application.

| File | Skills |
|---|---|
| `01_functions.py` | Functions, parameters, defaults, keyword arguments, and returns |
| `02_scope.py` | Nested calls, local scope, and debugging |
| `03_decisions.py` | Conditionals, truthiness, and guard clauses |

### Activity A — Functions

**File:** `practice/01_functions.py`

1. Predict the output before running the file.
2. Identify parameters and arguments.
3. Explain default and keyword arguments.
4. Create one new function with a docstring and a return value.
5. Explain the difference between printing and returning.

Run:

```bash
python3 practice/01_functions.py
```

### Activity B — Scope and Debugging

**File:** `practice/02_scope.py`

1. Trace the nested function calls.
2. Identify local variables.
3. Predict what happens when a local variable is accessed outside its function.
4. Explain a `NameError` scenario.
5. Investigate how incorrect function arguments produce `TypeError`.
6. Explain an `UnboundLocalError` scenario.

Run:

```bash
python3 practice/02_scope.py
```

### Activity C — Conditional Decisions

**File:** `practice/03_decisions.py`

1. Predict which branches execute.
2. Compare `if`, `elif`, and `else`.
3. Explain `is None` versus a falsy-value check.
4. Rewrite a nested conditional using guard clauses.
5. Create a conditional expression.

Run:

```bash
python3 practice/03_decisions.py
```

**Remember:** These practice files are for learning. They are not part of the finished ParkPulse application.

---

## 4. ParkPulse — Week 2 Development

**File:** `src/parkpulse.py`

Your instructor has provided Week 2 starter function definitions and TODOs.

Complete them using the approved ParkPulse business requirements.

### Task A — Refactor Into Functions

Review the capacity/utilization logic you wrote during Week 1.

Identify repeated work that should be moved into reusable functions.

Your functions should:

- Have descriptive names.
- Accept appropriate parameters.
- Include docstrings.
- Return values that other code can use.
- Avoid unnecessary reliance on global variables.

**Preserve your working Week 1 calculations and formatted status.**

### Task B — Ride Eligibility

Complete the ride eligibility function.

Your implementation should:

- Accept relevant visitor and attraction information.
- Apply the assigned eligibility requirements.
- Return an appropriate result.
- Handle missing or invalid values.

Consider which conditions should be checked first.

### Task C — Ticket Pricing

Complete the ticket pricing function.

Your implementation should:

- Accept the information needed to determine ticket pricing.
- Apply the assigned pricing rules.
- Use appropriate conditional logic.
- Return the calculated result.
- Handle invalid values.

Consider why returning a value is more flexible than printing it inside the function.

### Task D — Capacity Rules

Complete the capacity rules function.

Your implementation should:

- Reuse or refactor existing Week 1 capacity logic.
- Apply the assigned capacity requirements.
- Use guard clauses where appropriate.
- Return an appropriate result.
- Preserve correct Week 1 behavior.

### Task E — Integrate and Test

Once your functions are implemented:

1. Identify where your application should call them.
2. Pass the appropriate arguments.
3. Store and use their return values.
4. Run your existing ParkPulse application.
5. Confirm Week 1 functionality still works.
6. Test normal, boundary, and invalid inputs.

Do not add interactive menus or loop-based features yet. Those are part of Week 3.

---

## 5. AI Edge-Case Activity

Use AI to suggest additional inputs that might reveal problems in your code.

Example prompt:

"Suggest five unusual or boundary-case inputs that could test a Python ride eligibility function. Do not write the function or provide implementation code."

For each input:

1. Predict the expected behavior.
2. Run your function.
3. Compare your prediction with the actual behavior.
4. Explain unexpected results.
5. Decide whether the AI suggestion was useful.

**AI can suggest test cases, but you are responsible for the expected behavior and implementation.**

---

## 6. Interview Connection

Imagine an interviewer asks:

**"Why did you refactor that ParkPulse logic into a function?"**

Prepare a 60–90-second explanation using:

- **Point:** What did you change?
- **Reason:** Why does that structure help?
- **Evidence:** Which function, input, and observed result support your decision?
- **Final Point:** What is the takeaway?

Be prepared to explain how you verified an edge case.

---

## 7. Week 2 Completion Checklist

- [ ] My completed Week 1 application is already on `main`.
- [ ] I fetched the instructor's `Week_2` starter.
- [ ] I preserved my Week 1 application code.
- [ ] I completed the required Functions reading activity.
- [ ] I practiced function calls, scope, and conditional statements.
- [ ] I refactored ParkPulse into reusable functions.
- [ ] I completed ride eligibility, ticket pricing, and capacity rules.
- [ ] I added appropriate guard clauses.
- [ ] Week 1 functionality still works.
- [ ] I tested normal and edge-case inputs.
- [ ] I can explain one design decision using evidence.

---

## 8. Commit and Push Week 2

Confirm your branch:

```bash
git branch --show-current
git status
```

Commit your completed work:

```bash
git add src/parkpulse.py practice/ README.md
git commit -m "Complete Week 2 ParkPulse functions"
git push origin Week_2
```

Your completed work is now saved on your personal repository's `Week_2` branch.

### Integrate Your Completed Application Into Main

**Do not merge the Week 2 README or `practice/` files into `main`.**

Those are instructional materials for `Week_2` only.

Once your Week 2 application is complete and approved, transfer only the finished Python application file:

```bash
git switch main
git pull --ff-only origin main
git restore --source Week_2 -- src/parkpulse.py
git add src/parkpulse.py
git commit -m "Integrate Week 2 ParkPulse features"
git push origin main
```

Your `main` branch should contain the cumulative working application, existing project documentation, and configuration files—not the weekly instructional README or practice exercises.

---

## Optional Practice

- Complete the Conditional Statements interactive reading.
- Trace additional functions involving default arguments, keyword arguments, and scope.
- Test additional edge cases.
- Complete any remaining Week 2 function work.

**Next week:** Loops, strings, and interactive input.