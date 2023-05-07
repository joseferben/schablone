from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site


class Command(BaseCommand):
    help = "Gets the project Site and adjusts the domain."

    def handle(self, *args, **options):
        if settings.DEBUG:
            print("Adjusting Site")
            s = Site.objects.get(domain="www.{{cookiecutter.domain_name}}")
            s.domain = "localhost"
            s.save()
        else:
            raise Exception("This command can only be run in DEBUG mode.")
