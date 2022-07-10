from rest_framework.serializers import ModelSerializer

from .models import Store, StoreProduct, Product, Review


class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StoreProductSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = StoreProduct
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
