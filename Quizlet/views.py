from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Quiz, Question
from django.http import Http404
from .forms import QuizForm, QuestionForm
from django.urls import reverse

def index(request):
    if request.method == "POST":
        forma = QuizForm(request.POST)
        if forma.is_valid():
            forma.save()
            HttpResponseRedirect('/')
    else:
        forma = QuizForm()
    
    context = Quiz.objects.all()  
     
    return render(request, "Quizlet/index.html", {"latest_question_list": context,'forma': forma })




def detail(request, id):
    some = Question.objects.filter(quiz=id)
    qizi = Quiz.objects.get(id=id)
    if request.method == "POST":
        answerform = QuestionForm(request.POST)
        if answerform.is_valid():
            answer = answerform.save(commit=False)
            answer.quiz = qizi
            answer.save()
            return HttpResponseRedirect(reverse('quizlet:detail', args=[id]))
    else:
        answerform = QuestionForm()
    return render(request, 'Quizlet/detail.html', {'form': answerform, "questions":some, "qizi":qizi})