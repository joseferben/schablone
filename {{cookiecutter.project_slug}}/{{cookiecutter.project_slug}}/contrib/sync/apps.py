from django.apps import AppConfig


class LocalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{cookiecutter.project_slug}}.contrib.local"
