from rest_framework.serializers import ModelSerializer

from .models import User, UserAddress


class UserAddressSerializer(ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'


class UserSerializer(ModelSerializer):
    addresses = UserAddressSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'firstname', 'lastname', 'phone', 'addresses']
