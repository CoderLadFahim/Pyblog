from django.http import JsonResponse
from .models import Blog
from .serializers import BlogSerializer


def get_blogs(req):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return JsonResponse(serializer.data, safe=False)

