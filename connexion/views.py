from rest_framework.generics import GenericAPIView
from connexion.serializers import RegisterSerializer, LoginSerializer
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
from rest_framework.response import Response
from connexion.models import User

class UserAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = LoginSerializer(user)
        return response.Response({"user": serializer.data})


class UsersAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = LoginSerializer(users, many=True)
        return response.Response({"users": serializer.data})


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save() # for that make sure that the RegisterSerializer implements the create method
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = []
    def post(self, request):
        username = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            serializer = self.serializer_class(user)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        return response.Response(data={"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(GenericAPIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'message': 'success'}
        return response
