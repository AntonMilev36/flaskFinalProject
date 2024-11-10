from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)
CORS(app)


@app.teardown_request
def commit_transaction_on_teardown(exception=None):
    if exception is None:
        try:
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            return (
                jsonify(
                    {
                        "error": "An error occurred while saving data. Please try again later"
                    }
                ), 500,
            )
        else:
            db.session.rollback()
            return (
                jsonify(
                    {
                        "error": "An unexpected error occurred. Please contact if the issue persists"
                    }
                ), 500
            )


@app.teardown_appcontext
def shutdown_session(response, exception=None):
    db.session.remove()
    return response


[api.add_resource(*route) for route in routes]
