from flask import request
from flask_restful import Resource
from managers.payment import PaymentManager
from managers.auth import auth
from models import UserModel
from models.enums import RoleType
from utils.decorators import permission_required


class InitiatePayment(Resource):
    @auth.login_required
    @permission_required(RoleType.user)
    def post(self):
        user: UserModel = auth.current_user()
        payment = PaymentManager.create_payment(user.pk)
        approval_url = next(
            link.href for link in payment.links if link.rel == "approval_url"
        )
        #Remove jsonify
        return {"approval_url": approval_url}


class PaymentSuccess(Resource):
    def get(self):
        # user_pk = request.args.get("user_pk")
        user = request.get_json()
        # try:
        PaymentManager.upgrade_user_to_superuser(user["user_pk"])
        return {"message": "You have been upgraded to superuser!"}
        # except NotFound:
        #     return jsonify({"status": "failure", "message": "User not found."}), 404


class PaymentCancel(Resource):
    def get(self):
        return {"message": "Payment was cancelled."}, 402
