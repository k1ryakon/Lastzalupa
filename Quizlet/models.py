from django.db import models
from django.urls import reverse



class Quiz(models.Model):
    question_text = models.CharField(max_length=100, verbose_name='Тема квиза')


    def get_absolute_url(self):
        return reverse("quizlet:detail", args=[self.id])

    def __str__(self):
        return self.question_text
    
    class Meta:
        db_table_comment= "Тут у нас храняться темы квиза"
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квизы'
        

        

class Question(models.Model):
    class Status(models.TextChoices):
        PROPERLY = 'PR', 'properly'
        WRONG = 'WR', "wrong"
        
    quiz = models.ForeignKey(Quiz, verbose_name="Вопросики", on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.WRONG)
    
    def __str__(self):
        return f"{self.question}"
    