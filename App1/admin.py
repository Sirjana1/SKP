from django.contrib import admin
from App1.models import Author, Book, Feedback, CustomerID
from .models import Feedback, CustomerID, Item, Members, BlogPost, BolckPostCreaterDetail

admin.site.register(Feedback),
admin.site.register(CustomerID),
admin.site.register(Item),
admin.site.register(Members),
admin.site.register(BlogPost),
admin.site.register(BolckPostCreaterDetail)




class BookInlineAdmin(admin.TabularInline):  # Fix here: TabularInline, not TabularInLine
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInlineAdmin]

# admin.site.register(Author, AuthorAdmin, Feedback)



