from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login


# Create your views here.


def login_user(request):
    if(request.method == "POST"):
        form = LoginUserForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if(user is not None and user.is_active):
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
    return render(request, 'login.html', context = {'form': form})


#TODO: добавить личный кабинет пользователя, добавить фукнцию выхода из системы

def register_user(request):
    if(request.method == 'POST'):
        form = RegisterUserForm(request.POST)
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password2'])
        user.save()
        return render(request, 'register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', context = {'form': form})


def register_done(request):
    return render(request, 'register_done.html')



