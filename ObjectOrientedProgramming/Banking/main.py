from class_module import BankAccount
from exception_module import InsufficientFundsError, InvalidAmountError
from logging_module import logger

def main():
    print(f"Welcome to {BankAccount.bank_name}!")
    
    # Creating accounts
    try:
        acc1 = BankAccount("Alice Smith", "ACC1001", 500.0)
        acc2 = BankAccount("Bob Jones", "ACC1002", 150.0)
    except InvalidAmountError as e:
        print(f"Creation Error: {e}")

    # Display initial info & total count
    acc1.display_account_details()
    print(f"Total Accounts Created: {BankAccount.get_total_accounts()}")

    # Perform deposit & valid withdrawal
    try:
        acc1.deposit(200.0)
        acc1.withdraw(100.0)
    except (InsufficientFundsError, InvalidAmountError) as e:
        print(f"Transaction Error: {e}")

    acc1.display_account_details()

    # Test overdraw exception handling
    print("\nAttempting invalid withdrawal (overdrawing)...")
    try:
        acc1.withdraw(1000.0)
    except InsufficientFundsError as e:
        print(f"Caught Exception: {e}")

    # Changing bank name via class method
    print("\nChanging Bank Name...")
    BankAccount.change_bank_name("Global Apex Bank")
    
    # Verify bank name update reflects everywhere
    acc1.display_account_details()
    acc2.display_account_details()

if __name__ == "__main__":
    main()