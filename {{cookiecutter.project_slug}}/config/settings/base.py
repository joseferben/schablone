# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import environ

# Build paths and read env variables
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_DIR = os.path.join(BASE_DIR, "{{cookiecutter.project_slug}}")

env = environ.Env()
env.read_env(os.path.join(PROJECT_DIR, ".env"))

# Basic settings
DEBUG = env.bool("DJANGO_DEBUG", False)
SITE_ID = 1
LOCALE_PATHS = [os.path.join(PROJECT_DIR, "locale")]
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# Django apps
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.storage",
    "health_check.contrib.migrations",
    "health_check.contrib.psutil",
    "widget_tweaks",
    "hijack",
    "huey.contrib.djhuey",
    "compressor",
    "whitenoise.runserver_nostatic",
]
LOCAL_APPS = [
    "{{cookiecutter.project_slug}}.users",
    "{{cookiecutter.project_slug}}.app",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middlewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "hijack.middleware.HijackUserMiddleware",
]

# Django template settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

# Internationalization & language settings
LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_TZ = True
TIME_ZONE = "UTC"

# Database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    },
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
MIGRATION_MODULES = {"sites": "{{cookiecutter.project_slug}}.contrib.sites.migrations"}

# General security settings
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# Authentication settings
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "sesame.backends.ModelBackend",
]
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "app:index"
LOGIN_URL = "users:email_login"
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        )
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
SESAME_MAX_AGE = 300  # 300 seconds = 5 minutes

# Static, media and fixture settings
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
FIXTURE_DIRS = (os.path.join(PROJECT_DIR, "fixtures"),)

# Worker queue settings
HUEY = {
    "huey_class": "huey.SqliteHuey",
    "name": DATABASES["default"]["NAME"],
    "filename": os.path.join(BASE_DIR, "huey.sqlite3"),
    "results": True,
    "store_none": False,
    "immediate": False,
    "utc": True,
}

# Health check settings
HEALTH_CHECK = {
    "DISK_USAGE_MAX": 90,  # percent
    "MEMORY_MIN": 200,  # in MB
}


# Email settings
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
EMAIL_TIMEOUT = 5

# Admin settings
ADMIN_URL = "admin/"
ADMINS = [("""{{cookiecutter.author_name}}""", "{{cookiecutter.email}}")]
MANAGERS = ADMINS

# Logging settings
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(levelname)s %(asctime)s %(module)s "
                "%(process)d %(thread)d %(message)s"
            )
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}
