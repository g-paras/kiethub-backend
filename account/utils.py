from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def send_mail_user(user_email, html_message):

    send_mail(
        "Registration Successfull, Verify your email",
        "here is some message",
        "Team KietHub",
        [
            user_email,
        ],
        fail_silently=False,
        html_message=html_message,
    )


def send_verification_email(user):
    """
    Function to send verfication email to a user,
    takes a user as a parameter
    """
    user_email = user.email

    verify_path = reverse(
        "accounts:verify-email", kwargs={"token": user.auth_status.auth_token}
    )

    html_message = render_to_string(
        "email/email_verification.html",
        {"user": user, "path": verify_path, "domain": settings.DOMAIN},
    )

    send_mail_user(user_email, html_message)


def send_reset_password_email(user, uid, token):
    """
    Helper function to send password reset link
    takes user, uid, and token as parameter
    """
    user_email = user.email
    reset_password_path = reverse(
        "accounts:reset-password", kwargs={"uid": uid, "token": token}
    )

    html_message = render_to_string(
        "email/reset_password.html",
        {"user": user, "path": reset_password_path, "domain": settings.DOMAIN},
    )

    send_mail_user(user_email, html_message)
