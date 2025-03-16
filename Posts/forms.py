from django import forms
from .models import Post, TagPost


class PostForm(forms.ModelForm):
    tag = forms.ModelChoiceField(queryset= TagPost.objects.all(), label = 'Теги', empty_label='Теги не выбраны')

    class Meta:
        model = Post
        fields = ['title', 'text', 'tag']
        widgets = {
            'title': forms.TextInput(),
            'text': forms.Textarea(),
        }
        labels = {
            'title': 'Заголовок',
            'text': 'Текст поста',
            'categoey': 'Категория',
        }

