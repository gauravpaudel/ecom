from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.store.models import Product

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length = 100, null=True, blank=True)
    last_name = models.CharField(max_length = 100, null=True, blank=True)
    city = models.CharField(max_length = 200, null=True, blank=True)
    phone = models.CharField(max_length = 20, null=True, blank=True)
    place = models.CharField(max_length = 200, null=True, blank=True)

    def __str__(self):
        return self.user.username
        
class ShopList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_list')
    items = models.ForeignKey(Product, on_delete=models.CASCADE)

@receiver(post_save, sender= User )
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender= User)
def saveUserProfile(sender, instance, **kwargs):
    instance.profile.save()