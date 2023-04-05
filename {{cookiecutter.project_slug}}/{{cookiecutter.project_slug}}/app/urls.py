from django.urls import path

from {{cookiecutter.project_slug}}.app.views import IndexView

app_name = "app"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
