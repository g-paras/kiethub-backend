from django.shortcuts import render
from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer

# Create your views here.
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer