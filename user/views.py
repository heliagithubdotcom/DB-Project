from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .utils import PasswordCreator
from .serializers import UserSerializer


# Create your views here.
class SignupView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        phone = data.get('phone')

        if username is None or password is None or firstname is None or lastname is None or phone is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        filtered_users = User.objects.raw('SELECT * FROM user_user WHERE username == %s OR phone == %s', [username, phone])
        if len(filtered_users) > 0:
            return Response({'message': 'user with this username or phone number exists'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            pass_creator = PasswordCreator(password)
            pass_creator.check_password_validation()
            hashed_password = pass_creator.hash_password()
        except Exception as exc:
            return Response({'message': str(exc)}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(username=username, password=hashed_password, firstname=firstname, lastname=lastname, phone=phone)
        ser = UserSerializer(user)
        return Response(ser.data, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        if username is None or password is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.raw('SELECT * FROM user_user WHERE username == %s', [username])[0]
        except IndexError:
            return Response({'message': "user with this username doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

        pass_creator = PasswordCreator(password)
        hashed_password = pass_creator.hash_password()

        if hashed_password != user.password:
            return Response({'message': 'password is not correct'}, status=status.HTTP_400_BAD_REQUEST)

        ser = UserSerializer(user)
        return Response(ser.data, status=status.HTTP_200_OK)
