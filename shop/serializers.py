from rest_framework.serializers import ModelSerializer

from .models import Store, StoreProduct, Product, Review, Category


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
        depth = 2


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
