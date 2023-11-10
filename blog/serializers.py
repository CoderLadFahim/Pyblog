from rest_framework import serializers

from .models import Author, Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'author_id']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'age']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['body', 'author_id', 'blog_id']
