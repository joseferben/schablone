import os

from django import template
from django.conf import settings

register = template.Library()


@register.filter(name="debug")
def debug():
    return settings.DEBUG


@register.filter(name="env")
def env(key):
    return os.environ.get(key)
