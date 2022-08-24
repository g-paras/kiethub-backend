from django.urls import path
from .api import RegisterApi, UserListApi, UserRetrieveApi
from .views import (
    check_username,
    reqeust_reset_password,
    resent_email_verification,
    reset_password,
    verify_email,
)

app_name = "accounts"
urlpatterns = [
    path("users/", UserListApi.as_view()),
    path("api/register/", RegisterApi.as_view()),
    path(
        "request-reset-password/", reqeust_reset_password, name="request-reset-password"
    ),
    path(
        "re-email-verification/",
        resent_email_verification,
        name="resent-email-verification",
    ),
    path("user/<str:username>/", UserRetrieveApi.as_view()),
    path("check/user/<str:username>/", check_username, name="check-username"),
    path("email-verification/<uuid:token>/", verify_email, name="verify-email"),
    path("reset-password/<uid>/<token>", reset_password, name="reset-password"),
]
