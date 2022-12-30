from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from accounts.models import Profile
from .serializers import ProfileSerializer


class EmployeeDepartmentAPIView(APIView):
    permission_classes = [IsAdminUser]
   
    def get(self, request, pk):
        employees = Profile.objects.filter(department=pk)
        serializers = ProfileSerializer(employees, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
