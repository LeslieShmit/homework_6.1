from django import forms
from django.core.exceptions import ValidationError

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

