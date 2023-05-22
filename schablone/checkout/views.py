import logging
from typing import Any, Dict

import stripe
from django.urls import reverse
from django.views.generic import TemplateView
from djstripe import settings as djstripe_settings
from djstripe.models.checkout import Session
from djstripe.models.core import Customer

logger = logging.getLogger(__name__)


# TODO add option to trigger test stripe flow (?test=True and only when superadmin?)?
class CreateCheckoutSessionView(TemplateView):
    """
    Create a Stripe Checkout session for the given price_id and redirect
    to the checkout page. No user is created at this stage, we are doing that
    by listening to webhooks.
    """

    template_name = "checkout/checkout.html"

    def get_context_data(self, **kwargs):
        """
        Creates and returns a Stripe Checkout Session
        """
        stripe.api_key = djstripe_settings.djstripe_settings.STRIPE_SECRET_KEY
        price_id = kwargs["price_id"]
        assert (
            price_id is not None and isinstance(price_id, str) and price_id != ""
        ), "invalid price_id provided"
        # Get Parent Context
        context = super().get_context_data(**kwargs)

        # to initialise Stripe.js on the front end
        context[
            "STRIPE_PUBLIC_KEY"
        ] = djstripe_settings.djstripe_settings.STRIPE_PUBLIC_KEY

        success_url = (
            self.request.build_absolute_uri(reverse("checkout:success"))
            + "?session_id={CHECKOUT_SESSION_ID}"
        )
        cancel_url = self.request.build_absolute_uri(reverse("checkout:cancel"))

        # get the id of the Model instance of
        # djstripe_settings.djstripe_settings.get_subscriber_model()
        # here we have assumed it is the Django User model. It could be a Team,
        # Company model too.
        # note that it needs to have an email field.
        # id = self.request.user.id

        # example of how to insert the SUBSCRIBER_CUSTOMER_KEY: id in the metadata
        # to add customer.subscriber to the newly created/updated customer.
        # metadata = {
        #     f"{djstripe_settings.djstripe_settings.SUBSCRIBER_CUSTOMER_KEY}": id
        # }

        logger.info("Customer Object not in DB.")

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": price_id,
                    "quantity": 1,
                },
            ],
            mode="subscription",
            success_url=success_url,
            cancel_url=cancel_url,
            # metadata=metadata,
        )

        context["CHECKOUT_SESSION_ID"] = session.id

        return context


class CheckoutSuccessView(TemplateView):
    """
    Successfull checkout happened, the Stripe checkout session id
    is in the URL query parameter session_id
    """

    template_name = "checkout/checkout_success.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        session_id = self.request.GET.get("session_id")
        if session_id is not None:
            session = Session.objects.filter(id=session_id).first()
            if session is not None:
                customer = session.customer
                context["customer"] = customer
        return context


class CheckoutCancelView(TemplateView):
    """
    Checkout was cancelled.
    """

    template_name = "checkout/checkout_cancel.html"


class CheckoutSuccessViewTest(CheckoutSuccessView):
    """
    Test checkout success view in development.
    """

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return {"customer": Customer.objects.get_or_create(name="Hans Peter", id=1)[0]}


class CheckoutCancelViewTest(CheckoutCancelView):
    """Test checkout cancel view in development."""

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return {"customer": Customer.objects.get_or_create(name="Hans Peter", id=1)[0]}
