from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def getAllBook(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {'libros': books})

def createBook(request):
    if request.method == 'POST':
        form = formBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = formBook()
    return render(request, 'books/createBook.html', {'form': form})

def updateBook(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'PUT':
        form = formBook(request.PUT, instance = book)
        if form.is_valid():
            form.save()
            return redirect('books')
        else:
            form = formBook(instance = book)
        return render(request, 'books/updateBook.html', {'form': form, 'libro': book})