from rest_framework.serializers import ModelSerializer

from .models import Order, OrderItem, OrderStatus


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 1


class OrderItemROSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        depth = 2


class OrderROSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 3


class OrderStatusSerializer(ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'
