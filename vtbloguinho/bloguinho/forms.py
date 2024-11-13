from django import forms
from .models import NewPost


class NewForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ['image', 'title', 'content', 'expires']
        widgets = {
            'expires': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'image': 'Imagem',
            'title': 'Título',
            'content': 'Conteúdo',
            'expires': 'Expira em',
        }