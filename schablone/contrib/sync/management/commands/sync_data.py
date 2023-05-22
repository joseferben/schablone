import os
import subprocess
from pathlib import Path

import environ
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Gets the first Site and adjusts the host and port."

    def handle(self, *args, **options):
        if settings.DEBUG:
            env = environ.Env()
            env.read_env(os.path.join(settings.BASE_DIR, ".env"))
            print("Remove db.sqlite3")
            media_dir = Path(settings.MEDIA_ROOT)
            for f in ["db.sqlite3", "db.sqlite3-shm", "db.sqlite3-wal"]:
                try:
                    os.remove(f)
                except FileNotFoundError:
                    pass

            print("Restore db.sqlite3 from litestream")
            subprocess.run(
                [
                    "litestream",
                    "restore",
                    "--config",
                    "etc/litestream.yml",
                    "db.sqlite3",
                ],
                check=True,
            )

            print("Syncing media")
            subprocess.run(
                [
                    "aws",
                    "s3",
                    "cp",
                    f"s3://{env('AWS_STORAGE_BUCKET_NAME')}/{env('AWS_LOCATION')}",
                    media_dir,
                    "--recursive",
                ],
                check=True,
            )
        else:
            raise Exception("This command can only be run in DEBUG mode.")
