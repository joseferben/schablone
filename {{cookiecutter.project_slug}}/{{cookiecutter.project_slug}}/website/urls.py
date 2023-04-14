from django.conf import settings
from django.urls import path
from django.views.generic import RedirectView, TemplateView

from .faqs import faqs

app_name = "website"

urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="website/index.html", extra_context={"faqs": faqs}
        ),
        name="index",
    ),
    path(
        "privacy",
        TemplateView.as_view(template_name="website/privacy.html"),
        name="privacy",
    ),
    path(
        "favicon.ico",
        RedirectView.as_view(url=settings.STATIC_URL + "favicon.ico"),
    ),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="website/robots.txt", content_type="text/plain"
        ),
    ),
]
