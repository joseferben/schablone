# type: ignore
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "{{project_name}}.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import {{project_name}}.users.signals  # noqa F401
        except ImportError:
            pass
