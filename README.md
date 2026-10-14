# Python ATM Simulation

A beginner-friendly **ATM Simulation System built with Python**. This project simulates the basic functions of an automated teller machine (ATM), allowing users to log in using a bank card number and PIN, manage their account balance, perform financial transactions, and view their transaction history.

The program uses Python dictionaries to store pre-saved account information and transaction records while demonstrating important programming concepts such as functions, loops, conditional statements, exception handling, and data management.

## Features

### 1. Account Login and Authentication
- Supports multiple pre-saved bank accounts.
- Requires a 16-digit card number and a 4-digit PIN.
- Checks whether the entered card number exists.
- Displays the account holder's name after successful login.
- Allows a maximum of three incorrect PIN attempts.
- Automatically locks the account after three incorrect PIN attempts.

### 2. Card Recovery System
- Allows users to recover a locked card by verifying their identity.
- Uses the last four digits of the user's stored PhilSys Card Number (PCN).
- Allows a maximum of three PCN verification attempts.
- Unlocks the account after successful verification.
- Restricts card recovery to one successful use per account.
- Instructs users to visit their bank if recovery is unavailable or unsuccessful.

### 3. Balance Inquiry
- Displays the account holder's name.
- Shows the current account balance in Philippine pesos (PHP).
- Updates the displayed balance after successful transactions.

### 4. Cash Withdrawal
- Allows users to withdraw money from their accounts.
- Checks whether the entered amount is greater than zero.
- Prevents withdrawals that exceed the available balance.
- Deducts the withdrawal amount from the account balance.
- Generates a transaction number and displays a receipt after a successful withdrawal.

### 5. Cash Deposit
- Allows users to deposit money into their accounts.
- Rejects amounts that are zero or negative.
- Adds the deposit amount to the account balance.
- Records successful deposits in the transaction history.
- Generates a receipt showing the updated balance.

### 6. Money Transfer
- Allows users to transfer money between registered accounts.
- Checks whether the recipient's account exists.
- Prevents transfers to the sender's own account.
- Validates the transfer amount and available balance.
- Deducts money from the sender and adds it to the recipient.
- Records the transfer in both accounts' transaction histories.
- Generates a receipt for the sender.

### 7. Transaction History
- Displays the account's previous transactions during the current program session.
- Shows the transaction number, type, amount, date, time, and additional details.
- Records withdrawals, deposits, sent transfers, and received transfers.
- Displays a message when no transactions have been made.

### 8. Transaction Receipts
- Generates a receipt after successful withdrawals, deposits, and money transfers.
- Displays the transaction date and time.
- Includes the transaction ID, account holder, transaction type, and amount.
- Shows additional transaction details when applicable.
- Displays the remaining account balance.

### 9. Unique Transaction Numbers
- Generates transaction IDs using the `ATM` prefix.
- Starts the transaction counter at 1000, making the first generated transaction ID `ATM1001`.
- Uses a shared transaction counter to assign sequential IDs to transactions during the program session.

### 10. Interactive ATM Menu
The system provides the following menu options:

1. Balance Inquiry
2. Withdraw Cash
3. Deposit Cash
4. Transfer Money
5. Transaction History
6. Logout

Users can choose an operation, perform transactions, and log out when finished.

### 11. Input Validation and Error Handling
- Rejects invalid menu selections.
- Checks transaction amounts before processing them.
- Uses `try-except` statements to handle non-numeric transaction inputs.
- Prevents transactions involving insufficient balances.
- Provides messages to guide users when an operation cannot be completed.

## Technologies Used

- **Python** — Main programming language.
- **datetime** — Retrieves the current date and time for transaction records and receipts.
- **Dictionaries** — Store account information, balances, PINs, recovery status, and transaction histories.
- **Lists** — Store transaction records for each account.
- **Functions** — Organize the program into separate operations.
- **Loops** — Keep the login system, ATM menu, and input prompts running when needed.
- **Conditional Statements** — Validate user choices, account status, PINs, and transaction requirements.
- **Exception Handling** — Handles invalid numeric inputs using `try-except` statements.

## How to Run the Program

### Prerequisites
- Python 3 installed on your computer.
- A code editor such as PyCharm or Visual Studio Code.

### Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace the URL with your actual GitHub repository link.

**2. Open the project folder**

Open the downloaded project in PyCharm, Visual Studio Code, or another Python editor.

**3. Run the program**

Save the Python code in a file such as `main.py`, then run:

```bash
python main.py
```

No external Python packages are required because the program uses Python's built-in `datetime` module.

## Sample Account Information

The program includes four pre-saved accounts for testing.

| Account Holder | Initial Balance |
|---|---:|
| Ron Ivan Baniqued | PHP 10,000.00 |
| Yzekiel Zachary Nahil | PHP 15,000.00 |
| Jose Manuel Navoa | PHP 20,000.00 |
| Justin Rafael Tengco | PHP 1,000.00 |

The card numbers, PINs, and PCN verification digits are defined directly in the Python source code.

**Note:** Refer to the `accounts` dictionary in `main.py` for the exact test credentials. These are sample credentials for a simulation and should not be used for real financial accounts.

## Program Structure

The current implementation is contained in a single Python file.

| Function | Purpose |
|---|---|
| `login()` | Authenticates users and manages failed PIN attempts. |
| `recover_card(account)` | Verifies the user's PCN and unlocks an eligible locked card. |
| `get_transaction_number()` | Generates sequential transaction IDs. |
| `show_receipt()` | Displays transaction receipts. |
| `add_transaction()` | Saves transaction details to an account's history. |
| `balance_inquiry(account)` | Displays the current account balance. |
| `withdraw_cash(account)` | Processes cash withdrawals. |
| `deposit_cash(account)` | Processes cash deposits. |
| `transfer_money(sender_card, sender_account)` | Transfers money between accounts. |
| `transaction_history(account)` | Displays recorded transactions. |
| `another_transaction()` | Asks whether the user wants to continue after a financial transaction. |
| `atm_menu(card_number)` | Displays and manages the main ATM menu. |
| `main()` | Starts the program and manages the login loop. |

## Programming Concepts Demonstrated

This project demonstrates the following fundamental Python concepts:

- **Functions:** Each major operation is organized into a function.
- **Variables:** Store account details, user inputs, transaction amounts, and other values.
- **Dictionaries:** Organize account information using keys and values.
- **Lists:** Store transaction records.
- **While Loops:** Repeat login attempts, menu operations, and input prompts.
- **For Loops:** Iterate through transaction history records.
- **If-Elif-Else Statements:** Make decisions based on user input and account conditions.
- **Nested Conditional Statements:** Check additional conditions within an existing decision.
- **Return Statements:** Send results back to the calling function or end a function.
- **Global Variables:** Maintain a shared transaction counter.
- **Exception Handling:** Prevent invalid numeric inputs from crashing transaction functions.
- **String Formatting:** Display currency values and receipt details clearly.
- **Date and Time Handling:** Record when transactions occur.

## Scope and Limitations

### Scope
The project focuses on simulating common ATM operations in a terminal environment. It demonstrates basic authentication, account balance management, transfers between pre-saved accounts, transaction records, receipt generation, and a simple card recovery process.

### Limitations
- Account information is stored in a Python dictionary rather than a database.
- There is no registration feature for creating new accounts.
- Account balances and transaction histories are stored in memory and reset when the program restarts.
- The system does not connect to an actual bank or payment network.
- Transaction records are not permanently saved to a file or database.
- Card numbers, PINs, and PCN verification digits are defined directly in the source code.
- The recovery process is a classroom simulation and does not provide real banking-grade identity verification.
- The system does not include actual cash dispensing, physical card reading, or hardware integration.

## Future Improvements

Possible enhancements for future versions include:

- Integrating SQLite or another database for persistent account storage.
- Adding account registration and account management.
- Saving transaction histories permanently.
- Improving authentication and securely storing PINs.
- Adding daily withdrawal limits and transaction limits.
- Creating a graphical user interface using Tkinter or CustomTkinter.
- Adding printable or downloadable transaction receipts.
- Implementing more comprehensive validation for card numbers, PINs, and monetary amounts.

## Disclaimer

This project is intended for **educational purposes only**. It demonstrates basic ATM operations and Python programming concepts. It is not a real banking application and should not be used to store actual financial information or process real transactions.

## Author

**Jose Manuel Navoa**

Information Technology Student

Built as a Python programming project to practice functions, data structures, loops, conditional statements, exception handling, and basic transaction processing.
