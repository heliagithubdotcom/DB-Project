from django.db import models
from shop.models import StoreProduct
from user.models import UserAddress


# Create your models here.
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


class OrderItem(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    store_product = models.ForeignKey(StoreProduct, on_delete=models.CASCADE)
