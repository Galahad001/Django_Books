from django.shortcuts import render

from .models import Book
from django.views.generic import DetailView

def home(request):
    book = Book.objects.all()
    context = {'book':book}
    return render(request, 'book/home.html', context)


class PostsView(DetailView): # Класс динамических страниц,наслед. от DetailView
    model = Book             # Указать модель с которой работаем
    template_name = 'book/about_the_book.html' #Указать какой шаблон будет обрабатывать
    context_object_name = 'book' #Ключ для передачи в шаблон
# Create your views here.
