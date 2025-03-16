from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm
from django.contrib.auth import authenticate, login
from django.views.generic import UpdateView, TemplateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView




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
    return render(request, 'Users/login.html', context = {'form': form})


def register_user(request):
    if(request.method == 'POST'):
        form = RegisterUserForm(request.POST)
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password2'])
        user.save()
        return render(request, 'Users/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'Users/register.html', context = {'form': form})




class RegisterDone(TemplateView):
    template_name = 'Users/register.html'

def register_done(request):
    return render(request, 'Users/register_done.html')



class UserProfile(UpdateView):
    model = get_user_model()
    template_name = 'Users/user_account.html'
    form_class = ProfileUserForm 


    def get_object(self, queryset = None):
        return self.request.user
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    