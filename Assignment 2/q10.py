
name = input("Enter customer name: ")
bill = float(input("Enter food bill amount: "))
membership = input("Are you a member? (Yes/No): ").lower()

if bill < 0:
    print("Invalid bill amount!")

elif membership not in ["yes", "no"]:
    print("Invalid membership status!")

else:
    if bill < 1000:
        discount_percent = 0
    elif bill < 3000:
        discount_percent = 5
    elif bill < 5000:
        discount_percent = 10
    else:
        discount_percent = 15

    if membership == "yes":
        discount_percent = discount_percent + 5

    discount = bill * discount_percent / 100
    amount = bill - discount

    service_charge = amount * 5 / 100
    final_bill = amount + service_charge

    print("\nCustomer Name:", name)
    print("Original Bill: Rs.", bill)
    print("Discount: Rs.", discount)
    print("Service Charge: Rs.", service_charge)
    print("Final Payable Amount: Rs.", final_bill)

    if final_bill >= 5000:
        print("Thank you for being a valued customer")
