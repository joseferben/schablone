from django.urls import path
from sesame.views import LoginView

from {{cookiecutter.project_slug}}.users.views import EmailLoginView

app_name = "users"
urlpatterns = [
    path("login/", EmailLoginView.as_view(), name="email_login"),
    path("login/auth/", LoginView.as_view(), name="login"),
]
