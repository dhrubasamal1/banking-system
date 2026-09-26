# PROJECT REPORT
## Simple Banking System

### Submitted By
Name: Dhruba Charan Samal

Registration Number: 26BCE10263

Course: B.TECH CSE (Core)

College: VIT Bhopal

Year: 2026–2030

## Here's What I Built

I have created a simple banking system written in Python that simulates basic banking operations like new account creation, PIN based login for existing accounts, deposits, withdrawals, and balance checks with overdraft protection and a 3 attempt PIN lockout.

## What My Project Can Do

- Log in to an existing testing accounts using a 10 digit account number and PIN.
- Automatically creates a new 10 digit unique account number using the random library and user will be able to create a PIN manually.
- Deposit or Withdraw money into the bank account, with a overdraft check.
- Check your current balance anytime.
- Temporarily Locks you out after 3 wrong PIN attempts.
- Handles bad input if you type letters where a number should go, it just asks again instead of crashing.

## Information

- Language: Python.
- No external libraries or dependencies the project uses only the Python Standard Library.
- No database, server, or additional configuration of any kind is required.
- Runs from: any terminal like Command Prompt, PowerShell, or macOS/Linux Terminal.
- Data storage: everything lives in memory for the session.

## How I Organized Everything (Folder Structure)

```
banking-system/
├── README.md
├── LICENSE
└── main.py
└── account.py
└── transactions.py
└── Project Report.md
└── .gitignore
```


## What I Learned

Building this helped me in application of a lot of the python concepts in a practical way figuring out how to use nested loops and conditionals for a multi-step flow like login, menu, transaction, and thinking through edge cases (what if the account doesn't exist, what if the wron PIN is entered, what if someone types text where a number should go). Learnt why dictionaries are actually useful for organizing real data.

## Future Ideas

- Saving account data to a file so it doesn't reset every time the program restarts.
- Stronger validation on things like transaction amounts.
- Introducing a simple transaction history log.

## Final Words

This was my first Python project that feels like I made a real banking application.

Thank you for checking it out!
Made with lots of coffee and zero external libraries

Dhruba

VIT Bhopal
