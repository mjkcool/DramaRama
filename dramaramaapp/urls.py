from django.urls import path
from django.conf.urls import include, url
from . import views


# app_name = 'dramaramaapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('Who-you-are', views.form, name='form'),
    path('To.you--From.Rama💜', views.result),
    path('your-answer', views.answer),
    path('share-your-joy!', views.survey, name='survey'),
    path('submit', views.submitSurvey, name='submit'),
]