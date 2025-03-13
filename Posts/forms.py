from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    categories =[
        ('Спорт', 'Спорт'),
        ('Политика', 'Политика'),
        ('О себе', 'О себе'),
    ]
    category = forms.MultipleChoiceField(label = 'Категории', choices= categories)

    class Meta:
        model = Post
        fields = ['title', 'text', 'category']
        widgets = {
            'title': forms.TextInput(),
            'text': forms.Textarea(),
        }
        labels = {
            'title': 'Заголовок',
            'text': 'Текст поста',
            'categoey': 'Категория',
        }

