from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class Customer(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    # put your fields here
