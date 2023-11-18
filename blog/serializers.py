from rest_framework import serializers

from .models import Author, Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # fields = ['title', 'body', 'author_id', 'id']
        fields = ['title', 'body', 'id']

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title) 
        instance.body = validated_data.get('body', instance.body) 
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'age', 'id']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ['body', 'author_id', 'blog_id', 'id']
        fields = ['body', 'blog_id', 'id']
