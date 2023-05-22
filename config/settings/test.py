from .base import *  # noqa

SECRET_KEY = "Y0HhZ0tDiPKIzwZLFlIhHtzHhbrpfDxb0tFsEp0AiQn0ALdVyiDDOULctHZhCX4d"

HUEY = {
    "huey_class": "huey.SqliteHuey",
    "immediate": True,
}

TEST_RUNNER = "django.test.runner.DiscoverRunner"

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

STORAGES = {
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"}
}
