from .models import Customer
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def profileCreated(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        customer = Customer.objects.create(
            user=instance ,
            #email = instance.email,
            name= instance.username
            )
        customer.save()
        print("Customer Profile Created")