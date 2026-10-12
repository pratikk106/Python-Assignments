# Assignment 4 – Loops (`for`, `while`, `break`, `continue`)

This assignment uses loops to process repeated input: daily records, lists of students, products and employees, quiz questions, bank transactions and number ranges. The programs keep running totals, counters and maximums, and use `break` and `continue` to control the loop.

## Programs

| File | Problem | Key Concept |
|------|---------|-------------|
| [`q1.py`](q1.py) | Daily expense tracker with budget alert | `for` loop, running total, running maximum |
| [`q2.py`](q2.py) | Class grade calculator with pass/fail count | `for` loop, `continue` to skip invalid marks |
| [`q3.py`](q3.py) | ATM PIN verification with 3 attempts | `while` loop, `break` |
| [`q4.py`](q4.py) | Shopping cart with discount and delivery charge | `for` loop, `continue`, accumulators |
| [`q5.py`](q5.py) | Number guessing game with 5 attempts | `while` loop, `break`, high/low hints |
| [`q6.py`](q6.py) | Electricity usage analyser | Counting with conditions inside a loop |
| [`q7.py`](q7.py) | Employee payroll with overtime and deductions | Per-iteration calculation, total payroll |
| [`q8.py`](q8.py) | Six-question quiz with score and remark | Lists, indexing with `range()` |
| [`q9.py`](q9.py) | Bank account transaction simulator | Loop with multi-way branching |
| [`q10.py`](q10.py) | Multiplication table and even/odd count in a range | `range(start, end + 1)` |

## Business Rules at a Glance

| Program | Rules |
|---------|-------|
| Expense tracker | Prints total, average and highest expense; *Budget Alert* if total > ₹5000 |
| Grade calculator | A ≥ 75, B ≥ 60, C ≥ 50, D ≥ 40, otherwise Fail; marks outside 0–100 are skipped |
| PIN check | Correct PIN is `1234`; card locks after 3 wrong attempts |
| Shopping cart | 10% discount when subtotal ≥ ₹3000; ₹100 delivery when amount after discount < ₹1500 |
| Guessing game | Secret number is `37`; 5 attempts with *Too low* / *Too high* hints |
| Electricity usage | A day with more than 10 units counts as high usage; total > 300 units is *High Usage* |
| Payroll | Overtime ₹200/hour; 10% deduction when gross ≥ ₹50,000, otherwise 5% |
| Quiz | ≥ 80% *Excellent*, ≥ 60% *Good*, otherwise *Keep Practicing* |
| Bank simulator | Withdrawals larger than the balance are rejected; warns if final balance < ₹1000 |
| Table and range | Prints the 1–10 table, then even count, odd count and sum of the range |

## How to Run

Open a terminal inside this folder and run any program:

```bash
python q1.py
```

Then type each value the program asks for and press **Enter**.

## Notes

- **`q1.py`** and **`q6.py`** divide by the number of days to get the average, so entering `0` days raises a `ZeroDivisionError`.
- **`q2.py`** and **`q4.py`** use `continue` for invalid entries, so an invalid entry still uses up one of the loop's iterations instead of asking again.
- **`q3.py`** and **`q5.py`** have their PIN (`1234`) and secret number (`37`) hard-coded in the source.
- **`q5.py`** converts the guess with `int()`, so a non-numeric guess stops the program with a `ValueError`.

## More Documentation

- [OUTPUTS.md](OUTPUTS.md) – sample runs and the output of every program
- [DRY_RUN.md](DRY_RUN.md) – iteration-by-iteration dry runs, flowcharts and charts showing how each program works
