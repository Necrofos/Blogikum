from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.home, name = 'home'),
    path('authentication/', views.authorization, name = 'authentication'),
    path('registration/', views.registration, name = 'registration'),
    path('about_project/', views.about, name = 'about_project'),
    path('rules/', views.rules, name = 'rules'),
    path('add_post/', views.add_post, name = 'add_post')
]