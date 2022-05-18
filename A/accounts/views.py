from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
# Create your views here.
from accounts.serializers import UserRegisterSerializer

#
# class UserRegisterView(APIView):
#     def post(self, request):
#         ser_data = UserRegisterSerializer(data=request.POST)
#         if ser_data.is_valid():
#             ser_data.create(ser_data.validated_data)
#             return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
#
#         return Response(data=ser_data.errors,status=status.HTTP_400_BAD_REQUEST )


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        serializer.create(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

