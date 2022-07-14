from django.db import models
from user.models import User


# Create your models here.
#CREATE TABLE STORE
#(
#StoreID INT NOT NULL,
#StoreName VARCHAR(40) NOT NULL,
#PRIMARY KEY (StoreID),
#);
class Store(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

#CREATE TABLE PRODUCT
#(
#  ProductID INT NOT NULL,
#  ProductName VARCHAR(64) NOT NULL,
#  ProductPrice FLOAT NOT NULL,
#  Rating FLOAT,
#  About VARCHAR(100),
#  DateAdded DATE,
#  PRIMARY KEY (ProductID)
#);
class Product(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    rate = models.FloatField(null=True)

#CREATE TABLE PROSTORE
#(
#  ProductID INT NOT NULL,
#  StoreID INT NOT NULL,
#  Availabilities BINARY,
#  FOREIGN KEY ProductID REFERENCES PRODUCT(ProductID),
#  FOREIGN KEY StoreID REFERENCES STORE(StoreID),
#  PRIMARY KEY ProductID, StoreID,
#);
class StoreProduct(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)


#CREATE TABLE REVIEW
#(
#  ReviewID INT NOT NULL,
#  ReviewText VARCHAR(100) NOT NULL,
#  UserID INT NOT NULL,
#  ProductID INT NOT NULL,
#  PRIMARY KEY (ReviewID),
#  FOREIGN KEY UserID REFERENCES USER(UserID),
#  FOREIGN KEY ProductID REFERENCES PRODUCT(ProductID),
#);
class Review(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)
    rate = models.PositiveSmallIntegerField()

#CREATE TABLE CATEGORY
#(
#  CategoryID INT NOT NULL,
#  CategoryName VARCHAR(20) NOT NULL,
#  PRIMARY KEY (CategoryID),
#);
class Category(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=30)
    

#CREATE TABLE PROCAT
#(
#  ProductID INT NOT NULL,
#  CategoryID INT NOT NULL,
#  FOREIGN KEY ProductID REFERENCES PRODUCT(ProductID),
#  FOREIGN KEY CategoryID REFERENCES CATEGORY(CategoryID),
#  PRIMARY KEY ProductID, CategoryID,
#);
class ProductCategory(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

