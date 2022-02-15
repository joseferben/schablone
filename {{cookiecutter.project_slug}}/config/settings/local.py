# flake8: noqa
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MEDIA_ROOT = str(BASE_DIR / "{{cookiecutter.project_slug}}/media")

INSTALLED_APPS = (
    ["whitenoise.runserver_nostatic"]
    + INSTALLED_APPS
    + ["debug_toolbar", "django_browser_reload"]
)

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

Q_CLUSTER = {
    "name": "{{cookiecutter.project_slug}}",
    "sync": False,
    "workers": 4,
    "recycle": 500,
    "timeout": 60,
    "compress": True,
    "save_limit": 250,
    "max_attempts": 3,
    "cpu_affinity": 1,
    "label": "Django Q",
    "redis": REDIS_URL + "/0",
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL + "/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
