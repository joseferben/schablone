"""
With these settings, tests run faster.
"""

from .base import *  # noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="Y0HhZ0tDiPKIzwZLFlIhHtzHhbrpfDxb0tFsEp0AiQn0ALdVyiDDOULctHZhCX4d",
)

HUEY = {
    "huey_class": "huey.SqliteHuey",
    "immediate": True,
}

TEST_RUNNER = "django.test.runner.DiscoverRunner"

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
