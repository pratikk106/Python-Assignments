# Assignment 4 – Program Outputs

Each program was run with the sample inputs shown below. The text after each prompt (for example `Enter number of days: 5`) is what the user typed.

---

## Q1 – Daily Expense Tracker ([`q1.py`](q1.py))

```text
Enter number of days: 5
Enter expense for day 1: 800
Enter expense for day 2: 1200
Enter expense for day 3: 950
Enter expense for day 4: 1500
Enter expense for day 5: 1100
Total Expense: Rs. 5550.0
Average Daily Expense: Rs. 1110.0
Highest Daily Expense: Rs. 1500.0
Budget Alert
```

---

## Q2 – Class Grade Calculator ([`q2.py`](q2.py))

The fourth student's marks (120) are invalid, so that entry is skipped.

```text
Enter number of students: 4

Enter student name: Aman
Enter marks out of 100: 82
Aman Grade: A

Enter student name: Bela
Enter marks out of 100: 65
Bela Grade: B

Enter student name: Chirag
Enter marks out of 100: 35
Chirag Grade: Fail

Enter student name: Dev
Enter marks out of 100: 120
Invalid marks! Enter marks between 0 and 100.

Class Average: 60.666666666666664
Pass Count: 2
Fail Count: 1
```

---

## Q3 – ATM PIN Verification ([`q3.py`](q3.py))

**Run 1 – correct PIN on the second attempt**

```text
Enter your PIN: 1111
Incorrect PIN
Enter your PIN: 1234
Access Granted
Attempts Used: 2
```

**Run 2 – three wrong attempts**

```text
Enter your PIN: 0000
Incorrect PIN
Enter your PIN: 1111
Incorrect PIN
Enter your PIN: 2222
Incorrect PIN
Card Temporarily Locked
Attempts Used: 3
```

---

## Q4 – Shopping Cart ([`q4.py`](q4.py))

```text
Enter number of products: 3

Product 1
Enter price: 500
Enter quantity: 2
Item Subtotal: 1000.0

Product 2
Enter price: 1200
Enter quantity: 1
Item Subtotal: 1200.0

Product 3
Enter price: 250
Enter quantity: 4
Item Subtotal: 1000.0

Subtotal: 3200.0
Discount: 320.0
Delivery Charge: 0
Final Payable Amount: 2880.0
```

---

## Q5 – Number Guessing Game ([`q5.py`](q5.py))

**Run 1 – win on the third guess**

```text
Guess the secret number: 50
Too high
Guess the secret number: 20
Too low
Guess the secret number: 37
You Win! Correct guess.
Attempts used: 3
```

**Run 2 – all five guesses wrong**

```text
Guess the secret number: 10
Too low
Guess the secret number: 20
Too low
Guess the secret number: 30
Too low
Guess the secret number: 40
Too high
Guess the secret number: 50
Too high
You Lose! The secret number was 37
Attempts used: 5
```

---

## Q6 – Electricity Usage Analyser ([`q6.py`](q6.py))

```text
Enter number of days: 7
Enter units consumed on day 1: 8
Enter units consumed on day 2: 12
Enter units consumed on day 3: 9
Enter units consumed on day 4: 15
Enter units consumed on day 5: 10
Enter units consumed on day 6: 11
Enter units consumed on day 7: 7

Total Units: 72.0
Average Usage: 10.285714285714286
High-Usage Days: 3
Maximum Daily Usage: 15.0
Usage Status: Normal Usage
```

---

## Q7 – Employee Payroll ([`q7.py`](q7.py))

```text
Enter number of employees: 2

Employee 1
Enter employee name: Asha
Enter basic salary: 45000
Enter overtime hours: 10
Employee Name: Asha
Gross Salary: 47000.0
Deduction: 2350.0
Net Salary: 44650.0

Employee 2
Enter employee name: Bharat
Enter basic salary: 52000
Enter overtime hours: 5
Employee Name: Bharat
Gross Salary: 53000.0
Deduction: 5300.0
Net Salary: 47700.0

Total Net Payroll: 92350.0
Employee Count: 2
```

---

## Q8 – Quiz ([`q8.py`](q8.py))

```text
1. What is the capital of India? Delhi
Correct!
2. How many days are in a week? 7
Correct!
3. Which language is used for web page styling? CSS
Correct!
4. What is 5 + 5? 12
Wrong!
5. Which planet is known as the Red Planet? Mars
Correct!
6. What is the largest ocean on Earth? Atlantic
Wrong!

Score: 4 out of 6
Percentage: 66.66666666666666 %
Good
```

---

## Q9 – Bank Transaction Simulator ([`q9.py`](q9.py))

```text
Enter opening balance: 5000
Enter number of transactions: 4

Transaction 1
Enter type (deposit/withdraw): deposit
Enter amount: 2000
Deposit Successful

Transaction 2
Enter type (deposit/withdraw): withdraw
Enter amount: 3000
Withdrawal Successful

Transaction 3
Enter type (deposit/withdraw): withdraw
Enter amount: 6000
Insufficient Balance. Withdrawal Rejected

Transaction 4
Enter type (deposit/withdraw): withdraw
Enter amount: 3500
Withdrawal Successful

Final Balance: Rs. 500.0
Deposit Count: 1
Successful Withdrawals: 2
Rejected Withdrawals: 1
Warning: Low Balance
```

---

## Q10 – Multiplication Table and Range Analysis ([`q10.py`](q10.py))

```text
Enter a positive integer: 7

Multiplication Table of 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

Enter start of range: 1
Enter end of range: 10

Even Count: 5
Odd Count: 5
Sum of Range: 55
```
