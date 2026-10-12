
correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter your PIN: ")
    attempts = attempts + 1

    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")

if attempts == 3 and pin != correct_pin:
    print("Card Temporarily Locked")

print("Attempts Used:", attempts)
