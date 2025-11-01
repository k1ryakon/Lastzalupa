from django.forms import ModelForm
from .models import Dummy, Answer

class QuesForm(ModelForm):
    class Meta:
        model = Dummy
        fields = ['question_text']
        
class AnswerForm(ModelForm):
    class  Meta:
        model = Answer
        fields = ['answer1']        