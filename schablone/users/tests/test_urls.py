from django.urls import resolve


def test_login():
    assert resolve("/users/login/").view_name == "users:email_login"
    assert resolve("/users/login/auth/").view_name == "users:login"
