from django.urls import path
from .api import RegisterApi, UserListApi, UserRetrieveApi

urlpatterns = [
    path('api/register/', RegisterApi.as_view()),
    path('user/<str:username>/', UserRetrieveApi.as_view()),
    path('users/', UserListApi.as_view())
]