# Welcome to Expense Tracker - A Mini Python Project by Sahil Mukadam.

import json
def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"\nAdded expense: {description}, Amount: {amount}")

def get_total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)

def get_balance(balance, expenses):
    return balance - get_total_expenses(expenses)

def show_balance_details(balance, expenses):
    print(f"\nTotal balance: {balance}")
    print("Expenses:")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"\nTotal Spent: {get_total_expenses(expenses)}")
    print(f"Remaining balance: {get_balance(balance, expenses)}")

def load_balance_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['initial_balance'], data['expenses']
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []

def save_balance_data(filepath, initial_balance, expenses):
    data = {
        'initial_balance': initial_balance,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    print("Welcome to the Expense Tracker")
    initial_balance = float(input("Please enter your initial amount/balance: "))
    balance = initial_balance
    expenses = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show balance details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, description, amount)
        elif choice == "2":
            show_balance_details(balance, expenses)
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()