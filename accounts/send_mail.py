from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_message_to_email(user):
    context = {
        "email": user.email,
        "domain": "http://127.0.0.1:3000",
        "activation_code": user.activation_code
    }
    message = render_to_string("email.html", context)
    finally_message = strip_tags(message)
    send_mail(
        'Активация аккаунта',
        finally_message,
        settings.EMAIL_HOST_USER,
        [user.email, ],
        html_message=message,
    )
