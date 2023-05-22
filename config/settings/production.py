# type: ignore
import logging
import socket

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from .base import *  # noqa F403
from .base import env

# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": env("DB_FILE", default="/databases/db.sqlite3"),
        "ATOMIC_REQUESTS": True,
    },
}

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": env("CACHE_DIR", default="/storage/cache"),
    }
}

# SECURITY
# ------------------------------------------------------------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS",
    default=["app.project.com", "health.check"],
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

# MEDIA
# ------------------------------------------------------------------------------
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
# TODO adjust project name
AWS_STORAGE_BUCKET_NAME = "project"
AWS_LOCATION = "media"
AWS_S3_REGION_NAME = "eu-central-1"
AWS_S3_FILE_OVERWRITE = False
# TODO adjust project name
AWS_STORAGE_BUCKET_NAME = "project"
AWS_LOCATION = "media"
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    },
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}

# QUEUE
# ------------------------------------------------------------------------------
HUEY = (
    {
        "huey_class": "huey.SqliteHuey",  # Huey implementation to use.
        "name": DATABASES["default"]["NAME"],  # Use db name for huey.
        "results": True,  # Store return values of tasks.
        "store_none": False,  # If a task returns None, do not save to results.
        "immediate": False,  # If DEBUG=True, run synchronously.
        "utc": True,  # Use UTC for all times internally.
        "filename": env("DB_FILE_QUEUE", default="/databases/huey.sqlite3"),
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
    if not env.bool("DISABLE_HUEY", default=False)
    else {"huey_class": "huey.BlackHoleHuey"}
)

# ADMIN
# ------------------------------------------------------------------------------
ADMIN_URL = env("DJANGO_ADMIN_URL", default="admin")

# EMAIL
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["anymail"]  # noqa F405
EMAIL_BACKEND = "anymail.backends.postmark.EmailBackend"
ANYMAIL = {
    "POSTMARK_SERVER_TOKEN": env("POSTMARK_SERVER_TOKEN"),
}
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Josef <josef@project.com>",
)
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

# COMPRESSION
# ------------------------------------------------------------------------------
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

# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d"
                " %(message)s"
            ),
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        # Errors logged by the SDK itself
        "sentry_sdk": {"level": "ERROR", "handlers": ["console"], "propagate": False},
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

# SENTRY
# ------------------------------------------------------------------------------
SENTRY_DSN = env("SENTRY_DSN")
SENTRY_LOG_LEVEL = env.int("DJANGO_SENTRY_LOG_LEVEL", logging.INFO)

sentry_logging = LoggingIntegration(
    level=SENTRY_LOG_LEVEL,
    event_level=logging.ERROR,
)

integrations = [
    sentry_logging,
    DjangoIntegration(),
]

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=integrations,
    environment=env("SENTRY_ENVIRONMENT", default="production"),
    traces_sample_rate=env.float("SENTRY_TRACES_SAMPLE_RATE", default=0.2),
    send_default_pii=True,
)

# STRIPE
# ------------------------------------------------------------------------------
STRIPE_LIVE_SECRET_KEY = env("STRIPE_LIVE_SECRET_KEY")
STRIPE_TEST_SECRET_KEY = env("STRIPE_TEST_SECRET_KEY")
STRIPE_LIVE_PUBLIC_KEY = "pk_test_51N4QRqHxaE28n4C1woHehEHOlnHxzRshtAd2m0I7HQvswZkDSGUHkU2Ycdu1rYtudACzk1NilQk1TAlxF6PFi0o200rqdo83Vw"  # noqa
STRIPE_LIVE_MODE = False
DJSTRIPE_WEBHOOK_SECRET = env("DJSTRIPE_WEBHOOK_SECRET")

# CUSTOM
# ------------------------------------------------------------------------------
