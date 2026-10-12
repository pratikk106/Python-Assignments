
name = input("Enter customer name: ")
age = int(input("Enter age: "))
occupation = input("Enter occupation risk (Low/Medium/High): ").lower()
smoker = input("Are you a smoker? (Yes/No): ").lower()

base_premium = 10000
additional_charges = 0

if age < 18:
    print("Eligibility: Not Eligible")

elif occupation not in ["low", "medium", "high"] or smoker not in ["yes", "no"]:
    print("Invalid occupation risk or smoking status!")

else:
    if age > 50:
        additional_charges = additional_charges + 5000

    if occupation == "high":
        additional_charges = additional_charges + 7000
    elif occupation == "medium":
        additional_charges = additional_charges + 3000

    if smoker == "yes":
        additional_charges = additional_charges + 5000

    final_premium = base_premium + additional_charges

    print("\nCustomer Name:", name)
    print("Eligibility: Eligible")
    print("Base Premium: Rs.", base_premium)
    print("Additional Charges: Rs.", additional_charges)
    print("Final Premium: Rs.", final_premium)

    if additional_charges >= 10000:
        print("Risk Message: High Risk Policy")
    else:
        print("Risk Message: Normal Risk Policy")
