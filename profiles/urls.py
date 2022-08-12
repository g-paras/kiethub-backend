from django.urls import path, include
from rest_framework import routers

from profiles.views import ProfileView, follow_unfollow_profile, search_profile

router = routers.DefaultRouter()
router.register("", ProfileView)

urlpatterns = [
    path("", include(router.urls)),
    path("action/follow-unfollow/", follow_unfollow_profile, name="follow-unfollow"),
    path("v1/search/", search_profile, name="search-profile"),
]
