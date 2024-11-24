from chalice import Chalice

from chalicelib.views.singup import extra_routes_signup
from chalicelib.views.login import extra_routes_login
from chalicelib.views.refresh import extra_routes_refresh

app = Chalice(app_name="auth-service")

app.register_blueprint(extra_routes_signup)
app.register_blueprint(extra_routes_login)
app.register_blueprint(extra_routes_refresh)
