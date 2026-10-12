''' Problem Statement: Develop a small electricity billing program for a household. The electricity board
 charges different rates according to the number of units consumed.'''

customer_name = input("Enter customer name: ")
units = int(input("Enter units consumed: "))
if units <= 100:
    energy_charge = units * 3
elif units <= 200:
    energy_charge = (100 * 3) + (units - 100) * 4
elif units <= 300:
    energy_charge = (100 * 3) + (100 * 4) + (units - 200) * 5
else:
    energy_charge = (100 * 3) + (100 * 4) + (100 * 5) + (units - 300) * 6

service_charge = 50

final_bill = energy_charge + service_charge

if units <= 100:
    usage_message = "Low electricity usage"
elif units <= 200:
    usage_message = "Moderate electricity usage"
else:
    usage_message = "High electricity usage"

print("\n----- Electricity Bill -----")
print("Customer Name :", customer_name)
print("Units Consumed:", units)
print("Energy Charge :", energy_charge)
print("Service Charge:", service_charge)
print("Final Bill    :", final_bill)
print("Usage Message :", usage_message)
