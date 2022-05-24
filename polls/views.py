from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Choice, Subject, UserProfile

# Create your views here.
def showall(request):
    questions = Question.objects.all()
    return render(request, 'polls/qanda.html', {'questions': questions})


def vote(request, question_id):
    print(request.POST)
    return HttpResponse('hello')


def load_userprofile(request):
    interests = Subject.objects.all()
    return render(request, 'polls/user.html', {'interests': interests})


def create_profile(request):
    print(request.POST)
    mentor_subjects = request.POST.getlist('will_mentor')
    my_interests = request.POST.getlist('my_interests')
    username = request.POST['username']
    pwd = request.POST['password']

    print(request.user)

    if request.user.is_authenticated:
        user = request.user.userprofile_set.create()
        
    for ms in mentor_subjects:
        user.will_mentor.add(ms)

    for interest in my_interests:
        user.interests.add(interest)

    print(mentor_subjects, my_interests, username, pwd)
    return HttpResponse(request.POST['username'])


def load_testpage(request):
    return render(request, 'polls/bulmatest.html')