from rest_framework import serializers
from driver_app.models import Answer, Question, Training, Advice, Tag, User


class AdviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advice
        fields = '__all__'

    tags = serializers.HyperlinkedRelatedField(allow_empty=True, many=True, queryset=Tag.objects.all(),
                                               view_name='tag-detail')
    users_passed_advice = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='user-detail')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    advice_set = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='advices')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    answers = AnswerSerializer(many=True, required=False)


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

    advice_set = serializers.HyperlinkedRelatedField(many=True, queryset=Advice.objects.all(),
                                                     view_name='advice-detail')

    train_question = QuestionSerializer(many=True, required=False, read_only=True)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'