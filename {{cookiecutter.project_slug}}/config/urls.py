from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        "users/", include("{{cookiecutter.project_slug}}.users.urls", namespace="users")
    ),
    path("app/", include("{{cookiecutter.project_slug}}.app.urls", namespace="app")),
    path("ht/", include("health_check.urls")),
    path("hijack/", include("hijack.urls")),
    path("", include("{{cookiecutter.project_slug}}.website.urls", namespace="website")),
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
    urlpatterns += [path("herald/", include("herald.urls"))]
