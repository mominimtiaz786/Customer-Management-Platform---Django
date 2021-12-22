from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORIES = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.TextField( null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUSES = (
        ('Pending','Pending'),
        ('Out for Delievery','Out for Delievery'),
        ('Delieverd','Delieverd'),
    )
    status = models.CharField(max_length=200, null=True, choices=STATUSES)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)