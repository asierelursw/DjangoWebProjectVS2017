"""
Definition of models.
"""

from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import DateField

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    numChoices=models.IntegerField(default='0')
    tema = CharField(max_length=200, default="Vacío")
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)

class User(models.Model):
    email = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)


