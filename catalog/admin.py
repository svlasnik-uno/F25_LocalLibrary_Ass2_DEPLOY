from django.contrib import admin
from .models import Book, Author, Genre, BookInstance

# Register your models here.

admin.site.register(Author)
admin.site.register(Genre)

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','author', 'get_genres')

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])
    get_genres.short_description = 'Genres'

admin.site.register(Book, BookAdmin)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )



