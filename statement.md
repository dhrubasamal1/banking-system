## Problem Statement

Banking systems require the ability to access account securely and accurately.
This project addresses that problem, showing how a program can authenticate a user, maintain account state, this program solves the need for a lightweight, secure, and dependency free code. The most important requirement is being able to run on any OS without any external needs.

## Scope of Project

The scope of this project is limited to creating a simple simulation of how banking system works that can perform banking operations. 
It covers the core banking loop like - account creation, user authentication, and basic financial transactions.
All data is stored in memory during runtime, meaning no file storage is used. It is designed as a localized, session based demonstration.

## Overview

The program can run on CLI terminal. 
On start, you choose whether you are an existing customer logging in, a new customer opening an account, or you would like to exit. 
From there you can deposit, withdraw, check your balance, or log out and return to the main menu.

Note on data storage - All account data is held in memory only. Nothing is written to disk, so restarting the program resets everything back to the two demo accounts.


## Target Users

- Students and educators needing a clean, dependency free project to understand data structures like dictionaries and basic error handling.
- Developers who want a lightweight base app for an ATM or banking logic system to expand upon without configuring servers.

## High Level Features

- User Management: Handles new account creation with automated 10 digit account number generation and facilitates PIN based login for existing customers. The Program is also able to handle databases of multiple users.
- Robust Error Handling: Utilizes try except blocks to catch invalid inputs (like typing letters instead of amounts) so the program asks again instead of crashing.
- Account Monitoring: Allows users to read and check their current account balance or log out to return to the main menu. 
- Security: Implements a strict 3 attempt PIN lockout mechanism to prevent unauthorized access