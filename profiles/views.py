from django.http import JsonResponse
from profiles.serializers import ProfileSerializer
from django.contrib.auth.decorators import login_required
from .models import Profile
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.db.models import Q

# Create your views here.
# def create_profile(request):
#     if request.method=='POST':

# def get_profile(request):
#     return JsonResponse([item.name for item in Profile.objects.all()], safe=False)


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(["GET"])
def search_profile(request):
    query = request.GET.get("q")
    if not query:
        return JsonResponse([], safe=False)
    result = Profile.objects.filter(
        Q(first_name__icontains=query)
        | Q(last_name__icontains=query)
        | Q(user__username__icontains=query)
    )
    serialized_res = ProfileSerializer(result, many=True)
    return JsonResponse(serialized_res.data, safe=False)


@api_view(["POST"])
@login_required
def follow_unfollow_profile(request):
    user_profile = request.user.profile
    pk = request.POST.get("profile_id", None)
    print(request.POST["profile_id"])
    if pk is None:
        return JsonResponse({"status": "error", "mssg": "user_id is missing"})
    following_user = User.objects.filter(pk=pk)
    if not following_user.exists():
        return JsonResponse({"status": "error", "msg": "user not found"})
    else:
        following_user = following_user.first()
    if user_profile.user == following_user:
        return JsonResponse({"error": "error", "msg": "can not follow yourself"})
    if following_user in user_profile.following.all():
        user_profile.following.remove(following_user)
        msg = "successfully unfollowed"
    else:
        user_profile.following.add(following_user)
        msg = "successfully followed"
    return JsonResponse({"status": "success", "msg": msg})
