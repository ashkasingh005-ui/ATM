#-------------- ATM Simulation Project----------------#

balance = 5000
transactions = []

def display_balance():
    print("\n===== ACCOUNT BALANCE =====")
    print(f"Current Balance: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited: ₹{amount}")
        print("Deposit Successful!")
    else:
        print("Invalid amount!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        transactions.append(f"Withdrawn: ₹{amount}")
        print("Please collect your cash.")

def statement():
    print("\n===== TRANSACTION STATEMENT =====")

    if len(transactions) == 0:
        print("No transactions available.")
    else:
        for i, record in enumerate(transactions, start=1):
            print(f"{i}. {record}")

    print(f"\nAvailable Balance: ₹{balance}")

while True:
    print("\n========== ATM MENU ==========")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        statement()

    elif choice == "5":
        print("\nThank you for using our ATM!")
        break

    else:
        print("Invalid Choice! Please try again.")