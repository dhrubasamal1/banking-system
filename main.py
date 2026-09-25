from account import generate_account_number, create_account, authenticator, account_number_digit_checker, pin_digits_checker
from transactions import depositor, withdrawler, balance_checker

def banking_system():
    accounts = {
        "1000000001": {"pin": "1234", "balance": 5000.0},
        "1000000002": {"pin": "5678", "balance": 1500.0}
    }

    #login
    while True:
        print("Welcome to People's Bank")
        customer_type = input("If you are an existing customer [type E]. To create a new account [type N] (or [type X] to exit): ").upper()

        if customer_type == 'X':
            print("Thank you for visiting People's Bank.")
            break

        if customer_type not in ['E', 'N']:
            print("Invalid choice. If you are an existing customer [type E]. To create a new account [type N] (or [type X] to exit): ")
            continue

        while True:
            if customer_type == 'E':
                account_number = input("Enter your 10 Digit account number: ")
            else:
                account_number = generate_account_number(accounts)
                print("Successfully created your new account. Your new 10 digit account number is:", account_number)
                break

            if not account_number_digit_checker(account_number):
                print("Invalid account number. The account number must be of 10 digits.")
                continue

            if customer_type == 'E' and account_number not in accounts:
                print("Account not found. Please check your account number and try again.")
                continue

            break

        #PIN verification
        if account_number in accounts:
            authentication_handler = authenticator(accounts, account_number)
            if not authentication_handler:
                continue

        #account creation
        else:
            while True:
                new_pin = input("Create a 4 digit PIN for your new account: ")
                if pin_digits_checker(new_pin):
                    break
                print("Invalid PIN. It must be exactly 4 digits.")

            create_account(accounts, account_number, new_pin)
            print("New account created successfully. Your starting balance is INR 0.00")

        #menu
        while True:
            print("Account Main Menu")
            print("1.Deposit Money")
            print("2.Withdraw Money")
            print("3.Check Balance")
            print("4.Log Out")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                depositor(accounts, account_number)
            elif choice == '2':
                withdrawler(accounts, account_number)
            elif choice == '3':
                balance_checker(accounts, account_number)
            elif choice == '4':
                print("Logging out...", account_number,)
                break
            else:
                print("Invalid choice. Please select a valid option from the menu.")

            if choice in ['1', '2', '3']:
                continue_choice = input("Press 'Enter' to return to the Main Menu, or type 'L' to log out: ").upper()
                if continue_choice == 'L':
                    print("Logging out...")
                    break

banking_system()