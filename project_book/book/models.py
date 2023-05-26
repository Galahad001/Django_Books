from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название книги')
    content = models.TextField(verbose_name='Текст книги')
    description = models.TextField(verbose_name='Краткое описание')
    author = models.CharField(max_length=50, verbose_name='Автор')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
        
# Create your models here.
