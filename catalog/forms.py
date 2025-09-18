from django import forms
from django.core.exceptions import ValidationError
import os

from .models import Product
from .mixins import FormStyleMixin

restricted_words = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар',
]


class ProductForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at', 'owner']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for el in restricted_words:
            if el in name.lower():
                raise ValidationError(f'Наименование товара не может содержать слово "{el}".')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for el in restricted_words:
            if el in description.lower():
                raise ValidationError(f'Описание товара не может содержать слово "{el}".')
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

class ProductModeratorForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_published', ]
