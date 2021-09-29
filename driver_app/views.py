from driver_app.models import Advice, Answer, Question, Training, Tag, User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets, status
from driver_app.serializers import AdviceSerializer, AnswerSerializer, QuestionSerializer, TrainingSerializer, \
    TagSerializer, UserSerializer


class AdviceAPIView(generics.ListCreateAPIView):
    queryset = Advice.objects.all().order_by('?')
    serializer_class = AdviceSerializer


class AdviceDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


class AnswerAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TrainingAPIView(generics.ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class TrainingDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CheckTraining(APIView):
    @csrf_exempt
    def post(self, request):
        t = Training.objects.get(pk=request.data['training-id'])
        questions = t.question_to_training.all()
        correct_answers = []
        resp_dict = {}
        for q in questions:
            correct_answers.append(q.answers.filter(correct=True).first().pk)
        correct_counter = 0
        for answer_id in request.data['answers']:
            if answer_id in correct_answers:
                correct_counter += 1
        resp_dict['score'] = correct_counter
        resp_dict['possible_score'] = len(correct_answers)

        return Response(resp_dict, status=status.HTTP_200_OK)