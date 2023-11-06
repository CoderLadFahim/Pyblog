from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        field = ['title', 'body']
        fields = ['title', 'body', 'id']

