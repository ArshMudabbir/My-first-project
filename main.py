pin = "1234"
balance = 1000
attempts = 0
transactions = []

print("===== WELCOME TO PYTHON ATM =====")

# PIN check
while attempts < 3:
    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin == pin:
        print("PIN accepted. Access granted.\n")

        while True:
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Transactions")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                print("Current balance:", balance)

            elif choice == "2":
                amount = int(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    transactions.append("Deposited " + str(amount))
                    print("Deposit successful.")
                else:
                    print("Invalid amount.")

            elif choice == "3":
                amount = int(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Invalid amount.")
                elif amount > balance:
                    print("Insufficient balance.")
                else:
                    balance -= amount
                    transactions.append("Withdrew " + str(amount))
                    print("Please take your cash.")

            elif choice == "4":
                print("Transaction History:")
                if len(transactions) == 0:
                    print("No transactions yet.")
                else:
                    for t in transactions:
                        print("-", t)

            elif choice == "5":
                print("Thank you for using the ATM.")
                break

            else:
                print("Invalid choice.")

        break

    else:
        attempts += 1
        print("Incorrect PIN.")

if attempts == 3:
    print("Account locked. Too many incorrect attempts.")
