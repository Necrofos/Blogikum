from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.HomePage.as_view(), name = 'home'),
    path('about_project/', views.About.as_view(), name = 'about_project'),
    path('rules/', views.rules, name = 'rules'),
    path('add_post/', views.add_post, name = 'add_post'),
]