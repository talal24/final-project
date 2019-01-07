from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    confirm = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middile_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50)
    position = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name + '  ' + self.last_name

    @property
    def fullname(self):
        return self.first_name + self.middile_name + self.last_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
