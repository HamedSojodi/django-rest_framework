from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
from accounts.serializers import UserRegisterSerializer


class UserRegisterView(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            User.objects.create_user(ser_data.validated_data['username'],
                                     ser_data.validated_data['email'],
                                     ser_data.validated_data['password'],
                                     )
            return Response(data=ser_data.data)

        return Response(data=ser_data.errors)

#
# class UserRegisterView(generics.CreateAPIView):
#     serializer_class = UserRegisterSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
