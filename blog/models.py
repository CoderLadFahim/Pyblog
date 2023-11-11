from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=155)
    age = models.IntegerField()

class Blog(models.Model):
    title = models.CharField(max_length=155)
    body = models.CharField(max_length=255)
    # author_id = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='blogs')

class Comment(models.Model):
    body = models.CharField(max_length=155)
    # author_id = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, related_name='author')
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False, related_name='comments')
