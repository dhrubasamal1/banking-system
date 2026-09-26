def depositor(accounts, account_number):

# using try except here because converting the input to float() will give an error, if the user types anything else instead of a number.

    while True:
        try:
            amount = float(input("Enter amount to deposit: INR"))
            break
        except ValueError:
            print("Amount is invalid. Please enter a number.")

    if amount > 0:
        accounts[account_number]["balance"] += amount
        print("Transaction Successful!")
        print("Deposited: INR", format(amount, ".2f"))
        print("Current balance for account", account_number, "is: INR", format(accounts[account_number]["balance"], ".2f"))
    else:
        print("Amount is invalid. Please enter a positive number.")

def withdrawler(accounts, account_number):
    while True:
        try:
            amount = float(input("Enter amount to withdraw: INR"))
            break
        except ValueError:
            print("Amount is invalid. Please enter a number.")

    if amount > 0:
        if amount <= accounts[account_number]["balance"]:
            accounts[account_number]["balance"] -= amount
            print("Transaction Successful!")
            print("Withdrew: INR", format(amount, ".2f"))
            print("Current balance for account", account_number, "is: INR", format(accounts[account_number]["balance"], ".2f"))
        else:
            print("Transaction failed: Insufficient funds.")
    else:
        print("Amount is invalid. Please enter a positive number.")

def balance_checker(accounts, account_number):
    print("Current balance for account number", account_number, "is: INR", format(accounts[account_number]["balance"], ".2f"))