from django.urls import path

from .views import DashboardView, SettingsView

app_name = "app"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("settings/", SettingsView.as_view(), name="settings"),
]
