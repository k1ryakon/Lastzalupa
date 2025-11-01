from django.db import models
from django.urls import reverse



class Dummy(models.Model):
    question_text = models.CharField(max_length=100, verbose_name='Тема квиза')


    def get_absolute_url(self):
        return reverse("quizlet:detail", args=[self.id])

    def __str__(self):
        return self.question_text
    
    class Meta:
        db_table_comment= "Тут у нас храняться темы квиза"
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квизы'
        

        

class Answer(models.Model):
    dummy = models.ForeignKey(Dummy, verbose_name="Вопросики", on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=100)

    
    def __str__(self):
        return f"{self.answer1}"
    