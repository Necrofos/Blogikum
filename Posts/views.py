from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from .models import Post
from .forms import PostForm




#TODO: сделать базовый шаблон, от которого будут наследоваться все шаблоны
class HomePage(TemplateView):

    #TODO: добавить отображение меню через список меню(а лучше через миксин)
    template_name = 'home.html'


def home(request):
    posts = Post.objects.all()
    data = {'posts': posts}
    return render(request, 'home.html', context = data)


#TODO: добавить авторизацию, перенести ее в приложение Users
def authorization(request):
    
    return HttpResponse("Авторизация")


#TODO: добавить нормальные функции для регистрации, перенести регистрацию в приложение Users
def registration(reqeuest):
    return HttpResponse("Регистрация")


#TODO: добавить нормальные функции для описания платформы
def about(request):
    return HttpResponse('О проекте')


class AddPostPage(FormView):
    pass


#TODO: добавить нормальные функции для описания правил
def rules(request):
    return HttpResponse('Правила проекта')


def add_post(request):
    if(request.method == 'GET'):
        form = PostForm()
        return render(request, 'add_post.html', context = {'form' : form})
    elif (request.method == 'POST'):
        form = PostForm(request.POST)
        if(form.is_valid()):
            new_post = Post.objects.create(**form.cleaned_data)
            return redirect('home')
    return HttpResponse('kajdlfjdas;f')


#TODO: добавить кнопку добавления поста, которая доступна только авторизованным пользователям



#TODO: добавить кнопку лайка
