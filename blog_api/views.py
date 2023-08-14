from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from blog.models import Category, Post
from .serializers import CategorySerializer, PostSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
