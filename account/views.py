from django.http import JsonResponse
from django.contrib.auth.models import User
from django.utils.encoding import smart_bytes
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.decorators import api_view, permission_classes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from uuid import uuid4

from .models import AuthModel
from .utils import send_verification_email, send_reset_password_email


# Create your views here.
@api_view(["GET"])
def check_username(request, username):
    is_used = User.objects.filter(username=username).exists()

    return JsonResponse({"available": not is_used}, status=200)


@api_view(["GET"])
def verify_email(reqeust, token):
    user = User.objects.filter(auth_status__auth_token=token)

    if not user.exists():
        return JsonResponse({"message": "Token is invlaid", "status": "fail"})

    user = user.first()
    if user.auth_status.is_verified:  # type: ignore
        return JsonResponse({"message": "Email already verified", "status": "success"})

    user.auth_status.is_verified = True  # type: ignore
    user.auth_status.save()  # type: ignore

    return JsonResponse(
        {"message": "Email verification successfull", "status": "success"}
    )


@api_view(["POST"])
def resent_email_verification(request):
    """
    content type must be urlencoded otherwise email will be none
    """
    email = request.POST.get("email", "")

    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({"message": "Invalid email", "status": "error"})

    user = User.objects.filter(email=email)
    if not user.exists():
        return JsonResponse({"message": "User not found", "status": "error"})

    user = user.first()

    auth_model = AuthModel.objects.get(user=user)
    auth_model.auth_token = uuid4()
    auth_model.save()

    send_verification_email(user)
    return JsonResponse(
        {"message": "Verification mail sent successfully", "status": "success"}
    )


@api_view(["POST"])
def reqeust_reset_password(request):
    """
    post method to process password reset request and send customized link to reset password
    """
    email = request.POST.get("email", "")

    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({"message": "Invalid email", "status": "error"})

    user = User.objects.filter(email=email)
    if not user.exists():
        return JsonResponse({"message": "No account registered", "status": "fail"})

    user = user.first()
    token = PasswordResetTokenGenerator().make_token(user)  # type: ignore
    uid = urlsafe_base64_encode(smart_bytes(user.id))  # type: ignore

    send_reset_password_email(user, uid, token)

    return JsonResponse(
        {"message": "Mail with password reset link has been sent.", "status": "success"}
    )


@api_view(["POST"])
def reset_password(request, uid, token):
    id = urlsafe_base64_decode(uid)

    try:
        user = User.objects.get(pk=id)
    except ObjectDoesNotExist:
        return JsonResponse({"message": "No user found", "status": "error"})

    if not PasswordResetTokenGenerator().check_token(user, token):
        return JsonResponse({"message": "Invalid token found", "status": "error"})

    password1 = request.POST.get("password1", "")
    password2 = request.POST.get("password2", "")

    # todo: validate password
    if password1 != password2:
        return JsonResponse({"message": "password does not match", "status": "error"})
    elif len(password1) < 8:
        return JsonResponse(
            {"Password": "should be atleast 8 digits long", "status": "error"}
        )

    user.set_password(password1)
    user.save()

    return JsonResponse(
        {"message": "Password has been reset successfully", "status": "success"}
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user

    old_password = request.POST.get("old-password")
    new_password = request.POST.get("new-password")
    new_password_re = request.POST.get("new-password-re")

    if not user.check_password(old_password):
        return JsonResponse({"message": "Incorrect Password", "status": "error"})

    if new_password != new_password_re:
        return JsonResponse({"message": "Password does not match", "status": "error"})

    user.set_password(new_password)
    user.save()

    return JsonResponse(
        {"message": "Password changes successfully", "status": "success"}
    )
