from django.db import models

# Create your models here.


class Post(models.Model):

    #TODO: ДОбавить автора поста с помощью связи ManyToOne
    title = models.CharField(max_length = 50,
                             verbose_name='Заголовок',
                             )
    text = models.CharField(max_length = 100, verbose_name="Содержание")
    likes = models.IntegerField(verbose_name='Количество лайков', default = 0)
    date_create = models.DateTimeField(auto_now_add= True, verbose_name= 'Дата создания', blank = False)
    is_published = models.BooleanField(verbose_name = 'Статус публикации',
                                       blank = True, default=False)
    category = models.CharField(max_length = 50, blank = True)

    #TODO: добавить время обновления поста и картинку поста
 