# Generated by Django 4.2.7 on 2023-11-09 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='author',
            new_name='author_id',
        ),
    ]