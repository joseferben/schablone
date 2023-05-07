from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.site.models import Site


class Command(BaseCommand):
    help = "Gets the first Site and adjusts the host and port."

    def handle(self, *args, **options):
        if settings.DEBUG:
            print("Adjusting Site")
            s = Site.objects.get(hostname="{{cookiecutter.domain_name}}")
            s.hostname = "localhost"
            s.port = 8000
            s.save()
        else:
            raise Exception("This command can only be run in DEBUG mode.")
