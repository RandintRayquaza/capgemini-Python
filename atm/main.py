balance = 1000
transactions = []

def check_balance():
    print(f"\nYour Balance: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    
    if amount > 0:
        balance += amount
        transactions.append(f"Deposited ₹{amount}")
        print("Deposit successful!")
    else:
        print("Invalid amount.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        transactions.append(f"Withdrew ₹{amount}")
        print("Withdrawal successful!")

def show_statement():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print("-", t)


while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        show_statement()
    elif choice == "5":
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid choice. Try again.")