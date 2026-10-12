
name = input("Enter employee name: ")
salary = float(input("Enter monthly salary: "))
experience = int(input("Enter years of experience: "))
rating = int(input("Enter performance rating (1-5): "))

if rating < 1 or rating > 5:
    print("Invalid rating! Enter rating between 1 and 5.")

else:
    if experience >= 10 and rating >= 4:
        bonus_percent = 20
    elif experience >= 5 and rating >= 4:
        bonus_percent = 15
    elif experience >= 2 and rating >= 3:
        bonus_percent = 10
    else:
        bonus_percent = 0

    bonus_amount = salary * bonus_percent / 100
    final_salary = salary + bonus_amount

    print("\nEmployee Name:", name)
    print("Bonus Percentage:", bonus_percent, "%")
    print("Bonus Amount: Rs.", bonus_amount)
    print("Final Salary: Rs.", final_salary)

    if rating == 5:
        print("Performance Message: Excellent Performer")
    else:
        print("Performance Message: Keep Improving")
