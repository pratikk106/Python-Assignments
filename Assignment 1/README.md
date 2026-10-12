# Assignment 1 – Basic Conditional Statements (`if` / `else`)

This assignment introduces decision making in Python. Each program reads a single value from the user, tests it with one `if` / `else` condition, and prints the result.

## Programs

| File | Problem | Key Concept |
|------|---------|-------------|
| [`q1.py`](q1.py) | Check whether a number is positive or negative | Comparison `>` |
| [`q2.py`](q2.py) | Check whether a number is odd or even | Modulus operator `%` |
| [`q3.py`](q3.py) | Check whether a person is eligible to vote | Comparison `>=` |
| [`q4.py`](q4.py) | Check whether a number is greater than 100 | Comparison `>` |
| [`q5.py`](q5.py) | Check whether a year is a leap year | Compound condition with `and` / `or` |

## Concepts Covered

- Taking input with `input()` and converting it with `int()`
- Relational operators: `>`, `>=`, `==`, `!=`
- Arithmetic operator `%` (remainder)
- Logical operators `and`, `or`
- Two-way branching with `if` / `else`

## How to Run

Open a terminal inside this folder and run any program:

```bash
python q1.py
```

Then type the value the program asks for and press **Enter**.

## Notes

- **`q1.py`** – the `else` branch catches every value that is not greater than 0, so an input of `0` is reported as *negative*.
- **`q5.py`** – a year is a leap year when it is divisible by 4 but not by 100, **or** when it is divisible by 400. Because `and` binds tighter than `or`, the condition `year % 4 == 0 and year % 100 != 0 or year % 400 == 0` is evaluated as `(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`.

## More Documentation

- [OUTPUTS.md](OUTPUTS.md) – sample runs and the output of every program
- [DRY_RUN.md](DRY_RUN.md) – dry-run trace tables and flowcharts showing how each program works
