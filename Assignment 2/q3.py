'''Problem Statement: Build a simple ATM transaction program that allows a customer to withdraw money
after checking account balance and withdrawal limits.'''

account_name = input("Enter account holder name: ")
balance = float(input("Enter current balance: ₹"))
withdrawal = float(input("Enter withdrawal amount: ₹"))

if withdrawal > 0:
    if withdrawal <= balance:
        if withdrawal <= 20000:

            remaining_balance = balance - withdrawal

            print("\n----- ATM Transaction -----")
            print("Account Holder :", account_name)
            print("Transaction Status : Successful")
            print("Withdrawn Amount   : ₹", withdrawal)
            print("Remaining Balance  : ₹", remaining_balance)

            if remaining_balance < 1000:
                print("Low Balance Warning")

        else:
            print("\n----- ATM Transaction -----")
            print("Account Holder :", account_name)
            print("Transaction Status : Rejected")
            print("Reason : Maximum withdrawal allowed is ₹20,000")

    else:
        print("\n----- ATM Transaction -----")
        print("Account Holder :", account_name)
        print("Transaction Status : Rejected")
        print("Reason : Insufficient balance")

else:
    print("\n----- ATM Transaction -----")
    print("Account Holder :", account_name)
    print("Transaction Status : Rejected")
    print("Reason : Withdrawal amount must be greater than ₹0")
