
balance = float(input("Enter opening balance: "))
transactions = int(input("Enter number of transactions: "))

deposit_count = 0
successful_withdrawals = 0
rejected_withdrawals = 0

for i in range(1, transactions + 1):
    print("\nTransaction", i)
    transaction_type = input("Enter type (deposit/withdraw): ").lower()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount!")

    elif transaction_type == "deposit":
        balance = balance + amount
        deposit_count = deposit_count + 1
        print("Deposit Successful")

    elif transaction_type == "withdraw":
        if amount <= balance:
            balance = balance - amount
            successful_withdrawals = successful_withdrawals + 1
            print("Withdrawal Successful")
        else:
            rejected_withdrawals = rejected_withdrawals + 1
            print("Insufficient Balance. Withdrawal Rejected")

    else:
        print("Invalid transaction type!")

print("\nFinal Balance: Rs.", balance)
print("Deposit Count:", deposit_count)
print("Successful Withdrawals:", successful_withdrawals)
print("Rejected Withdrawals:", rejected_withdrawals)

if balance < 1000:
    print("Warning: Low Balance")
