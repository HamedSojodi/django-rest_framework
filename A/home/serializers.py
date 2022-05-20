from rest_framework import serializers

from home.models import Question, Answer


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    age = serializers.IntegerField(max_value=None, min_value=None)
    email = serializers.EmailField()


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Answer
        fields = '__all__'
