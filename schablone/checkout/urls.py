from django.conf import settings
from django.urls import path

from .views import (
    CheckoutCancelView,
    CheckoutCancelViewTest,
    CheckoutSuccessView,
    CheckoutSuccessViewTest,
    CreateCheckoutSessionView,
)

app_name = "checkout"

urlpatterns = [
    path(
        "create/<str:price_id>/",
        CreateCheckoutSessionView.as_view(),
        name="create",
    ),
    path("success/", CheckoutSuccessView.as_view(), name="success"),
    path("cancel/", CheckoutCancelView.as_view(), name="cancel"),
]


if settings.DEBUG:
    urlpatterns += [
        path(
            "success/test/",
            CheckoutSuccessViewTest.as_view(),
            name="success_test",
        ),
        path(
            "cancel/test/",
            CheckoutCancelViewTest.as_view(),
            name="cancel_test",
        ),
    ]
