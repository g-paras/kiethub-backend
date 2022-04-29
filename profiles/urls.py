from django.urls import path, include
from rest_framework import routers

from profiles.views import ProfileView

router = routers.DefaultRouter()
router.register('profile', ProfileView)

urlpatterns = [
    # path('', get_profile),
    path('', include(router.urls)),
]