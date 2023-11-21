import hashlib
import random
from datetime import datetime

class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = self._hash_password(password)
        self.accounts = []

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

class Account:
    def __init__(self, account_number, account_type, balance=0.0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

class Transaction:
    def __init__(self, transaction_id, date, transaction_type, amount, description, account_number):
        self.transaction_id = transaction_id
        self.date = date
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.account_number = account_number

class BankSystem:
    def __init__(self):
        self.users = []
        self.accounts = []
        self.transactions = []

    def create_user(self, username, password):
        user_id = len(self.users) + 1
        user = User(user_id, username, password)
        self.users.append(user)
        return user

    def create_account(self, user, account_type):
        account_number = random.randint(100000, 999999)
        account = Account(account_number, account_type)
        user.accounts.append(account)
        self.accounts.append(account)
        return account

    def perform_transaction(self, account, transaction_type, amount, description):
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdrawal':
            if not account.withdraw(amount):
                return False, "Insufficient funds."
        else:
            return False, "Invalid transaction type."

        transaction_id = len(self.transactions) + 1
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = Transaction(transaction_id, date, transaction_type, amount, description, account.account_number)
        self.transactions.append(transaction)
        return True, transaction

# Simple CLI Interface
def main():
    bank_system = BankSystem()

    while True:
        print("\n1. Login")
        print("2. Create Account")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            user = authenticate_user(bank_system, username, password)

            if user:
                user_menu(bank_system, user)
            else:
                print("Invalid username or password.")

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            new_user = bank_system.create_user(username, password)

            print(f"\nAccount created successfully! Your user ID is: {new_user.user_id}")

        elif choice == '3':
            print("Exiting the Online Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

def authenticate_user(bank_system, username, password):
    for user in bank_system.users:
        if user.username == username and user.password == hashlib.sha256(password.encode()).hexdigest():
            return user
    return None

def user_menu(bank_system, user):
    while True:
        print("\n1. Create Account")
        print("2. View Account Details")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. View Transaction History")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_type = input("Enter account type (e.g., savings, checking): ")
            new_account = bank_system.create_account(user, account_type)
            print(f"\nAccount created successfully! Your account number is: {new_account.account_number}")

        elif choice == '2':
            view_account_details(user)

        elif choice == '3':
            deposit(bank_system, user)

        elif choice == '4':
            withdraw(bank_system, user)

        elif choice == '5':
            view_transaction_history(bank_system, user)

        elif choice == '6':
            print("Logging out. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

def view_account_details(user):
    print("\nAccount Details:")
    for account in user.accounts:
        print(f"Account Number: {account.account_number}")
        print(f"Account Type: {account.account_type}")
        print(f"Balance: ${account.balance:.2f}\n")

def deposit(bank_system, user):
    account_number = int(input("Enter your account number: "))
    amount = float(input("Enter deposit amount: "))
    description = input("Enter deposit description: ")

    account = find_account_by_number(bank_system, account_number)

    if account:
        success, transaction = bank_system.perform_transaction(account, 'deposit', amount, description)
        if success:
            print(f"\nDeposit of ${amount:.2f} successful. Transaction ID: {transaction.transaction_id}")
        else:
            print(transaction)
    else:
        print("Invalid account number.")

def withdraw(bank_system, user):
    account_number = int(input("Enter your account number: "))
    amount = float(input("Enter withdrawal amount: "))
    description = input("Enter withdrawal description: ")

    account = find_account_by_number(bank_system, account_number)

    if account:
        success, transaction = bank_system.perform_transaction(account, 'withdrawal', amount, description)
        if success:
            print(f"\nWithdrawal of ${amount:.2f} successful. Transaction ID: {transaction.transaction_id}")
        else:
            print(transaction)
    else:
        print("Invalid account number.")

def view_transaction_history(bank_system, user):
    print("\nTransaction History:")
    for account in user.accounts:
        for transaction in bank_system.transactions:
            if account.account_number == transaction.account_number:
                print(f"Account Number: {account.account_number}")
                print(f"Transaction ID: {transaction.transaction_id}")
                print(f"Date: {transaction.date}")
                print(f"Type: {transaction.transaction_type}")
                print(f"Amount: ${transaction.amount:.2f}")
                print(f"Description: {transaction.description}\n")

def find_account_by_number(bank_system, account_number):
    for account in bank_system.accounts:
        if account.account_number == account_number:
            return account
    return None

if __name__ == "__main__":
    main()
