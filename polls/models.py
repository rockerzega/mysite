import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    # Creaamos una funcion str para imprimir los datos del objeto
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publisehd recently?'

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #objects = models.Manager()

class Choice(models.Model):
    # Creaamos una funcion str para imprimir los datos del objeto
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE,)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)