import paypalrestsdk
from flask import current_app
from db import db
from models.enums import RoleType
from models.user import UserModel


class PaymentManager:
    @staticmethod
    def configure_paypal():
        paypalrestsdk.configure({
            "mode": "sandbox",
            "client_id": current_app.config["PAYPAL_CLIENT_ID"],
            "client_secret": current_app.config["PAYPAL_CLIENT_SECRET"]
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
                "return_url": f"{current_app.config['CLIENT_URL']}/success?user_id={user_pk}",
                "cancel_url": f"{current_app.config['CLIENT_URL']}/cancel"
            },
            "transactions": [{
                "amount": {
                    "total": "10.00",
                    "currency": "BGN"
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
        user.role = RoleType.super_user
        db.session.flush()