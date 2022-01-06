from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORIES = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.TextField( null=True, blank=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
    date = models.DateField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=SET_NULL)

    STATUSES = (
        ('Pending','Pending'),
        ('Out for Delievery','Out for Delievery'),
        ('Delieverd','Delieverd'),
    )
    status = models.CharField(max_length=200, null=True, choices=STATUSES)
    date = models.DateField(auto_now_add=True, null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id) + " ----- "+self.customer.name + " -----> ordered -----> " + self.product.name