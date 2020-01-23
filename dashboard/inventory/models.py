import uuid, PIL
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Product(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    availability = models.BooleanField()
    sales_count = models.PositiveSmallIntegerField(null=True)

class Business(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    address = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    website = models.CharField(max_length=200)
    
class Transaction(models.Model):
    timestamp = models.DateTimeField()
    customer = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField()
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)

class Contribution(models.Model):
    year = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField()