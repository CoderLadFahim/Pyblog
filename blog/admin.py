from django.contrib import admin
from .models import Blog, Author, Comment

class BlogAdmin(admin.ModelAdmin):
    read_only = ('id')

class AuthorAdmin(admin.ModelAdmin):
    read_only = ('id')

class CommentAdmin(admin.ModelAdmin):
    read_only = ('id')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
