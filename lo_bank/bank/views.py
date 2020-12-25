from django.shortcuts import render
from rest_framework import viewsets
from .models import BankAccount
from .serializers import BankAccountSerializer

class BankAccountView(viewsets.ModelViewSet):
    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.all()