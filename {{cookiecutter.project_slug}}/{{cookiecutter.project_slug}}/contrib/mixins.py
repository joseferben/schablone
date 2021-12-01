from django.db import models


class EntityMixin:
    id = models.BigAutoField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
