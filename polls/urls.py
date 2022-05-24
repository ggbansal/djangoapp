from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('showall', views.showall, name='showall'),
    path('vote/<int:question_id>', views.vote, name='vote'),
    path('userprofile', views.load_userprofile, name='userprofile'),
    path('createprofile', views.create_profile, name='createprofile'),
    path('test', views.load_testpage, name='test')
]

