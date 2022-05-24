from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.models import Post
from posts.serializers import PostSerializer
# from posts.pagination import CustomPageNumberPagination
# Create your views here.
from rest_framework.pagination import PageNumberPagination
from .paginations import MyPageNumberPagination

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class= MyPageNumberPagination
    permission_classes = (IsAuthenticatedOrReadOnly, )