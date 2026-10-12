
name = input("Enter customer name: ")
plan = input("Enter plan type (Basic/Standard/Premium): ").lower()
extra_data = float(input("Enter extra data used in GB: "))

if extra_data < 0:
    print("Invalid data usage!")

else:
    if plan == "basic":
        base_charge = 299
    elif plan == "standard":
        base_charge = 499
    elif plan == "premium":
        base_charge = 799
    else:
        base_charge = 0
        print("Invalid plan type!")

    if base_charge > 0:
        extra_charge = extra_data * 20

        if extra_data > 10:
            surcharge = 100
        else:
            surcharge = 0

        final_bill = base_charge + extra_charge + surcharge

        print("\nCustomer Name:", name)
        print("Plan Type:", plan.title())
        print("Base Plan Charge: Rs.", base_charge)
        print("Extra Data Charge: Rs.", extra_charge)
        print("Surcharge: Rs.", surcharge)
        print("Final Bill: Rs.", final_bill)
