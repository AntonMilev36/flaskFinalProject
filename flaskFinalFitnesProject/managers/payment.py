import paypalrestsdk
from decouple import config
from db import db
from models.enums import RoleType
from models.user import UserModel
from werkzeug.exceptions import NotFound


class PaymentManager:
    @staticmethod
    def configure_paypal():
        paypalrestsdk.configure({
            "mode": "sandbox",
            "client_id": config("CLIENT_ID"),
            "client_secret": config("PAYPAL_SECRET")
        })

    @staticmethod
    def create_payment(user_pk):
        PaymentManager.configure_paypal()

        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": f"{config("CLIENT_URL")}/success?user_pk={user_pk}",
                "cancel_url": f"{config("CLIENT_URL")}/cancel"
            },
            "transactions": [{
                "amount": {
                    "total": "10.00",
                    "currency": "EUR"
                },
                "description": "Upgrade to Superuser"
            }]
        })

        if payment.create():
            return payment
        else:
            raise Exception("PayPal Payment creation failed.")

    @staticmethod
    def upgrade_user_to_superuser(user_pk):
        user = UserModel.query.get(user_pk)
        if not user:
            raise NotFound
        user.role = RoleType.super_user
        db.session.flush()