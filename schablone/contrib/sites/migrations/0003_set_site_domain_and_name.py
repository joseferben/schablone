"""
To understand why this file is here, please read:

http://cookiecutter-django.readthedocs.io/en/latest/faq.html#why-is-there-a-django-contrib-sites-directory-in-cookiecutter-django
"""
from django.conf import settings
from django.db import migrations


def _update_or_create_site_with_sequence(site_model, connection, domain, name):
    """Update or create the site with default ID and keep the DB sequence in sync."""
    site, created = site_model.objects.update_or_create(
        id=settings.SITE_ID,
        defaults={
            "domain": domain,
            "name": name,
        },
    )


def update_site_forward(apps, schema_editor):
    """Set site domain and name."""
    Site = apps.get_model("sites", "Site")
    _update_or_create_site_with_sequence(
        Site,
        schema_editor.connection,
        "project.com",
        "project",
    )


def update_site_backward(apps, schema_editor):
    """Revert site domain and name to default."""
    Site = apps.get_model("sites", "Site")
    _update_or_create_site_with_sequence(
        Site,
        schema_editor.connection,
        "project.com",
        "project.com",
    )


class Migration(migrations.Migration):
    dependencies = [("sites", "0002_alter_domain_unique")]

    operations = [migrations.RunPython(update_site_forward, update_site_backward)]
