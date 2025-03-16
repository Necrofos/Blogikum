from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


class HomePage(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'Posts/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context




class About(TemplateView):
    template_name = 'Posts/about_project.html'




#TODO: добавить нормальные функции для описания правил
def rules(request):
    return HttpResponse('Правила проекта')

@login_required
def add_post(request):
    if(request.method == 'GET'):
        form = PostForm()
        return render(request, 'Posts/add_post.html', context = {'form' : form})
    elif (request.method == 'POST'):
        form = PostForm(request.POST)
        if(form.is_valid()):
            cleaned_data = form.cleaned_data
            cleaned_data['author'] = request.user
            new_post = Post.objects.create(title = cleaned_data['title'],
                                           text = cleaned_data['text'],
                                           likes = 0,
                                           author = cleaned_data['author']
                                           )
            new_post.tags.add(cleaned_data['tag'])
            return redirect('home')
    return HttpResponse('kajdlfjdas;f')



#TODO: добавить кнопку лайка
