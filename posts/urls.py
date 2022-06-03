from django.urls import path, include
from rest_framework import routers

from .views import PostView, UserPostView

router = routers.DefaultRouter()
router.register('', PostView)

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:pk>/', UserPostView.as_view(), name='get-user-post'),
]