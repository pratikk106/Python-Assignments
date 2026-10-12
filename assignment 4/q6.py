
days = int(input("Enter number of days: "))

total = 0
high_count = 0
maximum = 0

for i in range(1, days + 1):
    units = float(input("Enter units consumed on day " + str(i) + ": "))

    total = total + units

    if units > 10:
        high_count = high_count + 1

    if i == 1 or units > maximum:
        maximum = units

average = total / days

print("\nTotal Units:", total)
print("Average Usage:", average)
print("High-Usage Days:", high_count)
print("Maximum Daily Usage:", maximum)

if total > 300:
    print("Usage Status: High Usage")
else:
    print("Usage Status: Normal Usage")
