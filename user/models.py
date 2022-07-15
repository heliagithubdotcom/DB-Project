from django.db import models


# Create your models here.
# CREATE TABLE USER
# (
#  UserID INT NOT NULL,
#  username VARCHAR(32) NOT NULL,
#  firstname VARCHAR(40) NOT NULL,
#  lastname VARCHAR(40) NOT NULL,
#  phone VARCHAR(11) NOT NULL,
#  password VARCHAR(300) NOT NULL,
#  AddressID INT NOT NULL,
#  PRIMARY KEY (UserID),
#  FOREIGN KEY AddressID REFERENCES ADDRESSES(AddressID),
# );
class User(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=300)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    phone = models.CharField(max_length=11, unique=True)

    @property
    def addresses(self):
        return UserAddress.objects.raw('SELECT * FROM user_useraddress WHERE user_id = %s', [self.id])


# CREATE TABLE ADDRESSES
# (
#  AddressID INT NOT NULL,
#  Addresses VARCHAR(100) NOT NULL,
#  PRIMARY KEY (AddressID),
# );
class UserAddress(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
