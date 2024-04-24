from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    id = models.CharField(primary_key=True, max_length=100, verbose_name='Номер категории')
    name = models.CharField(max_length=100, verbose_name='Категория продукта')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['id', ]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Товар')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория товара')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['category', 'pk', ]


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Короткая метка')
    body = models.TextField(**NULLABLE, verbose_name='Содержимое')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.BooleanField(default=True, verbose_name='Опубликовано')
    view_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Блог продукта')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-created_at', 'product', ]

    def __str__(self):
        return self.title


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number_version = models.FloatField(verbose_name='Номер версии')
    name_version = models.CharField(max_length=100, verbose_name='Название версии')
    is_active_version = models.BooleanField(default=True, verbose_name='Активная версия')

    def __str__(self):
        return f'{self.product}, {self.name_version} - {self.number_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
