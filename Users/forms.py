from django import forms
from.models import User
from django.contrib.auth import get_user_model

class LoginUserForm(forms.Form):
    username = forms.CharField(max_length = 100,
                               required = True,
                               label = 'Логин',
                               widget= forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(max_length=100,
                               label = 'Пароль',
                               required = True,
                               widget= forms.PasswordInput(attrs={'class': 'form-input'}))
    


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label = 'Логин')
    password1 = forms.CharField(label = 'Пароль')
    password2 = forms.CharField(label = 'Повтор пароля')
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email','first_name', 'last_name']
        labels = {
            'email': "E-mail",
            'first_name':'Имя',
            'last_name':'Фамилия',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if(cd['password1'] != cd['password2']):
            raise forms.ValidationError("Введенные пароли не совпадают")
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if(User.objects.filter(email = email).exists()):
            raise forms.ValidationError('Пользователь с таким email существует')
        return email
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if(User.objects.filter(username = username).exists()):
            raise forms.ValidationError("Пользователь с таким именем уже существует")
        return username