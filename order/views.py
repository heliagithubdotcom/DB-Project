from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from shop.models import StoreProduct
from user.models import UserAddress


# Create your views here.
class OrderView(APIView):
    def post(self, request):
        data = request.data
        customer_address_id = data.get('customer_address')
        delivery_method = data.get('delivery_method')
        order_items = data.get('order_items')

        if customer_address_id is None or delivery_method is None or order_items is None:
            return Response({"message": "customer id or delivery method or order items doesn't exist"},
                            status=status.HTTP_400_BAD_REQUEST)

        if delivery_method not in (Order.POST, Order.SNAPP, Order.TAPSI):
            return Response({"message": "delivery method is not valid"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            customer_address = UserAddress.objects.raw('SELECT * FROM user_useraddress WHERE id == %s', [customer_address_id])[0]
        except IndexError:
            return Response({"message": "customer id is not valid"}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(customer_address=customer_address, delivery_method=delivery_method)

        order_items_res = []
        for oi in order_items:
            try:
                osp = oi['store_product']
                store_product = StoreProduct.objects.raw('SELECT * FROM shop_storeproduct WHERE id == %s', [osp])[0]
            except (IndexError, KeyError):
                return Response({"message": "store product does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            if store_product.available is False:
                return Response({"message": "store product is not available"}, status=status.HTTP_400_BAD_REQUEST)

            order_item_obj = OrderItem.objects.create(order=order, store_product=store_product)
            oi_ser = OrderItemSerializer(order_item_obj)
            order_items_res.append(oi_ser.data)

        ser = OrderSerializer(order)
        res = ser.data.copy()
        res.update({"order_items": order_items_res})
        return Response(res, status=status.HTTP_201_CREATED)
