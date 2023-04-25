from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.urls import reverse
from sesame.utils import get_query_string


def get_magic_link(user: AbstractUser) -> str:
    """
    Return the magic link for this user that can be used to log in.
    """
    path = reverse("users:login")
    domain = "localhost:8000" if settings.DEBUG else Site.objects.get_current().domain
    protocol = "http" if settings.DEBUG else "https"
    link = f"{protocol}://{domain}{path}"
    link += get_query_string(user)
    return link
