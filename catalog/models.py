from django.db import models


# Create your models here.
class Category(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
