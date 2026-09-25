import random

def account_number_digit_checker(account_number):
    return account_number.isdigit() and len(account_number) == 10

def pin_digits_checker(pin):
    if len(pin) == 4 and pin.isdigit():
        return True
    return False

def generate_account_number(accounts):
    account_number = str(random.randint(1000000000, 9999999999))
    while account_number in accounts:
        account_number = str(random.randint(1000000000, 9999999999))
    return account_number

def create_account(accounts, account_number, pin):
    accounts[account_number] = {"pin": pin, "balance": 0.0}

def authenticator(accounts, account_number):
    attempts = 0
    while True:
        pin = input("Enter your 4 digit PIN: ")

        if pin == accounts[account_number]["pin"]:
            print("Login successful. Welcome back!")
            return True
        else:
            attempts += 1
            if attempts == 3:
                print("Account Locked: Too many failed attempts.")
                return False

            print("PIN is Incorrect. Remaining Attempts:", 3 - attempts)