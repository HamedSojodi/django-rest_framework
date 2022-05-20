from django.shortcuts import render
from rest_framework import generics, status
# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question
from .serializers import PersonSerializer, QuestionSerializer


class HomeView(APIView):
    # permission_classes = [IsAdminUser, ]

    def get(self, request):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person, many=True)
        return Response(ser_data.data)


# class HomeView(generics.ListAPIView):
#     permission_classes = [IsAdminUser, ]
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True).data
        return Response(ser_data, status=status.HTTP_200_OK)

#
# class QuestionListView(ListAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
