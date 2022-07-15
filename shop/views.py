from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Store, StoreProduct, Product, Review, Category, ProductCategory
from .serializers import StoreSerializer, StoreProductSerializer, ProductSerializer, ReviewSerializer, \
    CategorySerializer, StoreProductDeepSerializer
from user.models import User


# Create your views here.
class StoreView(APIView):

    def get(self, request):
        stores = Store.objects.raw('SELECT * FROM shop_store')
        ser = StoreSerializer(stores, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class StoreProductsView(APIView):

    def get(self, request, store_name):
        try:
            store = Store.objects.raw('SELECT * FROM shop_store WHERE name == %s', [store_name])[0]
            store_products = StoreProduct.objects.raw('SELECT * FROM shop_storeproduct WHERE store_id == %s', [store.id])
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        store_ser = StoreSerializer(store)
        products_ser = StoreProductSerializer(store_products, many=True)
        response_data = {
            'store': store_ser.data,
            'products': products_ser.data,
        }
        return Response(response_data, status=status.HTTP_200_OK)


class ProductView(APIView):

    def get(self, request, product_name):
        try:
            product = Product.objects.raw('SELECT * FROM shop_product WHERE name == %s', [product_name])[0]
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        ser = ProductSerializer(product)
        return Response(ser.data, status=status.HTTP_200_OK)


class ProductSortView(APIView):
    SORT_TYPES = ('ascending price', 'descending price', 'rate', 'date')

    def __is_valid_sort_type(self, sort_type):
        return sort_type in self.SORT_TYPES

    def get(self, request):
        sort_type = request.query_params.get('sort')

        if sort_type is not None:
            if sort_type == 'ascending price':
                products = Product.objects.raw('SELECT * FROM shop_product ORDER BY price')
            elif sort_type == 'descending price':
                products = Product.objects.raw('SELECT * FROM shop_product ORDER BY price DESC')
            elif sort_type == 'rate':
                products = Product.objects.raw('SELECT * FROM shop_product ORDER BY rate DESC')
            elif sort_type == 'date':
                products = Product.objects.raw('SELECT * FROM shop_product ORDER BY date')
            else:
                return Response({'message': 'sort type not valid'}, status=status.HTTP_400_BAD_REQUEST)
        else:   # without sort param
            products = Product.objects.raw('SELECT * FROM shop_product')

        ser = ProductSerializer(products, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class ProductStoreView(APIView):
    def get(self, request):
        store_products = StoreProduct.objects.raw('SELECT * FROM shop_storeproduct')
        ser = StoreProductDeepSerializer(store_products, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class ProductReviewView(APIView):

    def get(self, request, product_name):
        try:
            product = Product.objects.raw('SELECT * FROM shop_product WHERE name == %s', [product_name])[0]
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reviews = Review.objects.raw('SELECT * FROM shop_review WHERE product_id == %s', [product.id])
        ser = ReviewSerializer(reviews, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request, product_name):
        data = request.data
        review_description = data.get('description')
        rate = data.get('rate')
        user_id = data.get('user')

        if rate is None or review_description is None or user_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if rate < 1 or rate > 5:
            return Response({'message': 'rate is not valid'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.raw('SELECT * FROM user_user WHERE id == %s', [user_id])[0]
        except IndexError:
            return Response({'message': "user doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            product = Product.objects.raw('SELECT * FROM shop_product WHERE name == %s', [product_name])[0]
            reviews_count = len(Review.objects.raw('SELECT * FROM shop_review WHERE product_id == %s', [product.id]))
        except IndexError:
            return Response({'message': "product not found"}, status=status.HTTP_404_NOT_FOUND)

        review = Review.objects.create(user=user, product=product, description=review_description, rate=rate)
        
        if product.rate is None or reviews_count == 0:
            product.rate = review.rate
        else:
            product.rate = ((product.rate * reviews_count) + review.rate) / (reviews_count+1)
        product.save()

        ser = ReviewSerializer(review)
        return Response(ser.data, status=status.HTTP_201_CREATED)


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.raw('SELECT * FROM shop_category')
        ser = CategorySerializer(categories, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class CategoryProductView(APIView):
    def get(self, request, category_name):
        try:
            category = Category.objects.raw('SELECT * FROM shop_category WHERE name == %s', [category_name])[0]
        except IndexError:
            return Response({"message": "category not found"}, status=status.HTTP_404_NOT_FOUND)

        products = []
        category_products = ProductCategory.objects.raw('SELECT * FROM shop_productcategory WHERE category_id == %s', [category.id])
        
        for cp in category_products:
            products.append(cp.product)
        
        ser = ProductSerializer(products, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
