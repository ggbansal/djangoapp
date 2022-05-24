from ast import Sub
from django.contrib import admin

from .models import Question, Choice, Subject, UserProfile

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserProfile)
admin.site.register(Subject)