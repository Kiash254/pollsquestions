from pyexpat import model
from django.db import models

# Create your models here.
class Questions(models.Model):
    quiz_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.quiz_text 
class Choice(models.Model):
    questions=models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=8)
    def __str__(self):
        return self.choice_text