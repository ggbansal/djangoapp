from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.choice_text} ({self.question.id})'


class Subject(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self) -> str:
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    interests = models.ManyToManyField(Subject, blank=True, related_name='interests')
    will_mentor = models.ManyToManyField(Subject, blank=True, related_name='will_mentor')

    def __str__(self) -> str:
        return self.user.username
