from chalice import Blueprint
from chalicelib.utils.ssm import get_firebase_credential


extra_routes_signup = Blueprint(__name__)
creds = get_firebase_credential(parameter="firebase-client")


@extra_routes_signup.route("/signup", methods=["POST"])
def signup():
    return {"hello": "world"}
