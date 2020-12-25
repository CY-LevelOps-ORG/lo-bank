from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class BankAccount(models.Model):
    # Owner of the bank account.
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # Name of the account
    name = models.CharField(max_length=120)
