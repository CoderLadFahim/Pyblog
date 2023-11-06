from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import api_view 


@api_view(['GET', 'POST'])
def blog_list(req):
    if req.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return JsonResponse({'blogs': serializer.data }, safe=False)
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


