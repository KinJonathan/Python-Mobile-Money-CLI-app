from time import sleep

class MobileMoney:
    def __init__(self):
        #Initialise the default balance and pin
        print("WELCOME TO MOBILE MONEY SERVICE")
        print("Before using the system, You need to Initialise Balance and pin")
        name = input("Enter Account name: ")
        number = input("Enter phone number: ")
        while True:
            try:
                balance = float(input("Initial deposit amount on MM: "))
                pin = input("Set Pin: ")
                if len(pin) == 4 and balance:
                    print(f"Successfully Deposited {balance}")
                    print("Pin Set Successfully..")
                    break
                else:
                    print("Pin must be 4 characters. Try again")
            except ValueError:
                print("Invalid value for balance. Please enter a number!")
        self.name = name
        self.number = number
        self.balance = balance
        self.pin = pin
        
    def run_momo(self):
        while True:
            self.display_welcome()
            choice = self.get_user_choice()

            if choice == 1:
                self.send_money()
            elif choice == 2:
                self.deposit_money()
            elif choice == 3:
                self.withdraw_money()
            elif choice == 4:
                self.check_balance()
            elif choice == 5:
                print("Closing......")
                sleep(2)
                print("Thank you for using mobile money service, Goodbye")
                break
            input("Press Enter to continue")
        
    def display_welcome(self):
        # Display a Welcome message and the menu
        print("=" * 50)
        print("WELCOME TO MOBILE MONEY SERVICE")
        print("=" * 50)
        print("1. Send Money")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
    
    def get_user_choice(self):
        #Get user's menu choice with validation
        while True:
            try:
                choice = int(input("Enter your choice (1-5): "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def send_money(self):
        #Handle send money transaction
        print("\n" + "=" * 50)
        print("SEND MONEY")
        print("=" * 50)

        recipient = input("Enter recipient's number: ")

        while True:
            try:
                amount = float(input("Enter amount to send: "))
                if amount <= 0:
                    print("Amount must be positive.")
                elif amount > self.balance:
                    print("Insufficient balance.")
                else:
                    break
            except ValueError:
                print("Invalid Amount. please enter a number.")
        while True:
            pin = input("Enter your pin to confirm: ")
            if pin == self.pin:
                print(f"\nSending {amount} to {recipient}")
                self.balance = self.balance - amount
                print("Transaction Successful!")
                print(f"New balance: {self.balance}")
                break
            else:
                print("Invalid Pin. Enter the correct pin")
    
    def deposit_money(self):
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
        self.balance += amount
        print(f"New balance: {self.balance}")

    def withdraw_money(self):
        #Handle withdraw money transaction
        print("\n" + "=" * 50)
        print("WITHDRAW MONEY")
        print("=" * 50)

        while True:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("amount must be positive")
                elif amount > self.balance:
                    print("You have Insufficient balance.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number")

        agent_number = input("Enter agent number: ")
        while True:
            pin = input("Enter your pin to confirm: ")
            if pin == self.pin:
                print(f"\nWithdrawing {amount} from agent {agent_number}")
                self.balance = self.balance - amount
                print("Transaction Successful!")
                print(f"New balance: {self.balance}")
                break
            else:
                print("Invalid Pin. Enter the correct pin")

    def check_balance(self):
        #Display current balance
        print("\n" + "=" * 50)
        print("CHECK BALANCE")
        print("=" * 50)
        while True:
            pin = input("Enter your pin to confirm: ")
            if pin == self.pin:
                print("Transaction Successful!")
                print(f"Current balance: {self.balance}")
                break
            else:
                print("Invalid Pin. Enter the correct pin")

def main():
    mtn_momo = MobileMoney()
    while True:
        # Display a Welcome message and the menu
        print("=" * 50)
        print("WELCOME TO MOBILE MONEY SERVICE")
        print("=" * 50)
        print("1. Send Money")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = mtn_momo.get_user_choice()
        
        if choice == 1:
            mtn_momo.send_money()
        elif choice == 2:
            mtn_momo.deposit_money()
        elif choice == 3:
            mtn_momo.withdraw_money()
        elif choice == 4:
            mtn_momo.check_balance()
        elif choice == 5:
            print("Closing......")
            sleep(2)
            print("Thank you for using mobile money service, Goodbye")
            break
        input("Press Enter to continue")

if __name__ == "__main__":
    main()