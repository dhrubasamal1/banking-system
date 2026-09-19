def banking_system():
    accounts = {
        "1001": {"pin": "1234", "balance": 5000.0},
        "1002": {"pin": "5678", "balance": 1500.0}
    }
    
    #login menu 
    while True:
        print("--Welcome to People's Bank--")
        customer_type = input("If you are an existing customer [type E].To create a new account [type N] (or [type X] to exit): ").upper()

        if customer_type == 'X':
            print("Thank you for visiting People's Bank.")
            break

        if customer_type not in ['E', 'N']:
            print("Invalid choice. Please select E for existing customer or N for a new account.")
            continue

        if customer_type == 'E':
            account_num = input("Enter your 4 Digit Account Number: ")
        else:
            account_num = input("Type an 4 digit Account Number of your choice for your new account: ")

        if not account_num.isdigit() or len(account_num) != 4:
            print("Invalid account number. It must contain exactly 4 digits.")
            continue

        if customer_type == 'E':
            if account_num not in accounts:
                print("Account not found. Please check your account number and try again.")
                continue
        elif account_num in accounts:
                print("That account already exists. Please choose a different account number.")
                continue

        #login and PIN verification
        if account_num in accounts:
            attempts = 0
            auth_success = False
            
            while True:
                pin = input("Enter your 4-digit PIN: ")
                
                if pin == accounts[account_num]["pin"]:
                    print("Login successful. Welcome back!")
                    auth_success = True
                    break
                else:
                    attempts += 1
                    if attempts == 3:
                        print("ACCOUNT LOCKED: Too many failed attempts.")
                        break 
                        
                    print("Incorrect PIN. Attempts remaining:", 3 - attempts)

            if auth_success == False: 
                continue
                
        #account creation
        else:
            new_pin = input("Create a 4-digit PIN for your new account: ")
            accounts[account_num] = {"pin": new_pin, "balance": 0.0}
            print("New account created successfully. Your starting balance is ₹ 0.00")
            
            
        #dashboard
        while True:
            print("Account Main Menu")
            print("1.Deposit Money")
            print("2.Withdraw Money")
            print("3.Check Balance")
            print("4.Log Out")
            
            choice = input("Enter your choice (1-4): ") 
            
            #deposit
            if choice == '1':
                amount = float(input("Enter amount to deposit: ₹"))
                if amount > 0:
                    accounts[account_num]["balance"] += amount
                    print("Transaction Successful!")
                    print("Deposited: ₹", format(amount, ".2f"))
                    print("Current Balance for Account", account_num, "is: ₹", format(accounts[account_num]["balance"], ".2f"))
                    
                else:
                    print("Invalid amount. Please enter a positive number.")
                    
            #withdrawal
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount > 0:
                    if amount <= accounts[account_num]["balance"]:
                        accounts[account_num]["balance"] -= amount
                        print("Transaction Successful!")
                        print("Withdrew: ₹", format(amount, ".2f"))
                        print("Current Balance for Account", account_num, "is: ₹", format(accounts[account_num]["balance"], ".2f"))
                    else:
                        print("Transaction failed: Insufficient funds.")
                else:
                    print("Invalid amount. Please enter a positive number.")
                    
            #balance check
            elif choice == '3':
                print("Current Balance for Account", account_num, "is: ₹", format(accounts[account_num]["balance"], ".2f"))
                
            #logging out
            elif choice == '4':
                print("Logging out of account", account_num, "...")
                break 

            else:
                print("Invalid choice. Please select a valid option from the menu.")
                
            if choice in ['1', '2', '3']:
                continue_choice = input("Press 'Enter' to return to the Main Menu, or type 'L' to log out: ").upper()
                if continue_choice == 'L':
                    print("Logging out...")
                    break


banking_system()
