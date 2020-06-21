from django import forms
from django.forms.widgets import TextInput, FileInput
from .models import ImageModel
from django.forms import ValidationError


class ImageModelForm(forms.ModelForm):

    class Meta:
        model = ImageModel
        fields = [
            'title',
            'file_url',
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите низвание фотографии'}),
            'file_url': FileInput(attrs={'class': 'form-control', 'placeholder': 'Загрузить фото'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if ImageModel.objects.filter(title=title):
            raise ValidationError('Файл с таким именем уже существует.')
        return title
