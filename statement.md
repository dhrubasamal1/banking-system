## Problem Statement

Banking systems require the ability to access account securely and accurately.
This project addresses that problem, showing how a program can authenticate a user, maintain account state, this program solves the need for a lightweight, secure, and dependency free system to simulate banking system functioning  without relying on external modules and databases. 


## Scope of Project

The scope of this project is limited to creating a simple simulation of how banking system works that can perform banking operations. 
It covers the core banking loop: 
account creation, user authentication, and basic financial transactions.
All data is stored i -memory during runtime, meaning no local file storage is used. It is designed as a localized, session based demonstration.


## Target Users

- Students and educators needing a clean, dependency-free project to understand data structures like dictionaries and basic error handling.
- Developers who want a lightweight base app for an ATM or banking logic system to expand upon without configuring servers.


## High Level Features

- User Management: Handles new account creation with automated 10 digit account number generation and facilitates PIN based login for existing customers. The Program is also able to handle databases of multiple users.
- Transaction Processing: Manages financial operations by updating account balances through account deposits and withdrawals. 
- Account Monitoring: Allows users to read and check their current account balance or log out to return to the main menu. 
- Security: Implements a strict 3 attempt PIN lockout mechanism to prevent unauthorized access