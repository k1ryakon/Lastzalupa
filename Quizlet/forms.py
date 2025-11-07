from django.forms import ModelForm
from .models import Quiz, Question

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['question_text']
        
class QuestionForm(ModelForm):
    class  Meta:
        model = Question
        fields = ['question']        