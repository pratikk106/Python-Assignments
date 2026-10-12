
name = input("Enter guest name: ")
room_type = input("Enter room type (Standard/Deluxe/Suite): ").lower()
nights = int(input("Enter number of nights: "))

if nights <= 0:
    print("Invalid number of nights!")

else:
    if room_type == "standard":
        price = 2000
    elif room_type == "deluxe":
        price = 3500
    elif room_type == "suite":
        price = 6000
    else:
        price = 0
        print("Invalid room type!")

    if price > 0:
        room_charge = price * nights

        if nights >= 10:
            discount = room_charge * 20 / 100
        elif nights >= 5:
            discount = room_charge * 10 / 100
        else:
            discount = 0

        final_amount = room_charge - discount

        print("\nGuest Name:", name)
        print("Room Type:", room_type.title())
        print("Number of Nights:", nights)
        print("Room Charge: Rs.", room_charge)
        print("Discount: Rs.", discount)
        print("Final Booking Amount: Rs.", final_amount)
