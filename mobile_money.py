from time import sleep

def display_welcome():
    # Display a Welcome message and the menu
    print("=" * 50)
    print("WELCOME TO MOBILE MONEY SERVICE")
    print("=" * 50)
    print("1. Send Money")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Pay Bill")
    print("6. Exit")

def get_user_choice():
    #Get user's menu choice with validation
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def send_money(balance, mmpin):
    #Handle send money transaction
    print("\n" + "=" * 50)
    print("SEND MONEY")
    print("=" * 50)

    recipient = input("Enter recipient's number")

    while True:
        try:
            amount = float(input("Enter amount to send: "))
            if amount <= 0:
                print("Amount must be positive.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                break
        except ValueError:
            print("Invalid Amount. please enter a number.")
    while True:
        pin = input("Enter your pin to confirm: ")
        if pin == mmpin:
            print(f"\nSending {amount} to {recipient}")
            balance = balance - amount
            print("Transaction Successful!")
            print(f"New balance: {balance}")
            return balance
        else:
            print("Invalid Pin. Enter the correct pin")

def deposit_money(balance):
    #Handle deposit money transaction
    print("\n" + "=" * 50)
    print("DEPOSIT MONEY")
    print("=" * 50)

    while True:
        try:
            amount = float(input("Enter amount to Deposit: "))
            if amount <= 0:
                print("Amount must be positive.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    print(f"\nDepositing {amount}......")
    balance += amount
    print(f"New balance: {balance}")
    return balance

def withdraw_m0ney(balance, mmpin):
    #Handle withdraw money transaction
    print("\n" + "=" * 50)
    print("WITHDRAW MONEY")
    print("=" * 50)

    while True:
        try:
            amount = float(input("Enter amount to withdraw"))
            if amount <= 0:
                print("amount must be positive")
            elif amount > balance:
                print("You have Insufficient balance.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number")

    agent_number = input("Enter agent number: ")
    while True:
        pin = input("Enter your pin to confirm: ")
        if pin == mmpin:
            print(f"\nWithdrawing {amount} from agent {agent_number}")
            balance = balance - amount
            print("Transaction Successful!")
            print(f"New balance: {balance}")
            return balance
        else:
            print("Invalid Pin. Enter the correct pin")

def check_balance(balance, mmpin):
    #Display current balance
    print("\n" + "=" * 50)
    print("CHECK BALANCE")
    print("=" * 50)
    while True:
        pin = input("Enter your pin to confirm: ")
        if pin == mmpin:
            print("Transaction Successful!")
            print(f"Current balance: {balance}")
            return balance
        else:
            print("Invalid Pin. Enter the correct pin")

def pay_bill(balance, mmpin):
    print("\n" + "=" * 50)
    print("PAY BILL")
    print("=" * 50)
    print("1. Electricity")
    print("2. Water")
    print("3. TV Subscription")
    print("4. Internet")
    print("0. Back to main menu")

    while True:
        try:
            choice = int(input("Select bill type (0-4): "))
            if 0 <= choice <= 4:
                break
            else:
                print("Invalid input, Please enter a number between 0 an 5.")
        except ValueError:
            print("Invalid input, Please enter a number.")

    if choice == 0:
        return balance

    bill_types = ["Electricity", "Water", "TV Subscription", "Internet"]
    bill_type = bill_types[choice - 1]

    account_number = input(f"Enter your {bill_type} account number: ")
    while True:
        try:
            amount = float(input("Enter amount to pay: "))
            if amount <= 0:
                print("Amount must be positive")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number")

    while True:
        pin = input("Enter your pin to confirm: ")
        if pin == mmpin:
            print(f"Paying {amount} for {bill_type} account {account_number}")
            balance -= amount
            print("Payment Successful!")
            print(f"Current balance: {balance}")
            return balance
        else:
            print("Invalid Pin. Enter the correct pin")

def main():
    #Main Program Function
    #Initialise the default balance and pin
    print("WELCOME TO MOBILE MONEY SERVICE")
    print("Before using the system, You need to Initialise Balance and pin")
    while True:
        try:
            balance = float(input("Initialise amount on MM: "))
            pin = input("Set Pin: ")
            if len(pin) == 4 and balance:
                print("Pin Set Successfully")
                break
            else:
                print("Pin must be 4 characters. Try again")
        except ValueError:
            print("Invalid value for balance. Please enter a number!")


    while True:
        display_welcome()
        choice = get_user_choice()

        if choice == 1:
            balance = send_money(balance, pin)
        elif choice == 2:
            balance = deposit_money(balance)
        elif choice == 3:
            balance = withdraw_m0ney(balance, pin)
        elif choice == 4:
            check_balance(balance, pin)
        elif choice == 5:
            balance = pay_bill(balance, pin)
        elif choice == 6:
            print("Closing......")
            sleep(2)
            print("Thank you for using mobile money service, Goodbye")
            break

        input("Press Enter to continue")

if __name__ == "__main__":
    main()