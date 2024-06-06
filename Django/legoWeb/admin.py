from django.contrib import admin
from .models import QuestionType,PracticalQuestion,ChoiceQuestion,TrueOrFalseQuestion
# Register your models here.

admin.site.register(QuestionType)
admin.site.register(PracticalQuestion)
admin.site.register(ChoiceQuestion)
admin.site.register(TrueOrFalseQuestion)