from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование категории',
                            help_text='Введите наименование категории')
    description = models.TextField(verbose_name='Описание', null=True, blank=True,
                                   help_text='Введите описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name', ]


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование товара')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Изображение',
                              help_text='Загрузите изображение товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Стоимость')
    is_available = models.BooleanField(default=True, verbose_name='Наличие товара',
                                       help_text='Укажите, есть ли товар в наличии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name', ]


class Contact(models.Model):
    country = models.CharField(max_length=50, verbose_name='Страна', help_text='Введите страну')
    tin = models.CharField(max_length=50, verbose_name='ИНН', help_text='Введите ИНН')
    address = models.TextField(verbose_name='Адрес', help_text='Введите адрес')

    def __str__(self):
        return f'Контактные данные в стране {self.country} с ИНН {self.tin}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ['country', ]
