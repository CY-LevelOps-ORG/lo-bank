from django.db import models
from django.contrib.auth import get_user_model

# Errors
class InvalidAmount(Exception):
    # Invalid deposit or withdrawal amount
    pass

# Create your models here.


class AccountTransaction(models.Model):
    # A transaction on an account
    TXN_MEDIUM_CASH = 'CA'
    TXN_MEDIUM_CHECK = 'CH'
    TXN_MEDIUM_WIRE = 'WI'
    TXN_MEDIUMS = (
        (TXN_MEDIUM_CASH, 'Cash'),
        (TXN_MEDIUM_CHECK, 'Check'),
        (TXN_MEDIUM_WIRE, 'Wire Transfer'),
    )

    TXN_DIR_IN = 'IN'
    TXN_DIR_OUT = 'OU'
    TXN_DIRS = (
        (TXN_DIR_IN, 'Deposit'),
        (TXN_DIR_OUT, 'Withdraw'),
    )

    medium = models.CharField(max_length=2, choices=TXN_MEDIUMS)
    direction = models.CharField(max_length=2, choices=TXN_DIRS)
    amount = models.FloatField(default=0)
    created_at = models.DateField(auto_now_add=True)
    account = models.ForeignKey('BankAccount', on_delete=models.CASCADE)


class BankAccount(models.Model):
    '''
    Bank Account
    '''
    # Owner of the bank account.
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # Name of the account
    name = models.CharField(max_length=120)
    # Account balance
    balance = models.FloatField(default=0)

    def _deposit(self, amount, txn_medium):
        # Validate the deposit amount
        if amount <= 0.0:
            raise InvalidAmount("Deposit has to be more than zero")
        self.balance += amount
        # Record the transaction
        AccountTransaction.objects.create(
            medium = txn_medium,
            direction = AccountTransaction.TXN_DIR_IN,
            amount = amount,
            account = self
        )

    def deposit_cash(self, amount):
        # Deposit an amount into the account.
        self._deposit(amount, AccountTransaction.TXN_MEDIUM_CASH)

    def deposit_check(self, amount):
        self._deposit(amount, AccountTransaction.TXN_MEDIUM_CHECK)
    
    def deposit_wiretransfer(self, amount):
        self._deposit(amount, AccountTransaction.TXN_MEDIUM_WIRE)
    
    def _withdraw(self, amount, txn_medium):
        if amount > self.balance:
            raise InvalidAmount('Withdraw amount cannot exceed the account balance')
        self.balance -= amount
        # Record the transaction
        AccountTransaction.objects.create(
            amount=amount,
            medium=txn_medium,
            direction=AccountTransaction.TXN_DIR_OUT,
            account=self
        )
    
    def withdraw_cash(self, amount):
        self._withdraw(amount, AccountTransaction.TXN_MEDIUM_CASH)
    
    def withdraw_check(self, amount):
        self._withdraw(amount, AccountTransaction.TXN_MEDIUM_CHECK)

    def withdraw_wiretransfer(self, amount):
        self._withdraw(amount, AccountTransaction.TXN_MEDIUM_WIRE)
    
    def get_balance(self):
        return self.balance