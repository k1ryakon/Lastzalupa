from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question, Comment
from django.http import Http404
from .forms import QuizForm, QuestionForm, CommentForm
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST


def index(request):
    if request.method == "POST":
        forma = QuizForm(request.POST)
        if forma.is_valid():
            forma.save()
            HttpResponseRedirect('/')
    else:
        forma = QuizForm()
    
    context = Quiz.objects.all().order_by('-id')  
    paginator = Paginator(context, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
     
    return render(request, "Quizlet/index.html", {"latest_question_list": posts,'forma': forma })




def detail(request, id):
    some = Question.objects.filter(quiz=id)
    qizi = Quiz.objects.get(id=id)
    commentform = CommentForm()
    comments = Comment.objects.filter(quize=qizi)
    if request.method == "POST":
        answerform = QuestionForm(request.POST)
        if answerform.is_valid():
            answer = answerform.save(commit=False)
            answer.quiz = qizi
            answer.save()
            return HttpResponseRedirect(reverse('quizlet:detail', args=[id]))
    else:
        answerform = QuestionForm()
    return render(request, 'Quizlet/detail.html', {'form': answerform, "questions":some, "qizi":qizi, "commentform":commentform,"comments":comments,})


@require_POST
def post_comment(request, id):
    qizi = Quiz.objects.get(id=id)
    comment = None
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.quize = qizi
        comment.save()
    return render(request,  'Quizlet/comment.html', {"commentform":form,"comment":comment, "qizi":qizi})