from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)

class BookInline(admin.TabularInline):
    model = Book

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] # Changes the view of the vields in admin

    inlines = [BookInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# This class calls to the models
class BooksInstanceInline(admin.TabularInline): # https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre') # display_genre needs to be defined as a function in models.py. This needs to be done with many to many fields.

    # This is calls to the class that calls to the models.
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    list_display = ('book', 'status', 'due_back', 'id')

    # Changes the sections of the view in admin
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(Genre)
admin.site.register(Language)