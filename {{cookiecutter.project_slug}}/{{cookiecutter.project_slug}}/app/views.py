from django import http
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from {{cookiecutter.project_slug}}.users.models import User


class AuthedHttpRequest(http.HttpRequest):
    user: User  # type: ignore [assignment]


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "app/index.html"
