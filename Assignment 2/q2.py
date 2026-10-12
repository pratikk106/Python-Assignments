'''Problem Statement: Create a checkout program for an online shopping website. The discount depends on
the purchase amount, and premium customers receive an additional benefit.'''

customer_name = input("Enter customer name: ")
purchase_amount = float(input("Enter purchase amount: ₹"))
customer_type = input("Enter customer type (Regular/Premium): ")

if purchase_amount >= 5000:
    discount_rate = 20
elif purchase_amount >= 3000 and purchase_amount < 5000:
    discount_rate = 10
elif purchase_amount >= 1000 and purchase_amount < 3000:
    discount_rate = 5
else:
    discount_rate = 0

if customer_type.lower() == "premium":
    if purchase_amount > 0:
        discount_rate = discount_rate + 5

discount_amount = purchase_amount * discount_rate / 100

final_amount = purchase_amount - discount_amount

if final_amount >= 2000:
    delivery_charge = 0
else:
    if final_amount < 2000:
        delivery_charge = 100

final_payable = final_amount + delivery_charge

print("\n----- Shopping Checkout -----")
print("Customer Name     :", customer_name)
print("Discount Amount   : ₹", discount_amount)
print("Delivery Charge   : ₹", delivery_charge)
print("Final Payable     : ₹", final_payable)
