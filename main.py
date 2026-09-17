def banking_system():
    # Dictionary to store both the PIN and the balance
    accounts = {
        "1001": {"pin": "1234", "balance": 5000.0},
        "1002": {"pin": "5678", "balance": 1500.0}
    }
    
    # OUTER LOOP: The Login Screen
    while True:
        print("\n=== Welcome to People's Bank ===")
        account_num = input("Enter your Account Number (or type 'E' to exit bank): ")
        
        if account_num.upper() == 'E':
            print("Thank you for visiting People's Bank. Goodbye!")
            break
            
        # 1. LOGIN & PIN VERIFICATION
        if account_num in accounts:
            attempts = 0
            auth_success = False
            
            # The PIN verification loop
            while True:
                pin = input("Enter your 4-digit PIN: ")
                
                if pin == accounts[account_num]["pin"]:
                    print("\nLogin successful. Welcome back!")
                    auth_success = True
                    break
                else:
                    attempts += 1
                    if attempts == 3:
                        # 3 failed attempts: Break keyword locks them out
                        print("\nACCOUNT LOCKED: Too many failed attempts.")
                        break 
                        
                    print("Incorrect PIN. Attempts remaining:", 3 - attempts)
            
            # If they were locked out, 'continue' restarts the outer loop (back to login)
            if auth_success == False:
                continue
                
        # 2. NEW ACCOUNT CREATION
        else:
            new_pin = input("Create a 4-digit PIN for your new account: ")
            # Initialize the new nested dictionary
            accounts[account_num] = {"pin": new_pin, "balance": 0.0}
            print("\nNew account created successfully. Your starting balance is ₹ 0.00")
            
            
        # INNER LOOP: The Account Dashboard
        while True:
            print("\n--- Account Main Menu ---")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Log Out")
            
            choice = input("Enter your choice (1-4): ") 
            
            # 3. DEPOSIT LOGIC
            if choice == '1':
                amount = float(input("Enter amount to deposit: ₹"))
                if amount > 0:
                    accounts[account_num]["balance"] += amount
                    print("\nTransaction Successful!")
                    print("Deposited: ₹", format(amount, ".2f"))
                    print("\nCurrent Balance for Account", account_num, "is: ₹", format(accounts[account_num]["balance"], ".2f"))
                    
                else:
                    print("\nInvalid amount. Please enter a positive number.")
                    
            # 4. WITHDRAWAL LOGIC
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount > 0:
                    if amount <= accounts[account_num]["balance"]:
                        accounts[account_num]["balance"] -= amount
                        print("\nTransaction Successful!")
                        print("Withdrew: ₹", format(amount, ".2f"))
                        print("\nCurrent Balance for Account", account_num, "is: ₹", format(accounts[account_num]["balance"], ".2f"))
                    else:
                        print("\nTransaction failed: Insufficient funds.")
                else:
                    print("\nInvalid amount. Please enter a positive number.")
                    
            # 5. BALANCE CHECK LOGIC
            elif choice == '3':
                print("\nCurrent Balance for Account", account_num, "is: ₹", format(accounts[account_num]["balance"], ".2f"))
                
            # 6. LOG OUT LOGIC
            elif choice == '4':
                print("\nLogging out of account", account_num, "...")
                # Breaks the inner loop, naturally returning to the outer login loop
                break 
                
            # 7. ERROR HANDLING
            else:
                print("\nInvalid choice. Please select a valid option from the menu.")
                
            # 8. POST-TRANSACTION PROMPT
            if choice in ['1', '2', '3']:
                continue_choice = input("\nPress 'Enter' to return to the Main Menu, or type 'L' to log out: ").upper()
                if continue_choice == 'L':
                    print("\nLogging out...")
                    break

# Execute the function to start the program
banking_system()
