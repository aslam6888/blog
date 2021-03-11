from django.shortcuts import render,get_object_or_404
from .models import blog
# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer


class BlogList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        blogs = blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)