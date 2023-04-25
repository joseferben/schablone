from django import http
from django.views.generic import TemplateView


class AuthedHttpRequest(http.HttpRequest):
    user: User  # type: ignore [assignment]


class IndexView(TemplateView):
    template_name = "app/index.html"
