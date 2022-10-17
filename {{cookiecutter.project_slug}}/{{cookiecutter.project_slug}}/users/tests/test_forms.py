"""
Module for all Form Tests.
"""
import pytest

from {{cookiecutter.project_slug}}.users.forms import EmailLoginForm
from {{cookiecutter.project_slug}}.users.models import User

pytestmark = pytest.mark.django_db


class TestEmailLoginForm:
    """
    Test class for all tests related to the UserAdminCreationForm
    """

    def test_login(self, user: User):
        form = EmailLoginForm({"email": user.email})

        assert form.is_valid()
        assert len(form.errors) == 0
