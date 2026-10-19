# Python ATM Simulation

A beginner-friendly **ATM Simulation System built with Python**. This project simulates the basic functions of an automated teller machine (ATM), allowing users to log in using a bank card number and PIN, manage their account balance, perform financial transactions, and view their transaction history.

The program uses Python dictionaries to store pre-saved account information and transaction records while demonstrating important programming concepts such as functions, loops, conditional statements, return statements, exception handling, and data management.

## Features

### 1. Account Login and Authentication
- Supports multiple pre-saved bank accounts.
- Requires a 16-digit card number and a 4-digit PIN.
- Checks whether the entered card number exists in the system.
- Displays the account holder's name after successful login.
- Allows a maximum of three incorrect PIN attempts.
- Automatically locks the account after three incorrect PIN attempts.
- Prevents users from proceeding with normal login while their account is locked.

### 2. Card Recovery System
- Allows users to attempt recovery of a locked card by verifying their identity.
- Uses the last four digits of the user's stored PhilSys Card Number (PCN).
- Allows a maximum of three PCN verification attempts.
- Unlocks the account after successful verification when recovery is available.
- Restricts successful card recovery to one use per account.
- Prevents repeated recovery attempts after the recovery allowance has been used.
- Allows users to decline the recovery option.
- Instructs users to visit their bank if recovery is unavailable or unsuccessful.

### 3. Balance Inquiry
- Displays the account holder's name.
- Shows the current account balance in Philippine pesos (PHP).
- Reflects changes made by successful deposits, withdrawals, and transfers.
- Allows users to check their balance through the main ATM menu.

### 4. Cash Withdrawal
- Allows users to withdraw money from their accounts.
- Checks whether the entered amount is greater than zero.
- Prevents withdrawals that exceed the available balance.
- Handles invalid numeric inputs.
- Deducts the withdrawal amount from the account balance after validation.
- Records successful withdrawals in the transaction history.
- Generates a unique transaction number.
- Displays a transaction receipt containing the transaction details and updated balance.

### 5. Cash Deposit
- Allows users to deposit money into their accounts.
- Rejects amounts that are zero or negative.
- Handles invalid numeric inputs.
- Adds the deposit amount to the account balance after validation.
- Records successful deposits in the transaction history.
- Generates a unique transaction number.
- Displays a receipt showing the transaction details and updated balance.

### 6. Money Transfer
- Allows users to transfer money between registered accounts.
- Checks whether the recipient's account exists.
- Prevents users from transferring money to their own account.
- Validates the transfer amount.
- Prevents transfers that exceed the sender's available balance.
- Deducts the transfer amount from the sender's balance.
- Adds the transferred amount to the recipient's balance.
- Records the outgoing transfer in the sender's transaction history.
- Records the incoming transfer in the recipient's transaction history.
- Generates a transaction number for the transfer.
- Displays a receipt for the sender with relevant transaction details.

### 7. Transaction History
- Displays the account's recorded transactions during the current program session.
- Shows the transaction number, transaction type, amount, date, time, and additional details when available.
- Records successful withdrawals, deposits, outgoing transfers, and incoming transfers.
- Uses a list of dictionaries to organize transaction records.
- Displays a message when the account has no recorded transactions.
- Allows users to review their transactions through the main ATM menu.

### 8. Transaction Receipts
- Generates receipts after successful withdrawals, deposits, and money transfers.
- Displays the transaction date and time.
- Includes the transaction ID, account holder, transaction type, and amount.
- Shows additional transaction details when applicable.
- Displays the remaining account balance.
- Uses a reusable receipt function to keep receipt formatting consistent.

### 9. Unique Transaction Numbers
- Generates transaction IDs using the `ATM` prefix.
- Starts the transaction counter at `1000`, making the first generated transaction ID `ATM1001`.
- Uses a shared transaction counter to assign sequential IDs to transactions during the program session.
- Uses a transaction-recording function to associate transaction details with the generated ID.

### 10. Interactive ATM Menu
The system provides the following menu options:

1. Balance Inquiry
2. Withdraw Cash
3. Deposit Cash
4. Transfer Money
5. Transaction History
6. Logout

Users can select an operation, complete the requested action, and return to the main menu when appropriate.

The menu uses a loop to keep displaying the available options until the user logs out or the current session ends.

### 11. Another Transaction Option
- Asks users whether they would like to perform another transaction after completing a withdrawal, deposit, or transfer.
- Returns users to the ATM menu when they choose to continue.
- Logs users out when they choose not to perform another transaction.
- Uses a separate function to handle the user's decision.
- Prevents users from having to restart the program just to finish their current ATM session.

### 12. Logout and Session Control
- Allows users to exit their current ATM session through the Logout menu option.
- Ends the current account session when the user chooses not to continue after a financial transaction.
- Returns control to the main program so another login attempt can be made.
- Uses return values to communicate whether login and menu operations should continue or stop.

### 13. Input Validation and Error Handling
- Rejects invalid menu selections.
- Validates transaction amounts before processing them.
- Uses `try-except` statements to handle non-numeric transaction inputs.
- Prevents transactions involving insufficient balances.
- Checks recipient account details before completing transfers.
- Uses conditional statements to determine whether an operation can proceed.
- Provides messages to guide users when an operation cannot be completed.

## Technologies Used

- **Python** — Main programming language.
- **datetime** — Retrieves the current date and time for transaction records and receipts.
- **Dictionaries** — Store account information, balances, PINs, recovery status, and transaction details.
- **Lists** — Store transaction records for each account.
- **Functions** — Organize the program into separate operations.
- **While Loops** — Keep the login system, ATM menu, and input prompts running when needed.
- **For Loops** — Iterate through transaction history records.
- **Conditional Statements** — Validate user choices, account status, PINs, and transaction requirements.
- **Return Statements** — Send results back to calling functions or stop the current operation.
- **Exception Handling** — Handle invalid numeric inputs using `try-except` statements.

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
| `login()` | Authenticates users, checks account status, and manages failed PIN attempts. |
| `recover_card(account)` | Verifies the user's PCN and handles eligible locked-card recovery. |
| `get_transaction_number()` | Generates sequential transaction IDs. |
| `show_receipt()` | Displays transaction receipts with relevant details and the updated balance. |
| `add_transaction()` | Adds transaction details to an account's history. |
| `balance_inquiry(account)` | Displays the current account balance. |
| `withdraw_cash(account)` | Validates and processes cash withdrawals. |
| `deposit_cash(account)` | Validates and processes cash deposits. |
| `transfer_money(sender_card, sender_account)` | Transfers money between registered accounts and records the transaction for both accounts. |
| `transaction_history(account)` | Displays recorded transactions. |
| `another_transaction()` | Asks whether the user wants to continue after a financial transaction. |
| `atm_menu(card_number)` | Displays and manages the main ATM menu and its operations. |
| `main()` | Starts the program and manages the login loop. |

## Programming Concepts Demonstrated

This project demonstrates the following fundamental Python concepts:

- **Functions:** Organize each major operation into a separate function.
- **Parameters and Arguments:** Pass account information and transaction details to functions.
- **Variables:** Store account details, user inputs, transaction amounts, and other values.
- **Dictionaries:** Organize account information using keys and values.
- **Lists:** Store transaction records for each account.
- **While Loops:** Repeat login attempts, menu operations, and input prompts.
- **For Loops:** Iterate through transaction history records.
- **If-Elif-Else Statements:** Make decisions based on user input and account conditions.
- **Nested Conditional Statements:** Check additional conditions within an existing decision.
- **Return Statements:** Send results back to the calling function or end a function's execution.
- **Boolean Values:** Use `True` and `False` to represent outcomes such as recovery success or failure.
- **Global Variables:** Maintain a shared transaction counter.
- **Exception Handling:** Prevent invalid numeric inputs from crashing transaction functions.
- **String Formatting:** Display currency values and receipt details clearly.
- **Date and Time Handling:** Record when transactions occur.
- **Basic Data Management:** Update account balances and maintain transaction records during a program session.

## Scope and Limitations

### Scope

The project focuses on simulating common ATM operations in a terminal environment. It demonstrates basic authentication, account balance management, cash withdrawals, deposits, transfers between pre-saved accounts, transaction history, receipt generation, card recovery, and session management.

The program is intended to demonstrate beginner-level Python programming concepts through a practical ATM scenario.

### Limitations

- Account information is stored in a Python dictionary rather than a database.
- There is no registration feature for creating new accounts.
- Account balances, account lock status, recovery status, and transaction histories are stored in memory and reset when the program restarts.
- The system does not connect to an actual bank or payment network.
- Transaction records are not permanently saved to a file or database.
- Transaction IDs restart from the initial counter whenever the program starts.
- Card numbers, PINs, and PCN verification digits are defined directly in the source code.
- The recovery process is a classroom simulation and does not provide real banking-grade identity verification.
- The system does not include actual cash dispensing, physical card reading, or hardware integration.
- The program is terminal-based and does not currently provide a graphical user interface.

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
- Adding a transaction search or filtering feature.
- Allowing users to view their account information through a dedicated menu option.
- Improving account recovery with more secure verification procedures.

## Disclaimer

This project is intended for **educational purposes only**. It demonstrates basic ATM operations and Python programming concepts. It is not a real banking application and should not be used to store actual financial information or process real transactions.

## Author

**Jose Manuel Navoa**

Information Technology Student

Built as a Python programming project to practice functions, parameters, arguments, data structures, loops, conditional statements, return statements, exception handling, and basic transaction processing.
