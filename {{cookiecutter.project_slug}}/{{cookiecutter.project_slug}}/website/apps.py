from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = "{{cookiecutter.project_slug}}.website"
    verbose_name = "Website"
