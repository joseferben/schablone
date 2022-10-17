from django.urls import path

from {{cookiecutter.project_slug}}.app.views import DashboardView

app_name = "app"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
]
