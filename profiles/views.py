from profiles.serializers import ProfileSerializer
from .models import Profile
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
# def create_profile(request):
#     if request.method=='POST':

# def get_profile(request):
#     return JsonResponse([item.name for item in Profile.objects.all()], safe=False)


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
