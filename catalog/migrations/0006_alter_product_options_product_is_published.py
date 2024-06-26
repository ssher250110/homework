# Generated by Django 4.2.2 on 2024-04-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_blog_owner_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category', 'pk'], 'permissions': [('cancel_is_published', 'cancel is_published'), ('edit_description', 'edit description'), ('edit_category', 'edit category')], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]
