from .models import Rest_Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django import forms


class RestArticlesForm(ModelForm):
    class Meta:
        model = Rest_Articles
        fields = ['title', 'food', 'full_text', 'date','tel', 'url','addr']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название ресторана'
            }),
            "food": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кухня'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата открытия'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация о ресторане'
            }),
            "tel": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tелефон'
            }),
            "url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL ресторана'
            }),
            "addr": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
        }

