from django.contrib.auth import get_user_model, login
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, LoginTokenSerializer


class RegisterUserAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


User = get_user_model()


class AllUsersAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        users = User.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActivateAccountView(View):

    def get(self, request, activation_code):
        user = User.objects.get(activation_code=activation_code)
        user.is_active = True
        user.activation_code = ""
        user.save()
        return render(request, "success.html", locals())


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return Response({
            "login": "success"
        }, status=status.HTTP_200_OK)


class UserTokenLoginAPIView(APIView):
    def post(self, request):
        serializer = LoginTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserTokenLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
