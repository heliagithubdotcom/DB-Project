from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import OrderSerializer, OrderItemSerializer, OrderROSerializer, OrderStatusSerializer
from .models import Order, OrderItem, OrderStatus
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
        order_status = OrderStatus.objects.create(order=order)

        order_items_res = []
        for oi in order_items:
            try:
                osp = oi['store_product']
                oic = oi['count']
                store_product = StoreProduct.objects.raw('SELECT * FROM shop_storeproduct WHERE id == %s', [osp])[0]
            except (IndexError, KeyError):
                return Response({"message": "store product does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            if store_product.available is False:
                return Response({"message": "store product is not available"}, status=status.HTTP_400_BAD_REQUEST)

            if oic is None or oic <= 0:
                return Response({"message": "count not valid."}, status=status.HTTP_400_BAD_REQUEST)
 
            order_item_obj = OrderItem.objects.create(order=order, store_product=store_product, count=oic)
            oi_ser = OrderItemSerializer(order_item_obj)
            order_items_res.append(oi_ser.data)

        order_ser = OrderSerializer(order)
        order_status_ser = OrderStatusSerializer(order_status)

        res = order_ser.data.copy()
        res.update({"order_status": order_status_ser.data})
        res.update({"order_items": order_items_res})
        return Response(res, status=status.HTTP_201_CREATED)

    def get(self, request):
        user_id = request.query_params.get('user_id')

        if user_id is None:
            orders = Order.objects.raw('SELECT * FROM order_order')
        else:
            orders = Order.objects.raw('SELECT * FROM order_order INNER JOIN user_useraddress ON order_order.customer_address_id=user_useraddress.id WHERE user_useraddress.user_id == %s', [user_id])

        ser = OrderROSerializer(orders, many=True)
        response = ser.data.copy()

        for index, order in enumerate(orders):
            order_items = OrderItem.objects.raw('SELECT * FROM order_orderitem WHERE order_id == %s', [order.id])
            order_item_ser = OrderItemSerializer(order_items, many=True)

            order_status = OrderStatus.objects.raw('SELECT * FROM order_orderstatus WHERE order_id == %s ORDER BY created_at DESC', [order.id])[0]
            order_status_ser = OrderStatusSerializer(order_status)

            response[index]['order_items'] = order_item_ser.data
            response[index]['order_status'] = order_status_ser.data

        return Response(response, status=status.HTTP_200_OK)
