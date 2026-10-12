
products = int(input("Enter number of products: "))

subtotal = 0

for i in range(1, products + 1):
    print("\nProduct", i)

    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity < 0:
        print("Invalid price or quantity!")
        continue

    item_total = price * quantity
    subtotal = subtotal + item_total

    print("Item Subtotal:", item_total)

if subtotal >= 3000:
    discount = subtotal * 10 / 100
else:
    discount = 0

amount = subtotal - discount

if amount < 1500:
    delivery = 100
else:
    delivery = 0

final_amount = amount + delivery

print("\nSubtotal:", subtotal)
print("Discount:", discount)
print("Delivery Charge:", delivery)
print("Final Payable Amount:", final_amount)
