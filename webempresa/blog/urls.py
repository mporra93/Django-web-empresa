from django.urls import path
from . import views


urlpatterns =  [
    #path del core
    path('', views.blog, name='blog'), 
]