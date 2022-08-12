# from django.shortcuts import render
from django.contrib.auth.models import User

# from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
def check_username(request, username):
    is_used = User.objects.filter(username=username).exists()

    return JsonResponse({"available": not is_used}, status=200)
