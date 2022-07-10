from django.db import models


# Create your models here.
#CREATE TABLE USER
#(
#  UserID INT NOT NULL,
#  Username VARCHAR(20) NOT NULL,
#  UserFname VARCHAR(40) NOT NULL,
#  UserLname VARCHAR(40) NOT NULL,
#  Phone INT NOT NULL,
#  Pass VARCHAR(16) NOT NULL,
#  AddressID INT NOT NULL,
#  PRIMARY KEY (UserID),
#  FOREIGN KEY AddressID REFERENCES ADDRESSES(AddressID),
#);


class User(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=150)
    phone = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=50)

#CREATE TABLE ADDRESSES
#(
#  AddressID INT NOT NULL,
#  Addresses VARCHAR(100) NOT NULL,
#  PRIMARY KEY (AddressID),
#);


class UserAddress(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
