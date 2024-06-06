from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class QuestionType(models.Model):
    Question_name = models.CharField(max_length=100)
    Question_level = models.IntegerField(default=0)
    Question_Course = models.IntegerField(default=0)
    Add_User = ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    updateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Question_name

    @property
    def all_questions(self):
        return ChoiceQuestion.all()


class PracticalQuestion(models.Model):
    practicalQuestionType = ForeignKey(QuestionType, on_delete=models.CASCADE)
    practicalQuestionInfo = models.TextField(max_length=100)
    practicalQuestionAnswers = models.TextField(max_length=100)


class ChoiceQuestion(models.Model):
    ChoiceQuestionType = ForeignKey(QuestionType, on_delete=models.CASCADE)
    ChoiceQuestionInfo = models.TextField(max_length=100)
    choiceQst_Op1 = models.TextField(max_length=100)
    choiceQst_Op2 = models.TextField(max_length=100)
    choiceQst_Op3 = models.TextField(max_length=100)
    choiceQst_Op4 = models.TextField(max_length=100)
    choiceQst_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.ChoiceQuestionInfo


class TrueOrFalseQuestion(models.Model):
    questionType = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    questionInfo = models.TextField(max_length=100)
    questionAnswers = models.CharField(max_length=100)
