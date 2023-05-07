import pytest
from faker import Faker

from {{cookiecutter.project_slug}}.users.models import User
from {{cookiecutter.project_slug}}.users.tasks import get_users_count

pytestmark = pytest.mark.django_db
fake = Faker()

def test_user_count(settings):
    """A basic test to execute the get_users_count task."""
    User.objects.create(email=fake.email())
    User.objects.create(email=fake.email())
    User.objects.create(email=fake.email())
    assert get_users_count()() == 3  # type: ignore
