from django.db import models
from Users.models import User
from django.contrib.auth import get_user_model

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length = 50,
                             verbose_name='Заголовок',
                             )
    text = models.CharField(max_length = 100, verbose_name="Содержание")
    likes = models.IntegerField(verbose_name='Количество лайков', default = 0)
    date_create = models.DateTimeField(auto_now_add= True, verbose_name= 'Дата создания', blank = False)
    is_published = models.BooleanField(verbose_name = 'Статус публикации',
                                       blank = True, default=False)
    category = models.CharField(max_length = 50, blank = True)
    author = models.ForeignKey(get_user_model(),
                               on_delete= models.CASCADE,
                               verbose_name = 'Автор',
                               blank= False,
                               related_name='posts')
    tags = models.ManyToManyField('TagPost',
                                  blank = True,
                                  related_name = 'tags',
                                  verbose_name = 'Теги')
    

    #TODO: добавить время обновления поста и картинку поста


class TagPost(models.Model):
    tag = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)

    def __str__(self):
        return self.tag
 