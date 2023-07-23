

from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from . import views


def myHomeFun(request):
    return HttpResponse('<h1>Hello</h1>')
    
urlpatterns = [
    path('',myHomeFun),
    path('home/',views.myView)
]
