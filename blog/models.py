from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=155)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.name}, {self.age}'

class Blog(models.Model):
    title = models.CharField(max_length=155)
    body = models.CharField(max_length=255)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')

    def __str__(self):
        return f'{self.author_id} - {self.title}: {self.body}'

