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
    }
}


# Starting transaction number
transaction_number = 1000


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

        # Check PIN format
        if len(pin) != 4 or not pin.isdigit():
            attempts -= 1

            print("\nInvalid PIN format.")

            if attempts > 0:
                print("Enter exactly 4 digits.")
                print(f"You have {attempts} attempt(s) remaining.")
                continue

        # Check if the PIN is correct
        elif account["pin"] == pin:
            print("\nLogin successful!")
            print(f"Welcome, {account['name']}!")
            return card_number

        else:
            attempts -= 1
            print("\nIncorrect PIN.")

            if attempts > 0:
                print(f"You have {attempts} attempt(s) remaining.")
                continue

        # Lock the account after 3 failed attempts
        account["locked"] = True

        print("\nYou have reached the maximum number of PIN attempts.")
        print("Your card has been locked.")

        if account["recovery_used"]:
            print("Card recovery has already been used.")
            print("Please visit your bank to recover your card.")
            return None

        print("\nWould you like to proceed with card recovery?")
        print("1. Yes")
        print("2. No")

        while True:
            recovery_choice = input("Enter your choice: ").strip()

            if recovery_choice == "1":
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
    print("Your card has been locked due to")
    print("too many incorrect PIN attempts.")
    print()
    print("Verify your identity using your PCN.")
    print("Enter the last 4 digits of your PCN.")
    print("=" * 45)

    attempts = 3

    while attempts > 0:
        pcn = input("\nEnter last 4 digits of your PCN: ").strip()

        # Validate PCN format
        if len(pcn) != 4 or not pcn.isdigit():
            print("Invalid input. Please enter exactly 4 digits.")
            continue

        # Check if the PCN is correct
        if pcn == account["pcn"]:
            account["locked"] = False
            account["recovery_used"] = True

            print("\nPCN verification successful!")
            print("Your identity has been verified.")
            print("Your card has been successfully recovered.")
            print("Card recovery can only be used once.")
            print("=" * 45)

            return True

        attempts -= 1
        print("\nIncorrect PCN.")

        if attempts > 0:
            print(f"You have {attempts} attempt(s) remaining.")
        else:
            print("You have reached the maximum number")
            print("of card recovery attempts.")
            print("Your card is still locked.")
            print("Please visit your bank to recover your card.")

    return False


# Creates a unique transaction number
def get_transaction_number():
    global transaction_number
    transaction_number += 1
    return f"ATM{transaction_number}"


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


# Displays the receipt after a transaction
def show_receipt(
    transaction_type,
    amount,
    transaction_number,
    account_name,
    balance,
    extra_info=""
):
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

        # Validate the amount
        if amount <= 0:
            print("\nPlease enter an amount greater than zero.")
            return

        if round(amount, 2) != amount:
            print("\nPlease enter an amount with no more than 2 decimal places.")
            return

        # Withdrawals must be in multiples of PHP 100
        if amount % 100 != 0:
            print("\nWithdrawals must be in multiples of PHP 100.")
            return

        # Check available balance
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

        # Validate the amount
        if amount <= 0:
            print("\nPlease enter an amount greater than zero.")
            return

        if round(amount, 2) != amount:
            print("\nPlease enter an amount with no more than 2 decimal places.")
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
    receiver_card = input(
        "Enter recipient's 16-digit card number: "
    ).strip()

    # Check if the recipient exists
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

        # Validate the amount
        if amount <= 0:
            print("\nPlease enter an amount greater than zero.")
            return

        if round(amount, 2) != amount:
            print("\nPlease enter an amount with no more than 2 decimal places.")
            return

        # Check the sender's balance
        if amount > sender_account["balance"]:
            print("\nInsufficient balance.")
            return

        # Confirm the transfer before moving money
        print("\nTRANSFER SUMMARY")
        print(f"Recipient: {receiver_account['name']}")
        print(f"Amount   : PHP {amount:,.2f}")

        confirmation = input(
            "Confirm transfer? (Y/N): "
        ).strip().lower()

        if confirmation != "y":
            print("\nTransfer cancelled. No money was transferred.")
            return

        # Remove money from the sender
        sender_account["balance"] -= amount

        # Add money to the recipient
        receiver_account["balance"] += amount

        # Create one transaction number
        transaction_id = get_transaction_number()

        # Save the transaction to the sender's history
        add_transaction(
            sender_account,
            "TRANSFER SENT",
            amount,
            transaction_id,
            f"To: {receiver_account['name']}"
        )

        # Save the transaction to the recipient's history
        add_transaction(
            receiver_account,
            "TRANSFER RECEIVED",
            amount,
            transaction_id,
            f"From: {sender_account['name']}"
        )

        print("\nTransfer successful!")

        # Display receipt for the sender
        show_receipt(
            "MONEY TRANSFER",
            amount
