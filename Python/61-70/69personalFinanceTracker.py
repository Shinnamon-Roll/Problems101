income_entries = []
expense_entries = []

def add_income(amount: float, description: str) -> None:
    income_entries.append((amount, description))
    print(f"Income entry added: {description} - {amount}")

def add_expense(amount: float, description: str) -> None:
    expense_entries.append((amount, description))
    print(f"Expense entry added: {description} - {amount}")

def display_income_entries() -> None:
    print("Income Entries:")
    for description, amount in income_entries:
        print(f"{description}: {amount}")

def display_expense_entries() -> None:
    print("Expense Entries:")
    for description, amount in expense_entries:
        print(f"{description}: {amount}")

def calculate_balance() -> float:
    total_income = sum(amount for amount, _ in income_entries)
    total_expenses = sum(amount for amount, _ in expense_entries)
    return total_income - total_expenses

def main():
    while True:
        print("\nMenu:")
        print("1. Add Income Entry")
        print("2. Add Expense Entry")
        print("3. Display Income Entries")
        print("4. Display Expense Entries")
        print("5. Calculate Balance")
        print("6. Exit")
        option = input("Please select an option: ")

        if option == '1':
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            add_income(amount, description)
        elif option == '2':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            add_expense(amount, description)
        elif option == '3':
            display_income_entries()
        elif option == '4':
            display_expense_entries()
        elif option == '5':
            balance = calculate_balance()
            print(f"Current Balance: {balance}")
        elif option == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
