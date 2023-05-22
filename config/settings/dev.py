from .base import *  # noqa F403
from .base import env

DEBUG = True

SECRET_KEY = "LJPhQzD2G6GRAXkQKlDxYCu6OJbzHu38aH6cdiQhcvS3cyA7LUP5sS27bkgiB3lN"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

STRIPE_TEST_SECRET_KEY = env("STRIPE_TEST_SECRET_KEY")

INSTALLED_APPS += ["debug_toolbar"]  # noqa F405

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2", "localhost"]
