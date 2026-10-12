# Assignment 2 – Dry Runs and Visual Walkthroughs

A **dry run** means executing a program by hand, line by line, and writing down the value of each variable and the result of each condition. Every program below has:

1. A **flowchart** showing every path the program can take.
2. A **trace table** following the sample input from [OUTPUTS.md](OUTPUTS.md).
3. A **chart or diagram** showing how the final amount is built up.

> The flowcharts and charts use [Mermaid](https://mermaid.js.org/). They render as diagrams on GitHub and in Cursor / VS Code's Markdown preview.

---

## Q1 – Electricity Bill ([`q1.py`](q1.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read customer_name, units"/]
    B --> C{"units <= 100 ?"}
    C -- Yes --> C1["energy = units x 3"]
    C -- No --> D{"units <= 200 ?"}
    D -- Yes --> D1["energy = 300 + (units - 100) x 4"]
    D -- No --> E{"units <= 300 ?"}
    E -- Yes --> E1["energy = 300 + 400 + (units - 200) x 5"]
    E -- No --> E2["energy = 300 + 400 + 500 + (units - 300) x 6"]
    C1 --> F["service_charge = 50<br/>final_bill = energy + 50"]
    D1 --> F
    E1 --> F
    E2 --> F
    F --> G{"units <= 100 ?"}
    G -- Yes --> G1["Low usage"]
    G -- No --> H{"units <= 200 ?"}
    H -- Yes --> H1["Moderate usage"]
    H -- No --> H2["High usage"]
    G1 --> P[/"Print bill"/]
    H1 --> P
    H2 --> P
    P --> Z([End])
```

### Trace Table – Ravi, 250 units

| Step | Statement / Condition | Result | `energy_charge` | `final_bill` | `usage_message` |
|------|-----------------------|--------|-----------------|--------------|-----------------|
| 1 | `units = 250` | – | – | – | – |
| 2 | `units <= 100` | False | – | – | – |
| 3 | `units <= 200` | False | – | – | – |
| 4 | `units <= 300` | **True** | 300 + 400 + 50 × 5 = **950** | – | – |
| 5 | `final_bill = 950 + 50` | – | 950 | **1000** | – |
| 6 | `units <= 100` / `units <= 200` | False / False | 950 | 1000 | **High electricity usage** |

### Slab Breakdown

```text
Units:   1 ──────── 100 ──────── 200 ──── 250
Rate:      ₹3/unit      ₹4/unit    ₹5/unit
Cost:      100×3=300    100×4=400  50×5=250   → Energy = 950
```

```mermaid
pie showData title Ravi's bill (Rs. 1000)
    "Slab 1: 100 units x Rs.3" : 300
    "Slab 2: 100 units x Rs.4" : 400
    "Slab 3: 50 units x Rs.5" : 250
    "Service charge" : 50
```

---

## Q2 – Shopping Checkout ([`q2.py`](q2.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read name, purchase_amount, customer_type"/]
    B --> C{"amount >= 5000 ?"}
    C -- Yes --> C1["rate = 20"]
    C -- No --> D{"3000 <= amount < 5000 ?"}
    D -- Yes --> D1["rate = 10"]
    D -- No --> E{"1000 <= amount < 3000 ?"}
    E -- Yes --> E1["rate = 5"]
    E -- No --> E2["rate = 0"]
    C1 --> F{"type is premium ?"}
    D1 --> F
    E1 --> F
    E2 --> F
    F -- Yes --> F1["rate = rate + 5"]
    F -- No --> G
    F1 --> G["discount = amount x rate / 100<br/>final = amount - discount"]
    G --> H{"final >= 2000 ?"}
    H -- Yes --> H1["delivery = 0"]
    H -- No --> H2["delivery = 100"]
    H1 --> P[/"Print discount, delivery, final + delivery"/]
    H2 --> P
    P --> Z([End])
```

### Trace Table

| Variable / Check | Priya (5500, Premium) | Amit (1500, Regular) |
|------------------|-----------------------|----------------------|
| `amount >= 5000` | True → rate 20 | False |
| `3000 <= amount < 5000` | – | False |
| `1000 <= amount < 3000` | – | True → rate 5 |
| Premium? | Yes → rate **25** | No → rate **5** |
| `discount_amount` | 5500 × 25 / 100 = **1375.0** | 1500 × 5 / 100 = **75.0** |
| `final_amount` | 4125.0 | 1425.0 |
| `final_amount >= 2000` | True → delivery **0** | False → delivery **100** |
| `final_payable` | **4125.0** | **1525.0** |

### Where Priya's ₹5500 Goes

```mermaid
pie showData title Priya - purchase of Rs. 5500
    "Amount paid" : 4125
    "Discount (25%)" : 1375
```

---

## Q3 – ATM Transaction ([`q3.py`](q3.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read name, balance, withdrawal"/]
    B --> C{"withdrawal > 0 ?"}
    C -- No --> R1[/"Rejected: amount must be > 0"/]
    C -- Yes --> D{"withdrawal <= balance ?"}
    D -- No --> R2[/"Rejected: Insufficient balance"/]
    D -- Yes --> E{"withdrawal <= 20000 ?"}
    E -- No --> R3[/"Rejected: max Rs.20,000"/]
    E -- Yes --> S["remaining = balance - withdrawal"]
    S --> S1[/"Print Successful + remaining"/]
    S1 --> W{"remaining < 1000 ?"}
    W -- Yes --> W1[/"Print Low Balance Warning"/]
    W -- No --> Z([End])
    W1 --> Z
    R1 --> Z
    R2 --> Z
    R3 --> Z
```

### Trace Table

| Check | Rahul (15000, 14500) | Sneha (5000, 8000) | Kiran (50000, 25000) |
|-------|----------------------|--------------------|----------------------|
| `withdrawal > 0` | True | True | True |
| `withdrawal <= balance` | True | **False** | True |
| `withdrawal <= 20000` | True | – | **False** |
| `remaining_balance` | 500.0 | – | – |
| `remaining < 1000` | True | – | – |
| Result | Successful + Low Balance Warning | Rejected – Insufficient balance | Rejected – limit ₹20,000 |

### Gate View

Each request must pass every gate in order; the first gate it fails decides the rejection reason.

```text
 request ──► [ > 0 ? ] ──► [ ≤ balance ? ] ──► [ ≤ 20000 ? ] ──► SUCCESS ──► [ remaining < 1000 ? ] ──► warning
                 │               │                  │
              reject          reject             reject
```

---

## Q4 – Scholarship Eligibility ([`q4.py`](q4.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read name, percentage, income, attendance"/]
    B --> C{"percentage >= 75 AND income <= 400000 AND attendance >= 75 ?"}
    C -- Yes --> D{"percentage >= 90 ?"}
    D -- Yes --> D1[/"Eligible - Full Scholarship"/]
    D -- No --> D2[/"Eligible - Partial Scholarship"/]
    C -- No --> N[/"Not Eligible - None"/]
    N --> R1{"percentage < 75 ?"}
    R1 -- Yes --> R1a[/"Reason: percentage"/]
    R1 -- No --> R2
    R1a --> R2{"income > 400000 ?"}
    R2 -- Yes --> R2a[/"Reason: income"/]
    R2 -- No --> R3
    R2a --> R3{"attendance < 75 ?"}
    R3 -- Yes --> R3a[/"Reason: attendance"/]
    R3 -- No --> Z([End])
    R3a --> Z
    D1 --> Z
    D2 --> Z
```

### Trace Table

| Check | Meera (92, 3,00,000, 85) | Arjun (70, 5,00,000, 60) |
|-------|--------------------------|--------------------------|
| `percentage >= 75` | True | False |
| `income <= 400000` | True | False |
| `attendance >= 75` | True | False |
| All three (`and`) | **True** | **False** |
| `percentage >= 90` | True → Full Scholarship | – |
| Reasons printed | – | Percentage, Income, Attendance |

Because the three reason checks are separate `if` statements (not `elif`), **every** failed criterion is reported, not just the first one.

---

## Q5 – Employee Bonus ([`q5.py`](q5.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read name, salary, experience, rating"/]
    B --> C{"rating < 1 OR rating > 5 ?"}
    C -- Yes --> X[/"Invalid rating!"/]
    C -- No --> D{"exp >= 10 AND rating >= 4 ?"}
    D -- Yes --> D1["bonus = 20%"]
    D -- No --> E{"exp >= 5 AND rating >= 4 ?"}
    E -- Yes --> E1["bonus = 15%"]
    E -- No --> F{"exp >= 2 AND rating >= 3 ?"}
    F -- Yes --> F1["bonus = 10%"]
    F -- No --> F2["bonus = 0%"]
    D1 --> G["bonus_amount = salary x bonus / 100<br/>final = salary + bonus_amount"]
    E1 --> G
    F1 --> G
    F2 --> G
    G --> H{"rating == 5 ?"}
    H -- Yes --> H1[/"Excellent Performer"/]
    H -- No --> H2[/"Keep Improving"/]
    X --> Z([End])
    H1 --> Z
    H2 --> Z
```

### Trace Table

| Check | Vikram (60000, 12 yrs, 5) | Neha (40000, 3 yrs, 3) | Karan (30000, 5 yrs, 7) |
|-------|---------------------------|------------------------|-------------------------|
| Rating invalid? | False | False | **True** → stop |
| `exp >= 10 and rating >= 4` | **True** → 20% | False | – |
| `exp >= 5 and rating >= 4` | – | False | – |
| `exp >= 2 and rating >= 3` | – | **True** → 10% | – |
| `bonus_amount` | 12000.0 | 4000.0 | – |
| `final_salary` | 72000.0 | 44000.0 | – |
| Message | Excellent Performer | Keep Improving | Invalid rating! |

### Bonus Matrix

| Experience ↓ / Rating → | 1–2 | 3 | 4–5 |
|-------------------------|-----|---|-----|
| 0–1 years | 0% | 0% | 0% |
| 2–4 years | 0% | 10% | 10% |
| 5–9 years | 0% | 10% | 15% |
| 10+ years | 0% | 10% | 20% |

---

## Q6 – Hotel Booking ([`q6.py`](q6.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read name, room_type, nights"/]
    B --> C{"nights <= 0 ?"}
    C -- Yes --> X1[/"Invalid number of nights!"/]
    C -- No --> D{"room_type ?"}
    D -- standard --> P1["price = 2000"]
    D -- deluxe --> P2["price = 3500"]
    D -- suite --> P3["price = 6000"]
    D -- other --> X2[/"Invalid room type!"/]
    P1 --> E["room_charge = price x nights"]
    P2 --> E
    P3 --> E
    E --> F{"nights >= 10 ?"}
    F -- Yes --> F1["discount = 20%"]
    F -- No --> G{"nights >= 5 ?"}
    G -- Yes --> G1["discount = 10%"]
    G -- No --> G2["discount = 0"]
    F1 --> H["final = room_charge - discount"]
    G1 --> H
    G2 --> H
    H --> P[/"Print booking"/]
    P --> Z([End])
    X1 --> Z
    X2 --> Z
```

### Trace Table

| Variable / Check | Rohan (Deluxe, 6) | Sara (Suite, 12) |
|------------------|-------------------|------------------|
| `price` | 3500 | 6000 |
| `room_charge` | 3500 × 6 = 21000 | 6000 × 12 = 72000 |
| `nights >= 10` | False | **True** → 20% |
| `nights >= 5` | **True** → 10% | – |
| `discount` | 2100.0 | 14400.0 |
| `final_amount` | **18900.0** | **57600.0** |

### Room Charge vs Final Amount

```mermaid
xychart-beta
    title "Hotel booking - before and after discount (Rs.)"
    x-axis ["Rohan charge", "Rohan final", "Sara charge", "Sara final"]
    y-axis "Amount (Rs.)" 0 --> 80000
    bar [21000, 18900, 72000, 57600]
```

---

## Q7 – Mobile Data Plan Bill ([`q7.py`](q7.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read name, plan, extra_data"/]
    B --> C{"extra_data < 0 ?"}
    C -- Yes --> X1[/"Invalid data usage!"/]
    C -- No --> D{"plan ?"}
    D -- basic --> P1["base = 299"]
    D -- standard --> P2["base = 499"]
    D -- premium --> P3["base = 799"]
    D -- other --> X2[/"Invalid plan type!"/]
    P1 --> E["extra_charge = extra_data x 20"]
    P2 --> E
    P3 --> E
    E --> F{"extra_data > 10 ?"}
    F -- Yes --> F1["surcharge = 100"]
    F -- No --> F2["surcharge = 0"]
    F1 --> G["final = base + extra_charge + surcharge"]
    F2 --> G
    G --> P[/"Print bill"/]
    P --> Z([End])
    X1 --> Z
    X2 --> Z
```

### Trace Table

| Variable / Check | Ajay (Premium, 12 GB) | Pooja (Basic, 4 GB) |
|------------------|-----------------------|---------------------|
| `base_charge` | 799 | 299 |
| `extra_charge` | 12 × 20 = 240.0 | 4 × 20 = 80.0 |
| `extra_data > 10` | True → 100 | False → 0 |
| `final_bill` | 799 + 240 + 100 = **1139.0** | 299 + 80 + 0 = **379.0** |

### Ajay's Bill Breakdown

```mermaid
pie showData title Ajay - Premium plan (Rs. 1139)
    "Base plan" : 799
    "Extra data (12 GB x Rs.20)" : 240
    "Surcharge (> 10 GB)" : 100
```

---

## Q8 – Movie Ticket ([`q8.py`](q8.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read name, age, show_type, day_type"/]
    B --> I["price = 200, discount = 0, surcharge = 0"]
    I --> C{"age < 0 ?"}
    C -- Yes --> X1[/"Invalid age!"/]
    C -- No --> V{"show/day type valid ?"}
    V -- No --> X2[/"Invalid show type or day type!"/]
    V -- Yes --> D{"age < 12 ?"}
    D -- Yes --> D1["discount = 50% of 200 = 100"]
    D -- No --> E{"age >= 60 ?"}
    E -- Yes --> E1["discount = 30% of 200 = 60"]
    E -- No --> M
    D1 --> M{"show == morning ?"}
    E1 --> M
    M -- Yes --> M1["discount = discount + 30"]
    M -- No --> W
    M1 --> W{"day == weekend ?"}
    W -- Yes --> W1["surcharge = 50"]
    W -- No --> F
    W1 --> F["final = 200 - discount + surcharge"]
    F --> P[/"Print ticket"/]
    P --> Z([End])
    X1 --> Z
    X2 --> Z
```

### Trace Table

| Step | Riya (8, Morning, Weekend) | Mohan (65, Evening, Weekday) |
|------|----------------------------|------------------------------|
| Start | price 200, discount 0, surcharge 0 | price 200, discount 0, surcharge 0 |
| Age rule | age < 12 → discount **100.0** | age ≥ 60 → discount **60.0** |
| Morning? | Yes → discount **130.0** | No → 60.0 |
| Weekend? | Yes → surcharge **50** | No → surcharge 0 |
| `final_price` | 200 − 130 + 50 = **120.0** | 200 − 60 + 0 = **140.0** |

### Price Waterfall for Riya

```text
Base price          ₹200  ████████████████████
Child discount     −₹100  ██████████
Morning discount    −₹30  ███
Weekend surcharge   +₹50  █████
───────────────────────────────────────────────
Final price         ₹120  ████████████
```

---

## Q9 – Insurance Premium ([`q9.py`](q9.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read name, age, occupation, smoker"/]
    B --> I["base = 10000, additional = 0"]
    I --> C{"age < 18 ?"}
    C -- Yes --> X1[/"Not Eligible"/]
    C -- No --> V{"occupation and smoker valid ?"}
    V -- No --> X2[/"Invalid input!"/]
    V -- Yes --> D{"age > 50 ?"}
    D -- Yes --> D1["additional += 5000"]
    D -- No --> E
    D1 --> E{"occupation ?"}
    E -- high --> E1["additional += 7000"]
    E -- medium --> E2["additional += 3000"]
    E -- low --> S
    E1 --> S{"smoker == yes ?"}
    E2 --> S
    S -- Yes --> S1["additional += 5000"]
    S -- No --> F
    S1 --> F["final = base + additional"]
    F --> R{"additional >= 10000 ?"}
    R -- Yes --> R1[/"High Risk Policy"/]
    R -- No --> R2[/"Normal Risk Policy"/]
    R1 --> Z([End])
    R2 --> Z
    X1 --> Z
    X2 --> Z
```

### Trace Table – Suresh (55, High, Smoker)

| Step | Check | Result | `additional_charges` |
|------|-------|--------|----------------------|
| 1 | Initial | – | 0 |
| 2 | `age < 18` | False | 0 |
| 3 | `age > 50` | True | 5000 |
| 4 | `occupation == "high"` | True | 12000 |
| 5 | `smoker == "yes"` | True | 17000 |
| 6 | `final_premium = 10000 + 17000` | – | **27000** |
| 7 | `additional >= 10000` | True | High Risk Policy |

Anjali (30, Low, Non-smoker) passes every check without adding anything, so her premium stays at **₹10,000** with a *Normal Risk Policy*. Tom (16) stops at step 2 with *Not Eligible*.

### Premium Composition for Suresh

```mermaid
pie showData title Suresh - final premium Rs. 27000
    "Base premium" : 10000
    "Age above 50" : 5000
    "High-risk occupation" : 7000
    "Smoker" : 5000
```

---

## Q10 – Restaurant Bill ([`q10.py`](q10.py))

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/"Read name, bill, membership"/]
    B --> C{"bill < 0 ?"}
    C -- Yes --> X1[/"Invalid bill amount!"/]
    C -- No --> V{"membership is yes/no ?"}
    V -- No --> X2[/"Invalid membership status!"/]
    V -- Yes --> D{"bill < 1000 ?"}
    D -- Yes --> D1["0%"]
    D -- No --> E{"bill < 3000 ?"}
    E -- Yes --> E1["5%"]
    E -- No --> F{"bill < 5000 ?"}
    F -- Yes --> F1["10%"]
    F -- No --> F2["15%"]
    D1 --> M{"member ?"}
    E1 --> M
    F1 --> M
    F2 --> M
    M -- Yes --> M1["percent + 5"]
    M -- No --> G
    M1 --> G["discount = bill x percent / 100<br/>amount = bill - discount<br/>service = amount x 5 / 100<br/>final = amount + service"]
    G --> T{"final >= 5000 ?"}
    T -- Yes --> T1[/"Thank you message"/]
    T -- No --> Z([End])
    T1 --> Z
    X1 --> Z
    X2 --> Z
```

### Trace Table

| Variable / Check | Kunal (6000, member) | Divya (800, non-member) |
|------------------|----------------------|-------------------------|
| Slab | bill ≥ 5000 → 15% | bill < 1000 → 0% |
| Member bonus | +5% → **20%** | none → **0%** |
| `discount` | 6000 × 20 / 100 = 1200.0 | 0.0 |
| `amount` | 4800.0 | 800.0 |
| `service_charge` | 4800 × 5 / 100 = 240.0 | 800 × 5 / 100 = 40.0 |
| `final_bill` | **5040.0** | **840.0** |
| `final_bill >= 5000` | True → thank-you message | False |

### Kunal's Bill Flow

```text
Original bill   ₹6000
  − 20% discount  ₹1200   →  ₹4800
  + 5% service    ₹240    →  ₹5040   (≥ ₹5000 → "Thank you for being a valued customer")
```
