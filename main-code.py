from datetime import datetime

# Pre-Saved ATM accounts
accounts = {
    "1234567890123456": {
        "name": "Ron Ivan Baniqued",
        "pin": "1234",
        "pcn": "9001",
        "balance": 10000.00,
        "history": [],
        "locked": False,
        "recovery_used": False
    },
    "9876543210987654": {
        "name": "Yzekiel Zachary Nahil",
        "pin": "5678",
        "pcn": "3451",
        "balance": 15000.00,
        "history": [],
        "locked": False,
        "recovery_used": False
    },
    "1111222233334444": {
        "name": "Jose Manuel Navoa",
        "pin": "0000",
        "pcn": "1003",
        "balance": 20000.00,
        "history": [],
        "locked": False,
        "recovery_used": False
    },
    "2233445566778899": {
        "name": "Justin Rafael Tengco",
        "pin": "5678",
        "pcn": "4045",
        "balance": 1000.00,
        "history": [],
        "locked": False,
        "recovery_used": False
    },
}

# Handles the login process
def login():

    print("\n" + "=" * 45)
    print("             WELCOME TO PYTHON ATM")
    print("=" * 45)

    card_number = input("Enter your 16-digit card number: ").strip()

    # Check if the card number exists
    if card_number not in accounts:
        print("\nCard number not found.")
        print("Please check your card number and try again.")
        return None

    account = accounts[card_number]

    # Check if the account is locked
    if account["locked"]:
        print("\nAccount number is locked.")

        if account["recovery_used"]:
            print("Card recovery has already been used.")

        print("Please visit your bank to recover your card.")
        return None

    # Allow only 3 PIN attempts
    attempts = 3

    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ").strip()

        # Check if the PIN is correct
        if account["pin"] == pin:
            print("\nLogin successful!")
            print(f"Welcome, {account['name']}!")
            return card_number

        attempts -= 1

        if attempts > 0:
            print("\nIncorrect PIN.")
            print(f"You have {attempts} attempt(s) remaining.")

        else:
            # Lock the account after 3 incorrect PIN attempts
            account["locked"] = True

            print("\nIncorrect PIN.")
            print("You have reached the maximum number of PIN attempts.")
            print("Your card has been locked.")

            # Check if card recovery has already been used
            if account["recovery_used"]:
                print("\nCard recovery has already been used.")
                print("Your card cannot be recovered again.")
                print("Please visit your bank to recover your card.")
                return None

            # Ask if the user wants to recover the card
            print("\nWould you like to proceed with card recovery?")
            print("1. Yes")
            print("2. No")

            while True:
                recovery_choice = input("Enter your choice: ").strip()

                if recovery_choice == "1":
                    # Start card recovery without asking for card number again
                    recovered = recover_card(account)

                    if not recovered:
                        return None

                    return login()

                elif recovery_choice == "2":
                    print("\nCard recovery cancelled.")
                    print("Your card remains locked.")
                    print("Please visit your bank to recover your card.")
                    return None

                else:
                    print("\nInvalid choice.")
                    print("Please enter 1 or 2.")

# Handles the card recovery process
def recover_card(account):
    print("\n" + "=" * 45)
    print("              CARD RECOVERY")
    print("=" * 45)
    print("This card has been locked due to")
    print("too many incorrect PIN attempts.")
    print()
    print("To recover your card, please verify")
    print("your identity using your PhilSys Card Number (PCN).")
    print()
    print("Enter the LAST 4 DIGITS of your")
    print("12-digit PhilSys Card Number (PCN).")
    print("=" * 45)

    attempts = 3

    while attempts > 0:
        pcn = input("\nEnter last 4 digits of your PCN: ").strip()

        attempts -= 1

        if attempts > 0:
            print("\nIncorrect PCN.")
            print(f"You have {attempts} attempt(s) remaining.")

        else:
            print("\nIncorrect PCN.")
            print("You have reached the maximum number")
            print("of card recovery attempts.")
            print("Your card is still locked.")
            print("Please visit your bank to recover your card.")
            continue

        # Get the 4 digits from the stored PCN
        correct_pcn = account["pcn"]

        # Check if the entered PCN digits are correct
        if pcn == correct_pcn:
            account["locked"] = False

            # Mark card recovery as already used
            account["recovery_used"] = True

            print("\nPCN verification successful!")
            print("Your identity has been verified.")
            print("Your card has been successfully recovered.")
            print()
            print("Card recovery can only be used once.")
            print("=" * 45)
            return True

    return False

# Creates a unique transaction number
def get_transaction_number():
    global transaction_number
    transaction_number += 1
    return f"ATM{transaction_number}"

# Starting transaction number
transaction_number = 1000

# Displays the receipt after a transaction
def show_receipt(transaction_type, amount, transaction_number, account_name, balance, extra_info=""):
    current_time = datetime.now()

    print("\n" + "=" * 45)
    print("                 ATM RECEIPT")
    print("=" * 45)
    print(f"Date       : {current_time.strftime('%B %d, %Y')}")
    print(f"Time       : {current_time.strftime('%I:%M:%S %p')}")
    print(f"Transaction: {transaction_number}")
    print(f"Account    : {account_name}")
    print(f"Type       : {transaction_type}")
    print(f"Amount     : PHP {amount:,.2f}")

    if extra_info:
        print(extra_info)

    print(f"Balance    : PHP {balance:,.2f}")
    print("=" * 45)
    print("       Thank you for using our ATM!")
    print("=" * 45)

# Adds a transaction to the account history
def add_transaction(account, transaction_type, amount, transaction_id, details=""):
    current_time = datetime.now()

    transaction = {
        "transaction_id": transaction_id,
        "type": transaction_type,
        "amount": amount,
        "date": current_time.strftime("%B %d, %Y"),
        "time": current_time.strftime("%I:%M:%S %p"),
        "details": details
    }

    account["history"].append(transaction)

# Displays the current balance
def balance_inquiry(account):
    print("\n" + "=" * 45)
    print("             BALANCE INQUIRY")
    print("=" * 45)
    print(f"Account Holder : {account['name']}")
    print(f"Current Balance: PHP {account['balance']:,.2f}")
    print("=" * 45)

# Handles cash withdrawal
def withdraw_cash(account):
    print("\n" + "=" * 45)
    print("              WITHDRAW CASH")
    print("=" * 45)

    try:
        amount = float(input("Enter amount to withdraw: PHP "))

        # Make sure the amount is valid
        if amount <= 0:
            print("\nPlease enter an amount greater than zero.")
            return

        # Check if the account has enough money
        if amount > account["balance"]:
            print("\nInsufficient balance.")
            return

        # Subtract the withdrawal from the balance
        account["balance"] -= amount

        # Create a transaction number
        transaction_id = get_transaction_number()

        # Save the transaction
        add_transaction(
            account,
            "WITHDRAWAL",
            amount,
            transaction_id
        )

        print("\nWithdrawal successful!")

        # Display receipt
        show_receipt(
            "CASH WITHDRAWAL",
            amount,
            transaction_id,
            account["name"],
            account["balance"]
        )

    except ValueError:
        print("\nInvalid input. Please enter numbers only.")

# Handles cash deposits
def deposit_cash(account):
    print("\n" + "=" * 45)
    print("               DEPOSIT CASH")
    print("=" * 45)

    try:
        amount = float(input("Enter amount to deposit: PHP "))

        # Make sure the amount is valid
        if amount <= 0:
            print("\nPlease enter an amount greater than zero.")
            return

        # Add the deposit to the balance
        account["balance"] += amount

        # Create a transaction number
        transaction_id = get_transaction_number()

        # Save the transaction
        add_transaction(
            account,
            "DEPOSIT",
            amount,
            transaction_id
        )

        print("\nDeposit successful!")

        # Display receipt
        show_receipt(
            "CASH DEPOSIT",
            amount,
            transaction_id,
            account["name"],
            account["balance"]
        )

    except ValueError:
        print("\nInvalid input. Please enter numbers only.")

# Handles transferring money between accounts
def transfer_money(sender_card, sender_account):
    print("\n" + "=" * 45)
    print("              TRANSFER MONEY")
    print("=" * 45)

    # Ask for the recipient's card number
    receiver_card = input("Enter recipient's 16-digit card number: ").strip()

    # Check if recipient exists
    if receiver_card not in accounts:
        print("\nRecipient account was not found.")
        return

    # Prevent transferring to the same account
    if receiver_card == sender_card:
        print("\nYou cannot transfer money to your own account.")
        return

    receiver_account = accounts[receiver_card]

    print(f"\nRecipient: {receiver_account['name']}")

    try:
        amount = float(input("Enter amount to transfer: PHP "))

        # Check if amount is valid
        if amount <= 0:
            print("\nPlease enter an amount greater than zero.")
            return

        # Check if sender has enough money
        if amount > sender_account["balance"]:
            print("\nInsufficient balance.")
            return

        # Remove money from sender
        sender_account["balance"] -= amount

        # Add money to receiver
        receiver_account["balance"] += amount

        # Create one transaction number
        transaction_id = get_transaction_number()

        # Save transaction to sender's history
        add_transaction(
            sender_account,
            "TRANSFER SENT",
            amount,
            transaction_id,
            f"To: {receiver_account['name']}"
        )

        # Save transaction to receiver's history
        add_transaction(
            receiver_account,
            "TRANSFER RECEIVED",
            amount,
            transaction_id,
            f"From: {sender_account['name']}"
        )

        print("\nTransfer successful!")

        # Display receipt for sender
        show_receipt(
            "MONEY TRANSFER",
            amount,
            transaction_id,
            sender_account["name"],
            sender_account["balance"],
            f"Transferred To: {receiver_account['name']}"
        )

    except ValueError:
        print("\nInvalid input. Please enter numbers only.")

# Displays the transaction history
def transaction_history(account):
    print("\n" + "=" * 45)
    print("                 TRANSACTION HISTORY")
    print("=" * 45)

    history = account["history"]

    # Check if there are no transactions
    if len(history) == 0:
        print("No transactions have been made yet.")

    else:
        # Loop through every transaction
        for transaction in history:
            print(f"\nTransaction Number: {transaction['transaction_id']}")
            print(f"Type              : {transaction['type']}")
            print(f"Amount            : PHP {transaction['amount']:,.2f}")
            print(f"Date              : {transaction['date']}")
            print(f"Time              : {transaction['time']}")

            if transaction["details"]:
                print(f"Details           : {transaction['details']}")

            print("-" * 45)

# Asks the user if they want to perform another transaction
def another_transaction():
    print("\nWould you like to perform another transaction?")
    print("1. Yes")
    print("2. No")

    while True:
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            return True

        elif choice == "2":
            return False

        else:
            print("\nInvalid choice. Please enter 1 or 2.")

# Displays the main ATM menu
def atm_menu(card_number):
    account = accounts[card_number]

    # Keeps the ATM menu running until logout
    while True:
        print("\n" + "=" * 45)
        print("                  ATM MENU")
        print("=" * 45)
        print(f"Welcome, {account['name']}")
        print("=" * 45)
        print("1. Balance Inquiry")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Logout")
        print("=" * 45)

        choice = input("Select an option: ").strip()

        # Balance Inquiry
        if choice == "1":
            balance_inquiry(account)

        # Withdraw Cash
        elif choice == "2":
            withdraw_cash(account)

            if not another_transaction():
                print("\nLogging Out...")
                print("Thank you for using Python ATM.")
                return

        # Deposit Cash
        elif choice == "3":
            deposit_cash(account)

            if not another_transaction():
                print("\nLogging Out...")
                print("Thank you for using Python ATM.")
                return

        # Transfer Money
        elif choice == "4":
            transfer_money(card_number, account)

            if not another_transaction():
                print("\nLogging Out...")
                print("Thank you for using Python ATM.")
                return

        # Transaction History
        elif choice == "5":
            transaction_history(account)

        # Logout
        elif choice == "6":
            print("\nLogging Out...")
            print("Thank you for using Python ATM.")
            return

        else:
            print("\nInvalid option. Please select 1-6.")

# Main program
def main():
    print("=" * 45)
    print("          PYTHON ATM SIMULATION")
    print("=" * 45)

    # Keeps the program running so another user can log in
    while True:
        card_number = login()

        # Open the ATM menu if login is successful
        if card_number is not None:
            atm_menu(card_number)

# Starts the program
main()
