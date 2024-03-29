from django.contrib.auth.views import LogoutView
from django.urls import path
from sesame.views import LoginView

from .views import EmailLoginView

app_name = "users"
urlpatterns = [
    path("login/", EmailLoginView.as_view(), name="email_login"),
    path("login/auth/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
