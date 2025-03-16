from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.login_user, name = 'login'),
    path('register', views.register_user, name = 'register'),
    path('profile', views.UserProfile.as_view(), name = 'profile'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]