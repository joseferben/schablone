from typing import Any

from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import FormView
from sesame.utils import get_query_string

from {{cookiecutter.project_slug}}.users.forms import EmailLoginForm
from {{cookiecutter.project_slug}}.users.notifications import LoginEmail

User = get_user_model()


class EmailLoginView(FormView):
    template_name = "users/email_login.html"
    form_class = EmailLoginForm

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("app:index")
        return super().get(request, *args, **kwargs)

    def get_or_create_user(self, email: str) -> "User":
        """Find or create a user with this email address."""
        User = get_user_model()
        user = User.objects.filter(email=email).first()
        if user is None:
            user = User.objects.create(email=email, username=email)
            # this user has no password yet
            user.set_unusable_password()
            user.save()
        return user

    def create_link(self, user: "User") -> str:
        """Create a login link for this user."""
        link = reverse("users:login")
        link = self.request.build_absolute_uri(link)
        link += get_query_string(user)
        return link

    def send_email(self, user, link):
        """Send an email with this login link to this user."""
        LoginEmail(user, link).send()

    def email_submitted(self, email):
        user = self.get_or_create_user(email)
        link = self.create_link(user)
        self.send_email(user, link)

    def form_valid(self, form):
        self.email_submitted(form.cleaned_data["email"])
        return render(self.request, "users/email_sent.html")
