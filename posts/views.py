from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView, RetrieveAPIView

from posts.models import Post
from posts.serializers import PostSerializer
from .paginations import MyPageNumberPagination


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    pagination_class = MyPageNumberPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostRetrieveView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class UserPostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        user_id = self.kwargs["pk"]
        queryset = self.model.objects.filter(author=user_id)
        return queryset
