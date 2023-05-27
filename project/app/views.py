from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "app/dashboard.html"


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = "app/settings.html"
