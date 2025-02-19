from django.contrib import admin
from django.urls import path
from .views import getAllBook

urlpatterns = [
    path('', getAllBook, name='libros'),
]