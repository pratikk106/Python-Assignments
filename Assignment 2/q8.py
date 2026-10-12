
name = input("Enter customer name: ")
age = int(input("Enter age: "))
show_type = input("Enter show type (Morning/Evening): ").lower()
day_type = input("Enter day type (Weekday/Weekend): ").lower()

price = 200
discount = 0
surcharge = 0

if age < 0:
    print("Invalid age!")

elif show_type not in ["morning", "evening"] or day_type not in ["weekday", "weekend"]:
    print("Invalid show type or day type!")

else:
    if age < 12:
        discount = price * 50 / 100
    elif age >= 60:
        discount = price * 30 / 100

    if show_type == "morning":
        discount = discount + 30

    if day_type == "weekend":
        surcharge = 50

    final_price = price - discount + surcharge

    print("\nCustomer Name:", name)
    print("Original Ticket Price: Rs.", price)
    print("Discount: Rs.", discount)
    print("Weekend Surcharge: Rs.", surcharge)
    print("Final Ticket Price: Rs.", final_price)
