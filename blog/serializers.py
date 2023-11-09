from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author_id = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['title', 'body', 'id', 'author_id']

    def get_author_id(self, obj):
        return obj.author_id

