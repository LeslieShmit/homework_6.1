from django import forms
from django.core.exceptions import ValidationError
import os

from .models import Product

restricted_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите наименование товара'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите описание товара'})
        self.fields['image'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите стоимость товара'})
        self.fields['is_available'].widget.attrs.update(
            {'class': 'form-check-input'})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for el in restricted_words:
            if name.lower().find(el) != -1:
                raise ValidationError(f'Наименование товара не может содержать слово {el}.')
        return name

    def clean_description(self):
        description  = self.cleaned_data.get('description')
        for el in restricted_words:
            if description.lower().find(el) != -1:
                raise ValidationError(f'Описание товара не может содержать слово {el}.')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Стоимость не может быть меньше или равна нулю.')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            valid_mime_types = ['image/jpeg', 'image/png']
            if image.content_type not in valid_mime_types:
                raise ValidationError('Допустимы только изображения в формате JPEG или PNG.')

            ext = os.path.splitext(image.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png']:
                raise ValidationError('Файл должен иметь расширение .jpg, .jpeg или .png.')

            max_size = 5 * 1024 * 1024
            if image.size > max_size:
                raise ValidationError('Размер файла не должен превышать 5 МБ.')

        return image


