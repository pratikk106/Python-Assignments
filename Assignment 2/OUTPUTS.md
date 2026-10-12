# Assignment 2 – Program Outputs

Each program was run with the sample inputs shown below. The text after each prompt (for example `Enter customer name: Ravi`) is what the user typed.

---

## Q1 – Electricity Bill ([`q1.py`](q1.py))

**Run 1 – 250 units (three slabs used)**

```text
Enter customer name: Ravi
Enter units consumed: 250

----- Electricity Bill -----
Customer Name : Ravi
Units Consumed: 250
Energy Charge : 950
Service Charge: 50
Final Bill    : 1000
Usage Message : High electricity usage
```

**Run 2 – 80 units (first slab only)**

```text
Enter customer name: Anita
Enter units consumed: 80

----- Electricity Bill -----
Customer Name : Anita
Units Consumed: 80
Energy Charge : 240
Service Charge: 50
Final Bill    : 290
Usage Message : Low electricity usage
```

---

## Q2 – Shopping Checkout ([`q2.py`](q2.py))

**Run 1 – premium customer, large purchase**

```text
Enter customer name: Priya
Enter purchase amount: ₹5500
Enter customer type (Regular/Premium): Premium

----- Shopping Checkout -----
Customer Name     : Priya
Discount Amount   : ₹ 1375.0
Delivery Charge   : ₹ 0
Final Payable     : ₹ 4125.0
```

**Run 2 – regular customer, small purchase**

```text
Enter customer name: Amit
Enter purchase amount: ₹1500
Enter customer type (Regular/Premium): Regular

----- Shopping Checkout -----
Customer Name     : Amit
Discount Amount   : ₹ 75.0
Delivery Charge   : ₹ 100
Final Payable     : ₹ 1525.0
```

---

## Q3 – ATM Transaction ([`q3.py`](q3.py))

**Run 1 – successful withdrawal with low-balance warning**

```text
Enter account holder name: Rahul
Enter current balance: ₹15000
Enter withdrawal amount: ₹14500

----- ATM Transaction -----
Account Holder : Rahul
Transaction Status : Successful
Withdrawn Amount   : ₹ 14500.0
Remaining Balance  : ₹ 500.0
Low Balance Warning
```

**Run 2 – insufficient balance**

```text
Enter account holder name: Sneha
Enter current balance: ₹5000
Enter withdrawal amount: ₹8000

----- ATM Transaction -----
Account Holder : Sneha
Transaction Status : Rejected
Reason : Insufficient balance
```

**Run 3 – above the ₹20,000 limit**

```text
Enter account holder name: Kiran
Enter current balance: ₹50000
Enter withdrawal amount: ₹25000

----- ATM Transaction -----
Account Holder : Kiran
Transaction Status : Rejected
Reason : Maximum withdrawal allowed is ₹20,000
```

---

## Q4 – Scholarship Eligibility ([`q4.py`](q4.py))

**Run 1 – full scholarship**

```text
Enter student name: Meera
Enter percentage: 92
Enter annual family income: 300000
Enter attendance percentage: 85

Student Name: Meera
Eligibility Status: Eligible
Scholarship Category: Full Scholarship
```

**Run 2 – not eligible (all three reasons)**

```text
Enter student name: Arjun
Enter percentage: 70
Enter annual family income: 500000
Enter attendance percentage: 60

Student Name: Arjun
Eligibility Status: Not Eligible
Scholarship Category: None
Reason: Percentage is below 75%
Reason: Family income exceeds Rs. 4,00,000
Reason: Attendance is below 75%
```

---

## Q5 – Employee Bonus ([`q5.py`](q5.py))

**Run 1 – 20% bonus, excellent performer**

```text
Enter employee name: Vikram
Enter monthly salary: 60000
Enter years of experience: 12
Enter performance rating (1-5): 5

Employee Name: Vikram
Bonus Percentage: 20 %
Bonus Amount: Rs. 12000.0
Final Salary: Rs. 72000.0
Performance Message: Excellent Performer
```

**Run 2 – 10% bonus**

```text
Enter employee name: Neha
Enter monthly salary: 40000
Enter years of experience: 3
Enter performance rating (1-5): 3

Employee Name: Neha
Bonus Percentage: 10 %
Bonus Amount: Rs. 4000.0
Final Salary: Rs. 44000.0
Performance Message: Keep Improving
```

**Run 3 – invalid rating**

```text
Enter employee name: Karan
Enter monthly salary: 30000
Enter years of experience: 5
Enter performance rating (1-5): 7
Invalid rating! Enter rating between 1 and 5.
```

---

## Q6 – Hotel Booking ([`q6.py`](q6.py))

**Run 1 – Deluxe room, 6 nights (10% discount)**

```text
Enter guest name: Rohan
Enter room type (Standard/Deluxe/Suite): Deluxe
Enter number of nights: 6

Guest Name: Rohan
Room Type: Deluxe
Number of Nights: 6
Room Charge: Rs. 21000
Discount: Rs. 2100.0
Final Booking Amount: Rs. 18900.0
```

**Run 2 – Suite, 12 nights (20% discount)**

```text
Enter guest name: Sara
Enter room type (Standard/Deluxe/Suite): Suite
Enter number of nights: 12

Guest Name: Sara
Room Type: Suite
Number of Nights: 12
Room Charge: Rs. 72000
Discount: Rs. 14400.0
Final Booking Amount: Rs. 57600.0
```

---

## Q7 – Mobile Data Plan Bill ([`q7.py`](q7.py))

**Run 1 – Premium plan with surcharge**

```text
Enter customer name: Ajay
Enter plan type (Basic/Standard/Premium): Premium
Enter extra data used in GB: 12

Customer Name: Ajay
Plan Type: Premium
Base Plan Charge: Rs. 799
Extra Data Charge: Rs. 240.0
Surcharge: Rs. 100
Final Bill: Rs. 1139.0
```

**Run 2 – Basic plan, no surcharge**

```text
Enter customer name: Pooja
Enter plan type (Basic/Standard/Premium): Basic
Enter extra data used in GB: 4

Customer Name: Pooja
Plan Type: Basic
Base Plan Charge: Rs. 299
Extra Data Charge: Rs. 80.0
Surcharge: Rs. 0
Final Bill: Rs. 379.0
```

---

## Q8 – Movie Ticket ([`q8.py`](q8.py))

**Run 1 – child, morning show, weekend**

```text
Enter customer name: Riya
Enter age: 8
Enter show type (Morning/Evening): Morning
Enter day type (Weekday/Weekend): Weekend

Customer Name: Riya
Original Ticket Price: Rs. 200
Discount: Rs. 130.0
Weekend Surcharge: Rs. 50
Final Ticket Price: Rs. 120.0
```

**Run 2 – senior citizen, evening show, weekday**

```text
Enter customer name: Mohan
Enter age: 65
Enter show type (Morning/Evening): Evening
Enter day type (Weekday/Weekend): Weekday

Customer Name: Mohan
Original Ticket Price: Rs. 200
Discount: Rs. 60.0
Weekend Surcharge: Rs. 0
Final Ticket Price: Rs. 140.0
```

---

## Q9 – Insurance Premium ([`q9.py`](q9.py))

**Run 1 – high-risk policy**

```text
Enter customer name: Suresh
Enter age: 55
Enter occupation risk (Low/Medium/High): High
Are you a smoker? (Yes/No): Yes

Customer Name: Suresh
Eligibility: Eligible
Base Premium: Rs. 10000
Additional Charges: Rs. 17000
Final Premium: Rs. 27000
Risk Message: High Risk Policy
```

**Run 2 – normal-risk policy**

```text
Enter customer name: Anjali
Enter age: 30
Enter occupation risk (Low/Medium/High): Low
Are you a smoker? (Yes/No): No

Customer Name: Anjali
Eligibility: Eligible
Base Premium: Rs. 10000
Additional Charges: Rs. 0
Final Premium: Rs. 10000
Risk Message: Normal Risk Policy
```

**Run 3 – under 18**

```text
Enter customer name: Tom
Enter age: 16
Enter occupation risk (Low/Medium/High): Low
Are you a smoker? (Yes/No): No
Eligibility: Not Eligible
```

---

## Q10 – Restaurant Bill ([`q10.py`](q10.py))

**Run 1 – member with a large bill**

```text
Enter customer name: Kunal
Enter food bill amount: 6000
Are you a member? (Yes/No): Yes

Customer Name: Kunal
Original Bill: Rs. 6000.0
Discount: Rs. 1200.0
Service Charge: Rs. 240.0
Final Payable Amount: Rs. 5040.0
Thank you for being a valued customer
```

**Run 2 – non-member with a small bill**

```text
Enter customer name: Divya
Enter food bill amount: 800
Are you a member? (Yes/No): No

Customer Name: Divya
Original Bill: Rs. 800.0
Discount: Rs. 0.0
Service Charge: Rs. 40.0
Final Payable Amount: Rs. 840.0
```
