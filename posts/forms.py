from django import forms
from tinymce.widgets import TinyMCE
from .models import Post


class PostForm(forms.ModelForm):
    titulo = forms.CharField()

    class Meta:
        model = Post
        fields = ('titulo', 'contenido')
