"""
Module for all Form Tests.
"""
import pytest

from {{project_name}}.users.forms import EmailLoginForm
from {{project_name}}.users.models import User

pytestmark = pytest.mark.django_db


class TestEmailLoginForm:
    """
    Test class for all tests related to the UserAdminCreationForm
    """

    def test_login(self, user: User):
        form = EmailLoginForm({"email": user.email})

        assert form.is_valid()
        assert len(form.errors) == 0
