import pytest
from faker import Faker

from schablone.users.models import User

fake = Faker()


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return User.objects.create(
        email=fake.email(), name=fake.name(), password=fake.password()
    )
