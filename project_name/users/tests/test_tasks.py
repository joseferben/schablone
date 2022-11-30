import pytest

from {{project_name}}.users.tasks import get_users_count
from {{project_name}}.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_user_count(settings):
    """A basic test to execute the get_users_count task."""
    UserFactory.create_batch(3)
    assert get_users_count()() == 3  # type: ignore
