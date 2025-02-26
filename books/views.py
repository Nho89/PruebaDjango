from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import FormBook


@api_view(['GET'])
def getAllBook(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
    # return render(request, 'books/books.html', {'libros': books})


@api_view(['POST'])
def createBook(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()  
            return redirect('books')  
        else:
            return Response(serializer.errors, status=400)
    return render(request, 'books/books.html', {'form': serializer})

@api_view(['PUT'])
def updateBook(request, id):
    book = get_object_or_404(Book, pk=id)
    serializer = BookSerializer(book, data=request.data, partial=True)  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)  
    return Response(serializer.errors, status=400) 

    
        