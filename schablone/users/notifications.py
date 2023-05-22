from django.contrib.auth import get_user_model
from herald import registry
from herald.base import EmailNotification

from .shortcuts import get_magic_link

User = get_user_model()


@registry.register_decorator()
class LoginEmail(EmailNotification):
    template_name = "login"
    subject = "Magic link"

    def __init__(self, user):
        self.context = {"user": user, "link": get_magic_link(user)}
        self.to_emails = [user.email]

    @staticmethod
    def get_demo_args():
        return [
            User.objects.order_by("?")[0],
        ]
