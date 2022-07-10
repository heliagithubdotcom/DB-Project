from django.db import models


# Create your models here.
class User(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=150)
    phone = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=50)


class UserAddress(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
