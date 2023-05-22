from django.contrib.auth import get_user_model
from herald import registry
from herald.base import EmailNotification

User = get_user_model()


@registry.register_decorator()
class WelcomeEmail(EmailNotification):
    template_name = "welcome"
    subject = "Welcome to project"

    def __init__(self, user, link):
        self.context = {"user": user, "link": link}
        self.to_emails = [user.email]

    @staticmethod
    def get_demo_args():
        return [
            User.objects.order_by("?")[0],
            "https://example.com/token=adfasdfasdf",
        ]
