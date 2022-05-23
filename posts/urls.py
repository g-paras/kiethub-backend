from django.urls import path, include
from rest_framework import routers

from .views import PostView

router = routers.DefaultRouter()
router.register('', PostView)

urlpatterns = [
    # path('', get_profile),
    path('', include(router.urls)),
    
]