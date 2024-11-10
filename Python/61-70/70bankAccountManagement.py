def BankAccountManagement():
    Balance = 0

    while True:
        print("Menu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit Program")
        Option = input("Please select an option: ")

        if Option == '1':
            Amount = float(input("Enter amount to deposit: "))
            if Amount > 0:
                Balance += Amount
                print(f"Current Balance: {Balance}")
            else:
                print("Please enter a positive amount.")

        elif Option == '2':
            Amount = float(input("Enter amount to withdraw: "))
            if Amount > 0:
                if Amount <= Balance:
                    Balance -= Amount
                    print(f"Current Balance: {Balance}")
                else:
                    print("Insufficient funds.")
            else:
                print("Please enter a positive amount.")

        elif Option == '3':
            print(f"Current Balance: {Balance}")

        elif Option == '4':
            print("Thank you for using the bank account management system.")
            break

        else:
            print("Invalid option. Please try again.")

BankAccountManagement()
