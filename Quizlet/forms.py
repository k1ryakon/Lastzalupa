from django.forms import ModelForm
from .models import Quiz, Question, Comment

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['question_text']
        
class QuestionForm(ModelForm):
    class  Meta:
        model = Question
        fields = ['question', 'status']        
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']        