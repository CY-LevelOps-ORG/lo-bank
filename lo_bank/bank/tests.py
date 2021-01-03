from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import BankAccount, InvalidAmount

# Create your tests here.
class BankAccountTestCase(TestCase):
    def setUp(self):
        self.bob = get_user_model().objects.create()
        self.bob_account = BankAccount.objects.create(name='Bob Checking', owner=self.bob)

    def test_deposit_cash(self):
        first_deposit = 60
        self.bob_account.deposit_cash(first_deposit)
        self.assertEqual(self.bob_account.get_balance(), first_deposit)
        second_deposit = 30
        self.bob_account.deposit_cash(second_deposit)
        self.assertEqual(self.bob_account.get_balance(), first_deposit+second_deposit)

    def test_deposit_check(self):
        first_deposit = 60
        self.bob_account.deposit_cash(first_deposit)
        self.assertEqual(self.bob_account.get_balance(), first_deposit)
        second_deposit = 30
        self.bob_account.deposit_cash(second_deposit)
        self.assertEqual(self.bob_account.get_balance(), first_deposit+second_deposit)

    def test_deposit_wire(self):
        first_deposit = 60
        self.bob_account.deposit_cash(first_deposit)
        self.assertEqual(self.bob_account.get_balance(), first_deposit)
        second_deposit = 30
        self.bob_account.deposit_cash(second_deposit)
        self.assertEqual(self.bob_account.get_balance(), first_deposit+second_deposit)

    def test_invalid_deposit(self):
        with self.assertRaises(InvalidAmount):
            self.bob_account.deposit_cash(-10)

    def test_withdraw_cash(self):
        first_deposit = 60
        self.bob_account.deposit_cash(first_deposit)
        first_withdraw = 30
        self.bob_account.withdraw_cash(first_withdraw)
        self.assertEqual(self.bob_account.get_balance(), first_deposit-first_withdraw)

    def test_invalid_withdraw_amount(self):
        first_deposit = 60
        self.bob_account.deposit_cash(first_deposit)
        with self.assertRaises(InvalidAmount):
            self.bob_account.withdraw_cash(first_deposit+10)
