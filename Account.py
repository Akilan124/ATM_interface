import json
import os
from datetime import datetime

class Account:
    """
    A class to represent a bank account in the ATM system.
    Handles deposit, withdrawal, balance check, transaction history,
    and data persistence.
    """
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.history = []  # Stores transaction logs

    def deposit(self, amount):
        """Add funds to the account and log the transaction."""
        if amount > 0:
            self.balance += amount
            self._add_history(f"Deposited ₹{amount}")
            return True
        return False

    def withdraw(self, amount):
        """Withdraw funds if sufficient balance is available."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._add_history(f"Withdrew ₹{amount}")
            return True
        return False

    def check_balance(self):
        """Return the current balance and log the action."""
        self._add_history("Checked balance")
        return self.balance

    def _add_history(self, action):
        """Private method to log a transaction with a timestamp."""
        self.history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {action}")

    def view_history(self):
        """Return a list of all past transactions."""
        return self.history if self.history else ["No transactions yet."]

    def save(self):
        """Save account data to a JSON file (used for persistence)."""
        path = f"data/user_{self.account_number}.json"
        data = {
            'account_number': self.account_number,
            'pin': self.pin,
            'balance': self.balance,
            'history': self.history
        }
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load(cls, account_number, pin):
        """
        Load account from file based on account number and pin.
        Returns an Account object if credentials are correct.
        """
        path = f"data/user_{account_number}.json"
        if not os.path.exists(path):
            return None
        with open(path, 'r') as f:
            data = json.load(f)
            if str(data['pin']) == str(pin):
                acc = cls(data['account_number'], data['pin'], data['balance'])
                acc.history = data['history']
                return acc
            else:
                return None
