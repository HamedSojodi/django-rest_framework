from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer


# class HomeView(APIView):
#     def get(self, request):
#         person = Person.objects.all()
#         ser_data = PersonSerializer(instance=person, many=True)
#         return Response(ser_data.data)

class HomeView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
