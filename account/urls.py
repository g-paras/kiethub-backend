from django.urls import path
from .api import RegisterApi, UserListApi, UserRetrieveApi
from .views import check_username

app_name = "accounts"
urlpatterns = [
    path("api/register/", RegisterApi.as_view()),
    path("user/<str:username>/", UserRetrieveApi.as_view()),
    path("users/", UserListApi.as_view()),
    path("check/user/<str:username>/", check_username, name="check-username"),
]
