from django.core.management.base import BaseCommand

from django.contrib.sites.models import Site

class Command(BaseCommand):
    help = 'Creates default site in the sites app and a default admin user'

    def handle(self, *args, **kwargs):
        Site.objects.create(
            domain='{{cookiecutter.domain_name}}',
            name='{{cookiecutter.domain_name}}'
        )
        User.objects.create(
            email='admin@example.com',
            username='admin',
            password='password'
        )
