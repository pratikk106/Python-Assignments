
employees = int(input("Enter number of employees: "))

total_payroll = 0

for i in range(1, employees + 1):
    print("\nEmployee", i)

    name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: "))
    overtime_hours = float(input("Enter overtime hours: "))

    overtime_pay = overtime_hours * 200

    gross_salary = basic_salary + overtime_pay

    if gross_salary >= 50000:
        deduction = gross_salary * 10 / 100
    else:
        deduction = gross_salary * 5 / 100

    net_salary = gross_salary - deduction

    total_payroll = total_payroll + net_salary

    print("Employee Name:", name)
    print("Gross Salary:", gross_salary)
    print("Deduction:", deduction)
    print("Net Salary:", net_salary)

print("\nTotal Net Payroll:", total_payroll)
print("Employee Count:", employees)
