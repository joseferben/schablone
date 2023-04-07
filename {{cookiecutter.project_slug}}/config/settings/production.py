import socket

from .base import *
from .base import env

# Database settings
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": env("DB_FILE")},
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/tmp/cache",
    }
}

# Security settings
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS",
    default=["www.{{cookiecutter.domain_name}}", "health.check"],
)
# Docker environment like Dokku
ALLOWED_HOSTS.append(socket.getaddrinfo(socket.gethostname(), "http")[0][4][0])
SECURE_REDIRECT_EXEMPT = [r"^ht/", r"^/"]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

# Static and media settings
STATIC_ROOT = "/app/static"
# fmt: off
DEFAULT_FILE_STORAGE = "{{cookiecutter.project_slug}}.contrib.storages.storages.MediaStorage"
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")

# Worker queue settings
HUEY = {
    "huey_class": "huey.SqliteHuey",  # Huey implementation to use.
    "name": DATABASES["default"]["NAME"],  # Use db name for huey.
    "results": True,  # Store return values of tasks.
    "store_none": False,  # If a task returns None, do not save to results.
    "immediate": False,  # If DEBUG=True, run synchronously.
    "utc": True,  # Use UTC for all times internally.
    "filename": env("DB_FILE_QUEUE"),
    "consumer": {
        "workers": 1,
        "worker_type": "thread",
        "initial_delay": 0.1,  # Smallest polling interval, same as -d.
        "backoff": 1.15,  # Exponential backoff using this rate, -b.
        "max_delay": 10.0,  # Max possible polling interval, -m.
        "scheduler_interval": 1,  # Check schedule every second, -s.
        "periodic": True,  # Enable crontab feature.
        "check_worker_health": True,  # Enable worker health checks.
        "health_check_interval": 1,  # Check worker health every second.
    },
}

# Admin settings
ADMIN_URL = env("DJANGO_ADMIN_URL")

# Email settings
INSTALLED_APPS += ["anymail"]  # noqa F405
EMAIL_BACKEND = "anymail.backends.postmark.EmailBackend"
ANYMAIL = {
    "POSTMARK_SERVER_TOKEN": env("POSTMARK_SERVER_TOKEN"),
}
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="{{cookiecutter.project_slug}} <noreply@{{cookiecutter.domain_name}}>",
)
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[{{cookiecutter.project_slug}}]",
)

# Compression settings
COMPRESS_ENABLED = True
COMPRESS_STORAGE = "compressor.storage.GzipCompressorFileStorage"
COMPRESS_URL = STATIC_URL  # noqa F405
COMPRESS_OFFLINE = True
COMPRESS_FILTERS = {
    "css": [
        "compressor.filters.css_default.CssAbsoluteFilter",
        "compressor.filters.cssmin.rCSSMinFilter",
    ],
    "js": ["compressor.filters.jsmin.JSMinFilter"],
}

# Logging & performance settings
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": (
                "%(levelname)s %(asctime)s %(module)s "
                "%(process)d %(thread)d %(message)s"
            )
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
sentry_sdk.init(
    dsn=env("SENTRY_DSN"),
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
