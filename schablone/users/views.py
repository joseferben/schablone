from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView

from .forms import EmailLoginForm
from .models import User
from .notifications import LoginEmail


class EmailLoginView(FormView):
    template_name = "users/email_login.html"
    form_class = EmailLoginForm

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("classes:dashboard")
        return super().get(request, *args, **kwargs)

    def get_or_create_user(self, email: str) -> User:
        """Find or create a user with this email address."""
        user = User.objects.filter(email=email).first()
        if user is None:
            user = User.objects.create(email=email)
            # this user has no password yet
            user.set_unusable_password()
            user.save()
        return user

    def send_email(self, user):
        """Send an email with this login link to this user."""
        LoginEmail(user).send(raise_exception=True)  # type: ignore [call-arg]

    def email_submitted(self, email):
        user = self.get_or_create_user(email)
        self.send_email(user)

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        self.email_submitted(email)
        context = self.get_context_data()
        context["email"] = email
        return render(self.request, "users/email_sent.html", context)
