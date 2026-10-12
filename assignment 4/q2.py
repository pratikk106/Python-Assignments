
students = int(input("Enter number of students: "))

total = 0
pass_count = 0
fail_count = 0

for i in range(1, students + 1):
    name = input("\nEnter student name: ")
    marks = float(input("Enter marks out of 100: "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue

    total = total + marks

    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print(name, "Grade:", grade)

    if marks >= 40:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

valid_students = pass_count + fail_count

if valid_students > 0:
    average = total / valid_students
    print("\nClass Average:", average)
    print("Pass Count:", pass_count)
    print("Fail Count:", fail_count)
else:
    print("\nNo valid student marks entered.")
