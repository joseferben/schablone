import re

import pytest
from django.test.client import Client
from django.urls import reverse
from sesame.utils import get_query_string, get_user

from {{cookiecutter.project_slug}}.users.models import User

pytestmark = pytest.mark.django_db


class TestEmailLoginView:
    def test_email_login(self, user: User, client: Client, mailoutbox):
        response = client.post(
            reverse("users:email_login"),
            follow=True,
            data={
                "email": user.email,
            },
        )
        assert response.status_code == 200
        match = re.search(r"\?sesame=([^ \n]+)", mailoutbox[0].body)
        sesame_value = match.group(1)
        authenticated_user = get_user(sesame_value)
        assert authenticated_user == user


    def test_email_register(self, client: Client, mailoutbox):
        email = "foo@example.com"
        response = client.post(
            reverse("users:email_login"),
            follow=True,
            data={
                "email": email,
            },
        )
        user = User.objects.get(email=email)
        assert response.status_code == 200
        assert get_query_string(user) in mailoutbox[0].body

    def test_login(self, user: User, client: Client):
        link = reverse("users:login")
        link += get_query_string(user)
        response = client.get(link, follow=True)

        assert response.status_code == 200
