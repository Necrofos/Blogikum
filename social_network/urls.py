from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Posts.urls')),
    path('', include('Users.urls')),
    path('admin/', admin.site.urls),
]
