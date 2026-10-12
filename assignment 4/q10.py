
number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    print("\nMultiplication Table of", number)

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

start = int(input("\nEnter start of range: "))
end = int(input("Enter end of range: "))

if start > end:
    print("Invalid range! Start should not be greater than end.")
else:
    even_count = 0
    odd_count = 0
    total = 0

    for i in range(start, end + 1):
        total = total + i

        if i % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1

    print("\nEven Count:", even_count)
    print("Odd Count:", odd_count)
    print("Sum of Range:", total)
