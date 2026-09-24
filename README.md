# Simple Banking System

A simple banking system written in Python that simulates basic banking operations like new account creation, PIN based login for existing accounts, deposits, withdrawals, and balance checks with overdraft protection and a 3 attempt PIN lockout.

## Overview

The program runs as an interactive terminal session. 
On start, you choose whether you're an existing customer logging in, a new customer opening an account, or you'd like to exit. 
From there you can deposit, withdraw, check your balance, or log out and return to the start, all through a simple numbered menu.

**Note on data storage:** All account data is held in memory only, for the duration of a single run. Nothing is written to disk, so restarting the program resets everything back to the two demo accounts below.

## Prerequisites

- Python 3.1 (or above) installed on your system.
- No external libraries or dependencies the project uses only the Python Standard Library.
- No database, server, or additional configuration of any kind is required.

## Installation & Setup

1. Open a terminal (Command Prompt, PowerShell, or macOS/Linux Terminal).
2. Clone the repository:
   ```bash
   git clone https://github.com/dhrubasamal1/banking-system.git
   ```
3. Move into the project directory:
   ```bash
   cd banking-system
   ```

There is no dependency installation step and no configuration file to edit, the project runs as is once cloned.

## Running the Project

Start the program from the project directory with:

```bash
python3 main.py
```

(If `python3` isn't recognized, use `python main.py` instead.)

## Usage

Once running, you'll be asked:

```
Welcome to People's Bank
If you are an existing customer [type E]. To create a new account [type N] (or [type X] to exit):
```

**Type `E` - Log into an existing account**

You'll be asked for a 10 digit account number, then the matching PIN. Two accounts are pre-loaded for testing:

| Account Number | PIN  | Starting Balance |
|-----------------|------|-------------------|
| 1000000001            | 1234 | ₹5000.00          |
| 1000000002            | 5678 | ₹1500.00          |

If the account number isn't exactly 10 digits, or doesn't exist, you'll be asked to try again. Three incorrect PIN attempts locks that login attempt and returns you to the start.

**Type `N` - Create a new account**

Once you choose to create a new account, a new unique 10 digit account number will automatically be created using the python random module, then the user has to set up a PIN for the newly created account. The account is created immediately with a ₹0.00 balance and you're taken straight into it — no separate login step needed right after creating it.

**Type `X` - Exit the program**

Ends the session immediately from the start screen.

**Once logged in or after creating an account**, you'll see the account menu:

```
Account Main Menu
1.Deposit Money
2.Withdraw Money
3.Check Balance
4.Log Out
```

- **Deposit / Withdraw**: enter a positive amount (Withdrawals are blocked if withdrawal amount is greater than your current balance).
- **Check Balance**: prints your current balance.
- **Log Out**: returns you to the start screen (E / N / X) so you can log into a different account, create another, or exit.

After a deposit, withdrawal, or balance check, press **Enter** to return to the menu, or type **L** to log out.

## Known Limitations

- All data resets on restart.
