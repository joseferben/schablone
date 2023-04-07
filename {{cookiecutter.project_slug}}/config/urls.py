from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path(
        "favicon.ico",
        RedirectView.as_view(url=settings.STATIC_URL + "favicon.ico"),
    ),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(settings.ADMIN_URL, admin.site.urls),
    path("users/", include("{{cookiecutter.project_slug}}.users.urls", namespace="users")),
    path("app/", include("{{cookiecutter.project_slug}}.app.urls", namespace="app")),
    path("ht/", include("health_check.urls")),
    path("hijack/", include("hijack.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
