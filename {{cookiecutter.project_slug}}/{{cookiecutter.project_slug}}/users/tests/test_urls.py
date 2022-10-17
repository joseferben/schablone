import pytest
from django.urls import resolve

pytestmark = pytest.mark.django_db


def test_login():
    assert resolve("/users/login/").view_name == "users:email_login"
    assert resolve("/users/login/auth/").view_name == "users:login"
