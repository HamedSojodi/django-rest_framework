from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
# Create your views here.
from accounts.serializers import UserRegisterSerializer, UserSerializer
from rest_framework import viewsets


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


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    def list(self, request):
        ser_data = UserSerializer(instance=self.queryset, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerializer(instance=user)
        return Response(ser_data.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerializer(instance=user, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerializer(instance=user, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        # custom permisstions in viewsets
        if user != request.user:
            return Response({'permission denied': 'you are not the owner'})
        user.is_active = False
        user.save()
        return Response({'message':'user deactivated'})
