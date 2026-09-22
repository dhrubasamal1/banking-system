# PROJECT REPORT
## Simple Banking System

### Submitted By
Name: Dhruba Charan Samal

Course: B.TECH CSE (Core)

College: VIT Bhopal

Year: 2026–2030

## Here's What I Built

So this is a very simple CLI banking system I built in Python basically a mini oversimplified simulation of working of banking system.
## What My Project Can Do

- Log in to an existing account using a 4 digit account number and PIN
- Create a new account with a validated 4 digit account number and PIN
- Deposit and Withdraw money into the bank account, with a overdraft check
- Check your current balance anytime
- Temporarily Locks you out after 3 wrong PIN attempts
- Handles bad input gracefully if you type letters where a number should go, it just asks again instead of crashing

## Information

- Language: Python
- No external libraries or dependencies the project uses only the Python Standard Library
- No database, server, or additional configuration of any kind is required
- Runs from: any terminal like Command Prompt, PowerShell, or macOS/Linux Terminal
- Data storage: everything lives in memory for the session

## How I Organized Everything (Folder Structure)

```
banking-system/
├── README.md
├── LICENSE
└── main.py
└── Folder Structure
└── Project Report
```

Kept it simple on purpose one file, no extra folders, since the whole thing really comes down to one function handling the login, menu, and transactions.


## What I Learned

Building this helped me in application of a lot of the python concepts in a practical way figuring out how to nested loops and conditionals for a multi-step flow like login → menu → transaction, and thinking through edge cases (what if the account doesn't exist, what if the PIN's wrong three times in a row, what if someone types text where a number should go). Learnt why dictionaries are actually useful for organizing real data.

## Future Ideas

- Saving account data to a file so it doesn't reset every time the program restarts (Persistent Storage)
- Restructuring the code using classes and objects once I learn about OOP concept
- Stronger validation on things like transaction amounts
- Introducing a simple transaction history log

## Final Words

This was my first Python project that feels like a real mini application. It's simple, but it works perfectly as intended.

Thank you for checking it out!
Made with lots of coffee and zero external libraries
Dhruba
VIT Bhopal
