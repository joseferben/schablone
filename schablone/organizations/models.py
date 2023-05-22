from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel
from djstripe.models.core import Customer

User = get_user_model()


class Organization(TimeStampedModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True
    )

    @property
    def email(self) -> str:
        return self.owner.email  # type: ignore


class Membership(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "organization")
