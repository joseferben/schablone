import pytest
from faker import Faker

from {{cookiecutter.project_slug}}.users.models import User

fake = Faker()


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return User(email=fake.email(), username=fake.name(), name=fake.name())
