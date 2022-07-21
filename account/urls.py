import django.conf.urls 
from django.urls import path
from .api import RegisterApi, UserRetrieveApi

urlpatterns = [
    path('api/register/', RegisterApi.as_view()),
    path('user/<str:username>/', UserRetrieveApi.as_view())
]