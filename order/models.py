from django.db import models
from shop.models import StoreProduct
from user.models import UserAddress


# CREATE TABLE Order
# (
#  OrderID INT NOT NULL,
#   created_at DATE NOT NULL,
#   delivery_method VARCHAR(2) NOT NULL,
#   AddressID INT NOT NULL,
#   CodeID INT NOT NULL,
#   PRIMARY KEY (OrderID),
#   FOREIGN KEY (UserID) REFERENCES USER(UserID),
#   FOREIGN KEY (AddressID) REFERENCES ADDRESSES(AddressID),
#   FOREIGN KEY (CodeID) REFERENCES PROMOTION(CodeID),
# );
class Order(models.Model):
    POST = 'PT'
    SNAPP = 'SP'
    TAPSI = 'TP'
    DELIVERY_CHOICES = (
        (POST, 'Post'),
        (SNAPP, 'Snapp'),
        (TAPSI, 'Tapsi'),
    )

    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    customer_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    delivery_method = models.CharField(max_length=2, choices=DELIVERY_CHOICES, default=POST)
    created_at = models.DateTimeField(auto_now_add=True)


# CREATE TABLE OrderItem
# (
#  ProductID INT NOT NULL,
#  OrderID INT NOT NULL,
#  TotalPrice INT NOT NULL,
#  FOREIGN KEY ProductID REFERENCES PRODUCT(ProductID),
#  FOREIGN KEY OrderID REFERENCES ORDER(OrderID),
#  PRIMARY KEY ProductID, OrderID,
# );
class OrderItem(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    store_product = models.ForeignKey(StoreProduct, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


class OrderStatus(models.Model):
    PAID = 'Paid'
    DELIVERED = 'Delivered'
    RECEIVED = 'Received'
    CANCELED = 'Canceled'

    ORDER_STATUS_CHOICES = (
        (PAID, 'Paid'),
        (DELIVERED, 'Delivered'),
        (RECEIVED, 'Received'),
        (CANCELED, 'Canceled'),
    )

    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=ORDER_STATUS_CHOICES, default=PAID)
    created_at = models.DateTimeField(auto_now_add=True)
