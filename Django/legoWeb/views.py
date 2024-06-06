from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from legoWeb.models import QuestionType,ChoiceQuestion


# Create your views here.
@csrf_exempt
def add_question(request):
    if request.user.is_authenticated:
        if request.method != 'POST':
            print(1)
            return HttpResponse(status=400)
        else:
            if request.POST['question_type'] == '0':
                choice_question_info = request.POST['question']
                choice_op1 = request.POST['op1']
                choice_op2 = request.POST['op2']
                choice_op3 = request.POST['op3']
                choice_op4 = request.POST['op4']
                answer = request.POST['answer']
                print(request.POST)
                ChoiceQuestion(
                               ChoiceQuestionType=QuestionType.objects.get(pk=1),
                               ChoiceQuestionInfo=choice_question_info,
                               choiceQst_Op1=choice_op1,
                               choiceQst_Op2=choice_op2,
                               choiceQst_Op3=choice_op3,
                               choiceQst_Op4=choice_op4,
                               choiceQst_answer=answer).save()
                return render(request, 'add_question.html')


def add_page(request):
    if request.user.is_authenticated:
        return render(request,'add_question.html')
    else:
        return HttpResponse(status=400)


def show_all_question(request):

    a = QuestionType.objects.get(id=1)
    b = a.choicequestion_set.all().order_by('id')
    print(b)
    print(a)

    context = {'questions': b}
    return render(request, 'questions.html', context)