from django.shortcuts import render
from rest_framework import generics, status
# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from permissions import IsOwnerOrReady
from .models import Person, Question
from .serializers import PersonSerializer, QuestionSerializer


class HomeView(APIView):
    permission_classes = [IsAuthenticated, ]
    # throttle_scope = 'contacts'

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


class QuestionCreateView(APIView):
    def post(self, request):
        ser_data = QuestionSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


#
# class QuestionCreateView(CreateAPIView):
#     serializer_class = QuestionSerializer


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReady, ]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        ser_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


# class QuestionUpdateView(UpdateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#
#     lookup_field = 'pk'
#
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"messages": "question update successfully"})


class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReady, ]

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message : question deleted'}, status=status.HTTP_200_OK)

#
# class QuestionDeleteView(DestroyAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#
#     def preform_destroy(self, pk):
#         question = Question.objects.get(pk=pk)
#         question.delete()
