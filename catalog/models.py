from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование категории', help_text='Введите наименование категории')
    description = models.TextField(verbose_name='Описание', null=True, blank=True,
                                   help_text='Введите описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name',]


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование товара', help_text='Введите наименование товара')
    description = models.TextField(verbose_name='Описание', null=True, blank=True, help_text='Введите описание товара')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Изображение',
                              help_text='Загрузите изображение товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Стоимость',
                                help_text='Введите стоимость товара')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name',]
