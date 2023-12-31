from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Blog, Comment
from .serializers import AuthorSerializer, BlogSerializer, CommentSerializer
from rest_framework.decorators import api_view

from blog import serializers 


@api_view(['GET', 'POST'])
def blog_list(req):
    if req.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif req.method == 'POST':
        serializer = BlogSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def individual_blog(req, id):
    try:
        blog = Blog.objects.get(pk=id)
    except Blog.DoesNotExist as e:
        return Response({'message': 'no blog with that id exists'}, status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif req.method == 'PUT':
        serializer = BlogSerializer(blog, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def comment_list(req, id):
    try:
        blog = Blog.objects.get(pk=id) 
    except Blog.DoesNotExist as e:
        return Response({'message': 'no blog with that id exists'}, status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        comments = blog.comments
        comments_serialized = CommentSerializer(comments, many=True)
        return JsonResponse(comments_serialized.data, safe=False)

    if req.method == 'POST':
        new_comment = {
            'body': req.data.get('body'),
            # 'author_id': req.data.get('author_id'),
            'blog_id': id,
        }
        comment_serializer = CommentSerializer(data=new_comment)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def individual_comment(req, id):
    try:
        comment = Comment.objects.get(pk=id)
    except Comment.DoesNotExist as e:
        return Response({'message': 'no comment with that id exists'}, status=status.HTTP_404_NOT_FOUND)

    comment_serialized = CommentSerializer(comment)

    if req.method == 'GET':
        return JsonResponse(comment_serialized.data, safe=False)

    if req.method == 'PUT':
        comment_serialized = CommentSerializer(comment, data=req.data)
        if comment_serialized.is_valid():
            comment_serialized.save()
            return Response(comment_serialized.data, status=status.HTTP_201_CREATED)
        return HttpResponse(comment_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    if req.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







# SUBJECT TO CHANGE

@api_view(['GET'])
def get_author(req, id):
    try:
        blog = Blog.objects.get(pk=id)
    except Blog.DoesNotExist as e:
        return Response({'message': 'no blog with that id exists'}, status=status.HTTP_404_NOT_FOUND)

    author_serialized = AuthorSerializer(blog.author_id)

    return JsonResponse(author_serialized.data, safe=False)

@api_view(['GET'])
def get_author_list(req):
    authors = Author.objects.all()
    author_serialized = AuthorSerializer(authors, many=True)
    return JsonResponse(author_serialized.data, safe=False)

@api_view(['GET'])
def get_blogs_by_author(req, id):
    try:
        author_in_question = Author.objects.get(pk=id)
    except Author.DoesNotExist as e:
        return Response({'message': 'no author with that id exists'}, status=status.HTTP_404_NOT_FOUND)

    blogs_serialized = BlogSerializer(author_in_question.blogs, many=True)
    return JsonResponse(blogs_serialized.data, safe=False)
