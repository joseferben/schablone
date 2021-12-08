from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{cookiecutter.project_slug}}.main"

    def ready(self):
        # flake8: noqa
        import {{cookiecutter.project_slug}}.main.receivers
