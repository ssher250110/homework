# Generated by Django 5.0.3 on 2024-04-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]
