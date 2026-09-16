from exception_module import InsufficientFundsError, InvalidAmountError
from logging_module import logger

class BankAccount:
    # Class variables
    bank_name = "Global Trust Bank"
    total_accounts = 0  # Bonus: Tracks total number of accounts created

    def __init__(self, account_holder: str, account_number: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        
        if initial_balance < 0:
            logger.error(f"Initial balance cannot be negative for account {account_number}")
            raise InvalidAmountError("Initial balance cannot be negative.")
            
        self.balance = initial_balance
        BankAccount.total_accounts += 1
        logger.info(f"Account created for {account_holder} with Account No: {account_number}")

    @classmethod
    def change_bank_name(cls, new_name: str):
        cls.bank_name = new_name
        logger.info(f"Bank name changed globally to: {new_name}")

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    def deposit(self, amount: float):
        if amount <= 0:
            logger.warning(f"Failed deposit attempt of {amount} on account {self.account_number}")
            raise InvalidAmountError("Deposit amount must be greater than zero.")
        
        self.balance += amount
        logger.info(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            logger.warning(f"Failed withdrawal attempt of {amount} on account {self.account_number}")
            raise InvalidAmountError("Withdrawal amount must be greater than zero.")
            
        if amount > self.balance:
            logger.error(f"Overdraw attempt of {amount} on account {self.account_number} with balance {self.balance}")
            raise InsufficientFundsError(f"Insufficient funds! Available balance is {self.balance}")
            
        self.balance -= amount
        logger.info(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        return self.balance

    def check_balance(self):
        logger.info(f"Balance checked for account {self.account_number}: {self.balance}")
        return self.balance

    def display_account_details(self):
        print("\n--- Account Details ---")
        print(f"Bank Name: {BankAccount.bank_name}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")
        logger.info(f"Displayed details for account {self.account_number}")