# Assignment 2 – Real-World Decision Making (`if` / `elif` / `else` and Nested Conditions)

This assignment applies conditional logic to everyday billing and eligibility problems. The programs use `if`–`elif`–`else` ladders, nested `if` blocks, logical operators and input validation to calculate bills, discounts, bonuses and premiums.

## Programs

| File | Problem | Key Concept |
|------|---------|-------------|
| [`q1.py`](q1.py) | Electricity bill with slab-wise unit rates | `if`–`elif` ladder, slab calculation |
| [`q2.py`](q2.py) | Online shopping checkout with discounts and premium benefit | Ranges with `and`, nested `if` |
| [`q3.py`](q3.py) | ATM withdrawal with balance and limit checks | Three-level nested `if` |
| [`q4.py`](q4.py) | Student scholarship eligibility | Combined conditions with `and`, multiple independent `if`s |
| [`q5.py`](q5.py) | Employee performance bonus | Input validation, `elif` with `and` |
| [`q6.py`](q6.py) | Hotel room booking with long-stay discount | String matching, nested ladders |
| [`q7.py`](q7.py) | Mobile data plan bill with surcharge | Plan lookup, conditional surcharge |
| [`q8.py`](q8.py) | Movie ticket pricing by age, show and day | `not in` validation, stacked adjustments |
| [`q9.py`](q9.py) | Insurance premium based on risk factors | Accumulating charges |
| [`q10.py`](q10.py) | Restaurant bill with membership discount and service charge | Percentage chains |

## Business Rules at a Glance

| Program | Rules |
|---------|-------|
| Electricity bill | 0–100 units @ ₹3, 101–200 @ ₹4, 201–300 @ ₹5, above 300 @ ₹6, plus ₹50 service charge |
| Shopping checkout | ≥ ₹5000 → 20%, ≥ ₹3000 → 10%, ≥ ₹1000 → 5% off; Premium gets +5%; delivery ₹100 if final amount < ₹2000 |
| ATM | Amount must be > 0, ≤ balance and ≤ ₹20,000; warns if remaining balance < ₹1000 |
| Scholarship | Needs percentage ≥ 75, income ≤ ₹4,00,000, attendance ≥ 75; percentage ≥ 90 gets full scholarship |
| Bonus | 10+ yrs & rating ≥ 4 → 20%, 5+ yrs & rating ≥ 4 → 15%, 2+ yrs & rating ≥ 3 → 10%, else 0% |
| Hotel | Standard ₹2000, Deluxe ₹3500, Suite ₹6000 per night; 5+ nights → 10% off, 10+ nights → 20% off |
| Mobile plan | Basic ₹299, Standard ₹499, Premium ₹799; extra data ₹20/GB; ₹100 surcharge above 10 GB |
| Movie ticket | Base ₹200; child (< 12) 50% off, senior (≥ 60) 30% off; morning show extra ₹30 off; weekend +₹50 |
| Insurance | Base ₹10,000; age > 50 +₹5000; High risk +₹7000, Medium +₹3000; smoker +₹5000; age < 18 not eligible |
| Restaurant | < ₹1000 → 0%, < ₹3000 → 5%, < ₹5000 → 10%, else 15%; members +5%; 5% service charge on discounted amount |

## How to Run

Open a terminal inside this folder and run any program:

```bash
python q1.py
```

Then type each value the program asks for and press **Enter**.

## Notes

- Text inputs such as room type, plan type, show type and Yes/No answers are converted with `.lower()`, so they are case-insensitive.
- **`q2.py`** – the inner checks `if purchase_amount > 0` and `if final_amount < 2000` are always true where they sit, so they do not change the result; they only make the nesting explicit.
- **`q8.py`** – the morning-show benefit is a flat ₹30 added on top of any age-based discount.
- **`q9.py`** – all four inputs are collected before the age check, so an under-18 customer still answers every question before seeing *Not Eligible*.

## More Documentation

- [OUTPUTS.md](OUTPUTS.md) – sample runs and the output of every program
- [DRY_RUN.md](DRY_RUN.md) – dry-run trace tables, flowcharts and charts showing how each program works
