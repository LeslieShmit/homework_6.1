from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', help_text='Введите заголовок')
    content = models.TextField(verbose_name='Содержимое', null=True, blank=True, help_text='Тут должен быть текст вашей статьи')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Превью',
                              help_text='Загрузите изображение для превью')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Стоимость',
                                help_text='Введите стоимость товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации', help_text='Укажите, была ли статья опубликована')
    views_counter = models.PositiveIntegerField(verbose_name='Счетчик просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['created_at',]