from django.urls import path

from {{project_name}}.app.views import DashboardView

app_name = "app"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
]
