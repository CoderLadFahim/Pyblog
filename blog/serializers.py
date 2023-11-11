from rest_framework import serializers

from .models import Author, Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # fields = ['title', 'body', 'author_id', 'id']
        fields = ['title', 'body', 'id']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'age', 'id']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ['body', 'author_id', 'blog_id', 'id']
        fields = ['body', 'blog_id', 'id']
