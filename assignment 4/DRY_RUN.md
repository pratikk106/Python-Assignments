# Assignment 4 – Dry Runs and Visual Walkthroughs

A **dry run** means executing a program by hand, line by line, and writing down the value of each variable after every step. For loop programs, the most useful dry run is an **iteration table**: one row per pass through the loop, showing how the counters and totals change.

Every program below has:

1. A **flowchart** showing the loop and its exit conditions.
2. An **iteration table** following the sample input from [OUTPUTS.md](OUTPUTS.md).
3. A **chart or diagram** visualising the data the loop processed.

> The flowcharts and charts use [Mermaid](https://mermaid.js.org/). They render as diagrams on GitHub and in Cursor / VS Code's Markdown preview.

---

## Q1 – Daily Expense Tracker ([`q1.py`](q1.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read days"/]
    B --> I["total = 0, highest = 0, i = 1"]
    I --> L{"i <= days ?"}
    L -- Yes --> R[/"Read expense"/]
    R --> T["total = total + expense"]
    T --> H{"i == 1 OR expense > highest ?"}
    H -- Yes --> H1["highest = expense"]
    H -- No --> N
    H1 --> N["i = i + 1"]
    N --> L
    L -- No --> AV["average = total / days"]
    AV --> P[/"Print total, average, highest"/]
    P --> BA{"total > 5000 ?"}
    BA -- Yes --> BA1[/"Budget Alert"/]
    BA -- No --> BA2[/"Within Budget"/]
    BA1 --> Z([End])
    BA2 --> Z
```

### Iteration Table (5 days)

| `i` | `expense` | `total` (after) | `expense > highest` ? | `highest` (after) |
|-----|-----------|-----------------|-----------------------|-------------------|
| 1 | 800 | 800 | first day | 800 |
| 2 | 1200 | 2000 | 1200 > 800 ✔ | 1200 |
| 3 | 950 | 2950 | 950 > 1200 ✘ | 1200 |
| 4 | 1500 | 4450 | 1500 > 1200 ✔ | 1500 |
| 5 | 1100 | 5550 | 1100 > 1500 ✘ | 1500 |

After the loop: `average = 5550 / 5 = 1110.0`; `5550 > 5000` → **Budget Alert**.

### Daily Expenses

```mermaid
xychart-beta
    title "Daily expense (Rs.)"
    x-axis ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
    y-axis "Expense (Rs.)" 0 --> 1600
    bar [800, 1200, 950, 1500, 1100]
    line [1110, 1110, 1110, 1110, 1110]
```

The bars are the daily expenses and the flat line is the average (₹1110).

### Running Total vs Budget

```mermaid
xychart-beta
    title "Running total vs Rs. 5000 budget"
    x-axis ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
    y-axis "Total (Rs.)" 0 --> 6000
    line [800, 2000, 2950, 4450, 5550]
    line [5000, 5000, 5000, 5000, 5000]
```

The running total crosses the ₹5000 budget line on day 5, which triggers the alert.

---

## Q2 – Class Grade Calculator ([`q2.py`](q2.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read students"/]
    B --> I["total = 0, pass = 0, fail = 0"]
    I --> L{"more students ?"}
    L -- Yes --> R[/"Read name, marks"/]
    R --> V{"marks < 0 OR marks > 100 ?"}
    V -- Yes --> V1[/"Invalid marks!"/]
    V1 -- continue --> L
    V -- No --> T["total = total + marks"]
    T --> G{"marks ?"}
    G -->|">= 75"| GA["A"]
    G -->|">= 60"| GB["B"]
    G -->|">= 50"| GC["C"]
    G -->|">= 40"| GD["D"]
    G -->|"< 40"| GF["Fail"]
    GA --> PF
    GB --> PF
    GC --> PF
    GD --> PF
    GF --> PF{"marks >= 40 ?"}
    PF -- Yes --> P1["pass += 1"]
    PF -- No --> F1["fail += 1"]
    P1 --> L
    F1 --> L
    L -- No --> C{"valid students > 0 ?"}
    C -- Yes --> C1[/"Print average, pass, fail"/]
    C -- No --> C2[/"No valid marks"/]
    C1 --> Z([End])
    C2 --> Z
```

### Iteration Table (4 students)

| Iteration | Name | Marks | Valid? | Grade | `total` | `pass_count` | `fail_count` |
|-----------|------|-------|--------|-------|---------|--------------|--------------|
| 1 | Aman | 82 | ✔ | A | 82 | 1 | 0 |
| 2 | Bela | 65 | ✔ | B | 147 | 2 | 0 |
| 3 | Chirag | 35 | ✔ | Fail | 182 | 2 | 1 |
| 4 | Dev | 120 | ✘ → `continue` | – | 182 | 2 | 1 |

After the loop: `valid_students = 2 + 1 = 3`, `average = 182 / 3 = 60.67`.

### Grade Bands

```text
Marks:  0 ────────── 40 ──── 50 ──── 60 ──────── 75 ────────── 100
Grade:      Fail      │  D   │  C   │     B      │      A
                      ▲                          ▲
                   Chirag (35)        Bela (65)  │   Aman (82)
```

### Pass / Fail Split

```mermaid
pie showData title Result of valid students
    "Pass" : 2
    "Fail" : 1
```

---

## Q3 – ATM PIN Verification ([`q3.py`](q3.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> I["correct_pin = '1234', attempts = 0"]
    I --> L{"attempts < 3 ?"}
    L -- Yes --> R[/"Read pin"/]
    R --> INC["attempts = attempts + 1"]
    INC --> C{"pin == correct_pin ?"}
    C -- Yes --> G[/"Access Granted"/]
    G -- break --> E
    C -- No --> W[/"Incorrect PIN"/]
    W --> L
    L -- No --> E{"attempts == 3 AND pin wrong ?"}
    E -- Yes --> LK[/"Card Temporarily Locked"/]
    E -- No --> P
    LK --> P[/"Print attempts used"/]
    P --> Z([End])
```

### Iteration Tables

**Run 1 – PINs `1111`, `1234`**

| Pass | `pin` | `attempts` | `pin == "1234"` | Action |
|------|-------|------------|-----------------|--------|
| 1 | 1111 | 1 | False | Incorrect PIN |
| 2 | 1234 | 2 | **True** | Access Granted → `break` |

Lock check: `attempts == 3` is False → no lock. Output: *Attempts Used: 2*.

**Run 2 – PINs `0000`, `1111`, `2222`**

| Pass | `pin` | `attempts` | `pin == "1234"` | Action |
|------|-------|------------|-----------------|--------|
| 1 | 0000 | 1 | False | Incorrect PIN |
| 2 | 1111 | 2 | False | Incorrect PIN |
| 3 | 2222 | 3 | False | Incorrect PIN |
| – | – | 3 | `attempts < 3` is False | loop ends |

Lock check: `attempts == 3 and pin != "1234"` is True → **Card Temporarily Locked**.

---

## Q4 – Shopping Cart ([`q4.py`](q4.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read products"/]
    B --> I["subtotal = 0"]
    I --> L{"more products ?"}
    L -- Yes --> R[/"Read price, quantity"/]
    R --> V{"price < 0 OR quantity < 0 ?"}
    V -- Yes --> V1[/"Invalid!"/]
    V1 -- continue --> L
    V -- No --> T["item_total = price x quantity<br/>subtotal += item_total"]
    T --> L
    L -- No --> D{"subtotal >= 3000 ?"}
    D -- Yes --> D1["discount = 10%"]
    D -- No --> D2["discount = 0"]
    D1 --> AM["amount = subtotal - discount"]
    D2 --> AM
    AM --> DL{"amount < 1500 ?"}
    DL -- Yes --> DL1["delivery = 100"]
    DL -- No --> DL2["delivery = 0"]
    DL1 --> F[/"Print final = amount + delivery"/]
    DL2 --> F
    F --> Z([End])
```

### Iteration Table (3 products)

| Product | `price` | `quantity` | `item_total` | `subtotal` (after) |
|---------|---------|------------|--------------|--------------------|
| 1 | 500 | 2 | 1000.0 | 1000.0 |
| 2 | 1200 | 1 | 1200.0 | 2200.0 |
| 3 | 250 | 4 | 1000.0 | 3200.0 |

After the loop:

| Step | Check | Result |
|------|-------|--------|
| Discount | `3200 >= 3000` → True | 3200 × 10 / 100 = **320.0** |
| Amount | 3200 − 320 | **2880.0** |
| Delivery | `2880 < 1500` → False | **0** |
| Final | 2880 + 0 | **2880.0** |

### Cart Composition

```mermaid
pie showData title Cart subtotal Rs. 3200
    "Product 1 (500 x 2)" : 1000
    "Product 2 (1200 x 1)" : 1200
    "Product 3 (250 x 4)" : 1000
```

---

## Q5 – Number Guessing Game ([`q5.py`](q5.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> I["secret = 37, attempts = 0"]
    I --> L{"attempts < 5 ?"}
    L -- Yes --> R[/"Read guess"/]
    R --> INC["attempts += 1"]
    INC --> C{"guess == secret ?"}
    C -- Yes --> W[/"You Win!"/]
    W -- break --> E
    C -- No --> LO{"guess < secret ?"}
    LO -- Yes --> LO1[/"Too low"/]
    LO -- No --> HI1[/"Too high"/]
    LO1 --> L
    HI1 --> L
    L -- No --> E{"guess != secret ?"}
    E -- Yes --> LS[/"You Lose!"/]
    E -- No --> P
    LS --> P[/"Print attempts used"/]
    P --> Z([End])
```

### Iteration Table – Run 1 (win)

| Pass | `guess` | `attempts` | Comparison with 37 | Output |
|------|---------|------------|--------------------|--------|
| 1 | 50 | 1 | 50 > 37 | Too high |
| 2 | 20 | 2 | 20 < 37 | Too low |
| 3 | 37 | 3 | equal | You Win! → `break` |

### How the Hints Narrow the Range

```text
Guess 1 = 50 → "Too high"   possible range: 1 ─────────────── 49
Guess 2 = 20 → "Too low"    possible range:        21 ─────── 49
Guess 3 = 37 → "You Win!"                              ▲ 37
```

### Iteration Table – Run 2 (lose)

| Pass | `guess` | `attempts` | Hint |
|------|---------|------------|------|
| 1 | 10 | 1 | Too low |
| 2 | 20 | 2 | Too low |
| 3 | 30 | 3 | Too low |
| 4 | 40 | 4 | Too high |
| 5 | 50 | 5 | Too high |

The loop ends because `attempts < 5` is False, and `50 != 37` prints **You Lose! The secret number was 37**.

```mermaid
xychart-beta
    title "Run 2 guesses vs secret number 37"
    x-axis ["Guess 1", "Guess 2", "Guess 3", "Guess 4", "Guess 5"]
    y-axis "Value" 0 --> 60
    bar [10, 20, 30, 40, 50]
    line [37, 37, 37, 37, 37]
```

---

## Q6 – Electricity Usage Analyser ([`q6.py`](q6.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read days"/]
    B --> I["total = 0, high_count = 0, maximum = 0"]
    I --> L{"more days ?"}
    L -- Yes --> R[/"Read units"/]
    R --> T["total += units"]
    T --> H{"units > 10 ?"}
    H -- Yes --> H1["high_count += 1"]
    H -- No --> M
    H1 --> M{"first day OR units > maximum ?"}
    M -- Yes --> M1["maximum = units"]
    M -- No --> L
    M1 --> L
    L -- No --> AV["average = total / days"]
    AV --> P[/"Print summary"/]
    P --> S{"total > 300 ?"}
    S -- Yes --> S1[/"High Usage"/]
    S -- No --> S2[/"Normal Usage"/]
    S1 --> Z([End])
    S2 --> Z
```

### Iteration Table (7 days)

| Day | `units` | `total` | `units > 10` ? | `high_count` | `maximum` |
|-----|---------|---------|----------------|--------------|-----------|
| 1 | 8 | 8 | ✘ | 0 | 8 |
| 2 | 12 | 20 | ✔ | 1 | 12 |
| 3 | 9 | 29 | ✘ | 1 | 12 |
| 4 | 15 | 44 | ✔ | 2 | 15 |
| 5 | 10 | 54 | ✘ (10 is not > 10) | 2 | 15 |
| 6 | 11 | 65 | ✔ | 3 | 15 |
| 7 | 7 | 72 | ✘ | 3 | 15 |

After the loop: `average = 72 / 7 ≈ 10.29`; `72 > 300` is False → **Normal Usage**.

### Daily Usage vs High-Usage Threshold

```mermaid
xychart-beta
    title "Units consumed per day"
    x-axis ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    y-axis "Units" 0 --> 16
    bar [8, 12, 9, 15, 10, 11, 7]
    line [10, 10, 10, 10, 10, 10, 10]
```

Bars above the line at 10 units (days 2, 4 and 6) are the three high-usage days.

---

## Q7 – Employee Payroll ([`q7.py`](q7.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read employees"/]
    B --> I["total_payroll = 0"]
    I --> L{"more employees ?"}
    L -- Yes --> R[/"Read name, basic, overtime_hours"/]
    R --> O["overtime_pay = hours x 200<br/>gross = basic + overtime_pay"]
    O --> D{"gross >= 50000 ?"}
    D -- Yes --> D1["deduction = 10%"]
    D -- No --> D2["deduction = 5%"]
    D1 --> N["net = gross - deduction<br/>total_payroll += net"]
    D2 --> N
    N --> P1[/"Print employee details"/]
    P1 --> L
    L -- No --> P2[/"Print total payroll, count"/]
    P2 --> Z([End])
```

### Iteration Table (2 employees)

| Employee | `basic_salary` | OT hours | `overtime_pay` | `gross_salary` | Rate | `deduction` | `net_salary` | `total_payroll` |
|----------|----------------|----------|----------------|----------------|------|-------------|--------------|-----------------|
| Asha | 45000 | 10 | 2000 | 47000 | 5% | 2350 | 44650 | 44650 |
| Bharat | 52000 | 5 | 1000 | 53000 | 10% | 5300 | 47700 | **92350** |

### Gross vs Net Salary

```mermaid
xychart-beta
    title "Gross vs net salary (Rs.)"
    x-axis ["Asha gross", "Asha net", "Bharat gross", "Bharat net"]
    y-axis "Amount (Rs.)" 0 --> 60000
    bar [47000, 44650, 53000, 47700]
```

Bharat's gross crosses ₹50,000, so he moves into the 10% deduction bracket.

---

## Q8 – Quiz ([`q8.py`](q8.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> I["questions list, answers list, score = 0"]
    I --> L{"i in 0..5 ?"}
    L -- Yes --> R[/"Ask questions[i], read answer (lowercased)"/]
    R --> C{"answer == answers[i] ?"}
    C -- Yes --> C1[/"Correct! score += 1"/]
    C -- No --> C2[/"Wrong!"/]
    C1 --> L
    C2 --> L
    L -- No --> P["percentage = score / 6 x 100"]
    P --> G{"percentage ?"}
    G -->|">= 80"| G1[/"Excellent"/]
    G -->|">= 60"| G2[/"Good"/]
    G -->|"< 60"| G3[/"Keep Practicing"/]
    G1 --> Z([End])
    G2 --> Z
    G3 --> Z
```

### Iteration Table

| `i` | User answer (lowercased) | `answers[i]` | Match? | `score` |
|-----|--------------------------|--------------|--------|---------|
| 0 | delhi | delhi | ✔ | 1 |
| 1 | 7 | 7 | ✔ | 2 |
| 2 | css | css | ✔ | 3 |
| 3 | 12 | 10 | ✘ | 3 |
| 4 | mars | mars | ✔ | 4 |
| 5 | atlantic | pacific | ✘ | 4 |

After the loop: `percentage = 4 / 6 × 100 = 66.67`; `66.67 >= 80` False, `66.67 >= 60` True → **Good**.

### How the Two Lists Line Up

```text
index:      0         1      2        3      4        5
questions:  capital   week   styling  5+5    red      ocean
answers:    "delhi"   "7"    "css"    "10"   "mars"   "pacific"
user:       "delhi"   "7"    "css"    "12"   "mars"   "atlantic"
result:       ✔        ✔      ✔        ✘      ✔        ✘
```

```mermaid
pie showData title Quiz result (4 out of 6)
    "Correct" : 4
    "Wrong" : 2
```

---

## Q9 – Bank Transaction Simulator ([`q9.py`](q9.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read opening balance, transactions"/]
    B --> I["deposit_count = 0, success = 0, rejected = 0"]
    I --> L{"more transactions ?"}
    L -- Yes --> R[/"Read type, amount"/]
    R --> V{"amount <= 0 ?"}
    V -- Yes --> V1[/"Invalid amount!"/]
    V -- No --> T{"type ?"}
    T -- deposit --> DP["balance += amount<br/>deposit_count += 1"]
    T -- withdraw --> W{"amount <= balance ?"}
    T -- other --> X[/"Invalid transaction type!"/]
    W -- Yes --> WS["balance -= amount<br/>success += 1"]
    W -- No --> WR["rejected += 1"]
    V1 --> L
    DP --> L
    WS --> L
    WR --> L
    X --> L
    L -- No --> P[/"Print balance and counters"/]
    P --> LB{"balance < 1000 ?"}
    LB -- Yes --> LB1[/"Warning: Low Balance"/]
    LB -- No --> Z([End])
    LB1 --> Z
```

### Iteration Table (opening balance ₹5000)

| Txn | Type | Amount | Check | `balance` (after) | Deposits | Successful W | Rejected W |
|-----|------|--------|-------|-------------------|----------|--------------|------------|
| – | opening | – | – | 5000 | 0 | 0 | 0 |
| 1 | deposit | 2000 | – | 7000 | 1 | 0 | 0 |
| 2 | withdraw | 3000 | 3000 ≤ 7000 ✔ | 4000 | 1 | 1 | 0 |
| 3 | withdraw | 6000 | 6000 ≤ 4000 ✘ | 4000 | 1 | 1 | 1 |
| 4 | withdraw | 3500 | 3500 ≤ 4000 ✔ | 500 | 1 | 2 | 1 |

After the loop: `500 < 1000` → **Warning: Low Balance**.

### Balance Over Time

```mermaid
xychart-beta
    title "Account balance after each transaction (Rs.)"
    x-axis ["Opening", "Txn 1", "Txn 2", "Txn 3", "Txn 4"]
    y-axis "Balance (Rs.)" 0 --> 8000
    line [5000, 7000, 4000, 4000, 500]
    line [1000, 1000, 1000, 1000, 1000]
```

The flat line at ₹1000 is the low-balance threshold. The balance stays level at transaction 3 because that withdrawal was rejected.

---

## Q10 – Multiplication Table and Range Analysis ([`q10.py`](q10.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read number"/]
    B --> C{"number <= 0 ?"}
    C -- Yes --> C1[/"Please enter a positive integer"/]
    C -- No --> T{"i in 1..10 ?"}
    T -- Yes --> T1[/"Print number x i"/]
    T1 --> T
    T -- No --> R
    C1 --> R[/"Read start, end"/]
    R --> V{"start > end ?"}
    V -- Yes --> V1[/"Invalid range!"/]
    V -- No --> I["even = 0, odd = 0, total = 0"]
    I --> L{"i in start..end ?"}
    L -- Yes --> S["total += i"]
    S --> E{"i % 2 == 0 ?"}
    E -- Yes --> E1["even += 1"]
    E -- No --> O1["odd += 1"]
    E1 --> L
    O1 --> L
    L -- No --> P[/"Print even, odd, sum"/]
    P --> Z([End])
    V1 --> Z
```

### Part 1 – Multiplication Table of 7

| `i` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-----|---|---|---|---|---|---|---|---|---|----|
| `7 × i` | 7 | 14 | 21 | 28 | 35 | 42 | 49 | 56 | 63 | 70 |

### Part 2 – Range 1 to 10

| `i` | `i % 2` | Even / Odd | `even_count` | `odd_count` | `total` |
|-----|---------|------------|--------------|-------------|---------|
| 1 | 1 | Odd | 0 | 1 | 1 |
| 2 | 0 | Even | 1 | 1 | 3 |
| 3 | 1 | Odd | 1 | 2 | 6 |
| 4 | 0 | Even | 2 | 2 | 10 |
| 5 | 1 | Odd | 2 | 3 | 15 |
| 6 | 0 | Even | 3 | 3 | 21 |
| 7 | 1 | Odd | 3 | 4 | 28 |
| 8 | 0 | Even | 4 | 4 | 36 |
| 9 | 1 | Odd | 4 | 5 | 45 |
| 10 | 0 | Even | 5 | 5 | **55** |

`range(start, end + 1)` is used because Python's `range()` stops **before** its second argument; without the `+ 1`, the number 10 would be skipped.

```mermaid
xychart-beta
    title "Running sum of the range 1 to 10"
    x-axis [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y-axis "Sum" 0 --> 60
    line [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
```
