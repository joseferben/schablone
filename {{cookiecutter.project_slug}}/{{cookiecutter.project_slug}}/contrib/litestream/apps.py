from django.apps import AppConfig


class LitestreamConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{cookiecutter.project_slug}}.contrib.litestream"

    def ready(self):
        try:
            import {{cookiecutter.project_slug}}.contrib.litestream.signals  # noqa F401
        except ImportError:
            pass
