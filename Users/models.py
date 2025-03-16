from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    photo = models.ImageField(blank=True, 
                              null = True, 
                              verbose_name = 'Аватарка',
                              
                              )
    date_of_birth = models.DateTimeField(blank = True,
                                         null = True, 
                                         verbose_name= 'Дата рождения',
                                         )
    
    
