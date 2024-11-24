from chalice import Blueprint
from chalicelib.utils.ssm import get_firebase_credential

import json

import pyrebase


extra_routes_signup = Blueprint(__name__)
creds = get_firebase_credential(parameter="firebase-client")
firebase = pyrebase.initialize_app(json.loads(creds)).auth()


@extra_routes_signup.route("/refresh", methods=["POST"])
def refresh():
    try:
        body = extra_routes_signup.current_request.json_body
        refreshed_user = firebase.refresh(body.get("refresh_token"))
        return refreshed_user
    except Exception as e:
        return {"error": str(e)}
