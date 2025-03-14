from django import forms

class LoginUserForm(forms.Form):
    username = forms.CharField(max_length = 100,
                               required = True,
                               label = 'Логин',
                               widget= forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(max_length=100,
                               label = 'Пароль',
                               required = True,
                               widget= forms.PasswordInput(attrs={'class': 'form-input'}))
    
