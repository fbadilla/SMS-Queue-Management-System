"""
Here is where your API routs should be declared, all of them need to point to a particular View from the views.py file
"""
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from api import views

def HomeView(request):
    return HttpResponse("<h1>Hello!</h1>Please type a valid endpoint URL from api/urls.py")

urlpatterns = [
    path('', HomeView),
    ## add you api paths here
    path('next/', views.QueueView.as_view()),
    path('new/', views.QueueView.as_view()),
    path('all/', views.QueueAllView.as_view()),
]
