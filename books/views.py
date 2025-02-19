from django.shortcuts import render
from .models import Book

def getAllBook(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {'libros': books})
