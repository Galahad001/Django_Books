# Generated by Django 4.2.1 on 2023-05-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название книги')),
                ('content', models.TextField(verbose_name='Текст книги')),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
