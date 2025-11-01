from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Dummy, Answer
from django.http import Http404
from .forms import QuesForm, AnswerForm
from django.urls import reverse

def index(request):
    if request.method == "POST":
        forma = QuesForm(request.POST)
        if forma.is_valid():
            forma.save()
            HttpResponseRedirect('/')
    else:
        forma = QuesForm()
    
    context = Dummy.objects.all()  
     
    return render(request, "Quizlet/index.html", {"latest_question_list": context,'forma': forma })




def detail(request, id):
    some = Answer.objects.filter(dummy=id)
    question = Dummy.objects.get(id=id)
    if request.method == "POST":
        answerform = AnswerForm(request.POST)
        if answerform.is_valid():
            answer = answerform.save(commit=False)
            answer.dummy_id = id
            answer.save()
            return HttpResponseRedirect(reverse('quizlet:detail', args=[id]))
    else:
        answerform = AnswerForm()
    return render(request, 'Quizlet/detail.html', {'form': answerform, "context":some, "question":question})