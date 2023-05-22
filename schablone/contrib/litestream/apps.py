from django.apps import AppConfig


class LitestreamConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "schablone.contrib.litestream"

    def ready(self):
        try:
            import schablone.contrib.litestream.signals  # noqa F401
        except ImportError:
            pass
