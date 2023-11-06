from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=155)
    body = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.title}: {self.body}'
