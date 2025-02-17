from django.contrib import admin
from .models import Book
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','description' , 'publish_date', 'isbn')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('publish_date')