import random

#code for account number digit check
def account_number_digit_checker(account_number):
    return account_number.isdigit() and len(account_number) == 10

#code for PIN digit check
def pin_digits_checker(pin):
    if len(pin) == 4 and pin.isdigit():
        return True
    return False

#code for account number generator using the random module
def generate_account_number(accounts):
    account_number = str(random.randint(1000000000, 9999999999))
    while account_number in accounts:
        account_number = str(random.randint(1000000000, 9999999999))
    return account_number

#code for account creation
def create_account(accounts, account_number, pin):
    accounts[account_number] = {"pin": pin, "balance": 0.0}

#code for account information verification
def authenticator(accounts, account_number):
    attempts = 0
    while True:
        pin = input("Enter your 4 digit PIN: ")

        if pin == accounts[account_number]["pin"]:
            print("Login Successful. Welcome Back!")
            return True
        else:
            attempts += 1
            if attempts == 3:
                print("Account Locked: Too many failed attempts.")
                return False

            print("PIN is Incorrect. Remaining Attempts:", 3 - attempts)