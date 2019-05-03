"""
Here is where your API routs should be declared, all of them need to point to a particular View from the views.py file
"""
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from api import views

def HomeView(request):
    return HttpResponse("<h1>Not found</h1>Please type a valid endpoint URL like: <a href='/api/member/'>/api/member/</a>")

urlpatterns = [
    path('', HomeView),
    path('member/', views.MembersView.as_view()),
    path('member/<int:member_id>', views.MembersView.as_view()),
    ## add the second path member/<id> here
]
