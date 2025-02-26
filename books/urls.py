from django.contrib import admin
from django.urls import path
from .views import getAllBook, createBook, updateBook
from . import views

urlpatterns = [
    path('books/', views.getAllBook, name='books'),
    path('books/create/', views.createBook, name='create_books'),
    path('books/update/<int:id>', views.updateBook, name='update_books'),
]