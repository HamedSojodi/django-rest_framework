from rest_framework import serializers

from home.custom_relational_fields import UserEmailNameRelationalField
from home.models import Question, Answer


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    age = serializers.IntegerField(max_value=None, min_value=None)
    email = serializers.EmailField()


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    user = UserEmailNameRelationalField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self, obj):
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
