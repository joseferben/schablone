from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView

from {{cookiecutter.project_slug}}.users.forms import EmailLoginForm
from {{cookiecutter.project_slug}}.users.models import User
from {{cookiecutter.project_slug}}.users.notifications import LoginEmail
from {{cookiecutter.project_slug}}.users.shortcuts import get_magic_link


class EmailLoginView(FormView):
    template_name = "users/email_login.html"
    form_class = EmailLoginForm

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("app:index")
        return super().get(request, *args, **kwargs)

    def get_or_create_user(self, email: str) -> User:
        """Find or create a user with this email address."""
        user = User.objects.filter(email=email).first()
        if user is None:
            user = User.objects.create(email=email, username=email)
            # this user has no password yet
            user.set_unusable_password()
            user.save()
        return user

    def send_email(self, user, link):
        """Send an email with this login link to this user."""
        LoginEmail(user, link).send()

    def email_submitted(self, email):
        user = self.get_or_create_user(email)
        link = get_magic_link(user)
        self.send_email(user, link)

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        self.email_submitted(email)
        context = self.get_context_data()
        context["email"] = email
        return render(self.request, "users/email_sent.html", context)

