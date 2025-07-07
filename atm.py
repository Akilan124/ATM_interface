import os
from account import Account

def clear_screen():
    """Clear the terminal screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main function for ATM CLI interaction."""
    print("===== Welcome to Python ATM =====")
    
    # User login input
    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    # Load account from file
    user = Account.load(acc_no, pin)

    if not user:
        print("❌ Invalid credentials or account not found.")
        return

    # Main menu loop
    while True:
        clear_screen()
        print(f"\n Welcome, Account {user.account_number}")
        print("1. View Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")
        choice = input("Select an option: ")

        # Option 1: Check balance
        if choice == '1':
            print(f"Current Balance: ₹{user.check_balance()}")

        # Option 2: Deposit money
        elif choice == '2':
            amt = float(input("Enter amount to deposit: ₹"))
            if user.deposit(amt):
                print(" Deposit successful.")
            else:
                print("Invalid amount.")

        # Option 3: Withdraw money
        elif choice == '3':
            amt = float(input("Enter amount to withdraw: ₹"))
            if user.withdraw(amt):
                print("Withdrawal successful.")
            else:
                print("Insufficient funds or invalid amount.")

        # Option 4: Show transaction history
        elif choice == '4':
            print("\nTransaction History:")
            for entry in user.view_history():
                print(f"   - {entry}")

        # Option 5: Exit and save
        elif choice == '5':
            print(" Saving and exiting...")
            user.save()
            break

        # Invalid option
        else:
            print(" Invalid choice.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
