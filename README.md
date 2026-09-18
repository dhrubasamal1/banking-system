# Simple Banking System

A command-line banking system written in Python that simulates core banking operations — account creation, PIN-based login, deposits, withdrawals, and balance checks — with overdraft protection and a 3-attempt PIN lockout.

## Overview

The program runs as an interactive terminal session. On start, you either log into one of two pre-seeded demo accounts or create a new one on the fly by entering an account number that doesn't exist yet. From there you can deposit, withdraw, check your balance, or log out and switch accounts, all through a simple numbered menu.

**Note on data storage:** All account data (balances, PINs, and any new accounts you create) is held in memory only, for the duration of a single run. Nothing is written to disk, so restarting the program resets everything back to the two demo accounts below.

## Prerequisites

- Python 3.x installed on your system (tested on Python 3.14.6)
- No external libraries or dependencies — the project uses only the Python Standard Library
- No database, server, or additional configuration of any kind is required

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

There is no dependency installation step and no configuration file to edit — the project runs as-is once cloned.

## Running the Project

Start the program from the project directory with:

```bash
python3 main.py
```

(On Windows, or if `python3` isn't recognized, use `python main.py` instead.)

## Usage

Once running, you'll see:

```
=== Welcome to People's Bank ===
Enter your Account Number (or type 'E' to exit bank):
```

**Option A — Log into a demo account**

Two accounts are pre-loaded for testing:

| Account Number | PIN  | Starting Balance |
|-----------------|------|-------------------|
| 1001            | 1234 | ₹5000.00          |
| 1002            | 5678 | ₹1500.00          |

Enter one of the account numbers above, then the matching PIN. Three incorrect PIN attempts will lock you out of that login and return you to the account-number prompt.

**Option B — Create a new account**

Enter any account number that isn't `1001` or `1002`, and you'll be prompted to set a 4-digit PIN. The account is created immediately with a ₹0.00 balance.

**Once logged in**, you'll see the account menu:

```
--- Account Main Menu ---
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Log Out
```

- **Deposit / Withdraw**: enter a positive amount when prompted. Withdrawals are blocked if they'd exceed your current balance.
- **Check Balance**: prints your current balance.
- **Log Out**: returns you to the account-number prompt so you can log into a different account.

After a deposit, withdrawal, or balance check, press **Enter** to return to the menu, or type **L** to log out.

To exit the program entirely, type **E** at the account-number prompt.

## Known Limitations

- No persistent storage — all data resets on restart (see note above).
- Deposit/withdrawal amounts must be entered as valid numbers; non-numeric input will raise an error and stop the program.

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
