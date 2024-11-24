from chalice import Chalice
from chalicelib.views.singup import extra_routes_signup

app = Chalice(app_name="auth-service")

app.register_blueprint(extra_routes_signup)
